from icrawler.builtin import GoogleImageCrawler
import os

def download_images(query, num_images, output_dir):
    crawler = GoogleImageCrawler(storage={'root_dir': os.path.join(output_dir, query.split()[0])})
    crawler.crawl(keyword=query, max_num=num_images)

def create_image_dataset(member_names, max_images_per_member=50):
    base_dir = '/Users/suprita/supriML/image_classification/bts_dataset'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for member in member_names:
        query = member + " BTS"
        download_images(query, max_images_per_member, base_dir)

# BTS members
members = ["RM", "Jin", "Suga", "J-Hope", "Jimin", "V", "Jungkook"]

# Create dataset
create_image_dataset(members)
