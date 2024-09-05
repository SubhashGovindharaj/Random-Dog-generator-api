import streamlit as st
import requests

# Function to fetch a random dog image from The Dog API
def fetch_dog_image():
    api_url = "https://api.thedogapi.com/v1/images/search"
    
    try:
        # Make the API call
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the response as JSON
        data = response.json()

        # Return the image URL from the response
        return data[0]["url"]

    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        st.error(f"Error occurred: {req_err}")
    except Exception as err:
        st.error(f"An unexpected error occurred: {err}")

# Streamlit app interface
def main():
    st.title("Random Dog Image Fetcher")

    # Button to fetch a new dog image
    if st.button("Get a random dog image"):
        image_url = fetch_dog_image()

        if image_url:
            # Display the dog image using Streamlit's image component
            st.image(image_url, caption="Here's a random dog for you!", use_column_width=True)

if __name__ == "__main__":
    main()