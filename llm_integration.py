import openai

# Set up the OpenAI API key
openai.api_key = "Open_api_key"  # Replace with your OpenAI API key


def analyze_sales_data(prompt):
    """
    Use GPT-3.5-turbo to analyze sales data and generate insights.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert data analyst."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=150,
    )
    return response["choices"][0]["message"]["content"].strip()
