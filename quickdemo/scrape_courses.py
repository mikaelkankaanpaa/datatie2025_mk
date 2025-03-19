import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_tuni_courses():
    # URL of the course listing page
    url = "https://www.tuni.fi/fi/opiskelijan-opas/opintotiedot/opintojaksot"
    
    # Send GET request to the URL
    response = requests.get(url)
    response.encoding = 'utf-8'  # Ensure proper encoding
    
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all course elements (this will need to be adjusted based on actual HTML structure)
    courses = []
    
    # Find the main content area where courses are listed
    content_area = soup.find('main', {'class': 'main-content'})
    
    if content_area:
        # Find all course links
        course_links = content_area.find_all('a', href=True)
        
        for link in course_links:
            # Extract course information
            course_info = {
                'name': link.get_text(strip=True),
                'url': link['href']
            }
            
            if course_info['name'] and 'opintojaksot' in course_info['url'].lower():
                courses.append(course_info)
    
    # Create DataFrame
    df = pd.DataFrame(courses)
    
    # Save to CSV
    df.to_csv('tuni_courses.csv', index=False, encoding='utf-8')
    print(f"Found {len(courses)} courses. Data saved to tuni_courses.csv")
    return df

if __name__ == "__main__":
    df = scrape_tuni_courses()
    print("\nFirst few courses:")
    print(df.head()) 