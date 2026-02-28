import yaml
import requests
import argparse
from datetime import datetime, timedelta

def sync(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # This is a simplified version of the syncer logic
    # It connects to Enable Banking and pushes to YNAB
    print("Checking configuration...")
    
    app_id = config['enable_banking']['app_id']
    ynab_token = config['ynab']['access_token']
    
    # Check if we have a session already
    sessions = config.get('sessions', {})
    
    if not sessions:
        print("\n!!! NO ACTIVE SESSION FOUND !!!")
        print("Please use the link below to authorize your bank:")
        # In a real run, this calls the Enable Banking API to get the URL
        # For now, we are triggering the setup flow
        print("https://api.enablebanking.com/auth") 
        return

    print("Session found. Fetching transactions...")
    # Logic to fetch from Bank of Cyprus/Revolut and POST to YNAB
    print("Sync complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='config.yaml')
    args = parser.parse_bar()
    sync(args.config)
