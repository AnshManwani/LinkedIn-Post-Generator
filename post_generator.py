from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def generate_post(length, language, tag, tone, audience):
    prompt = get_prompt(length, language, tag, tone, audience)
    response = llm.invoke(prompt)
    return response.content

def get_prompt(length, language, tag, tone, audience):
    length_str = get_length_str(length)

    prompt = f'''
Generate a LinkedIn post using the information below. Do not add any preamble or explanation.

1) Topic: {tag}
2) Length: {length_str}
3) Language: {language}  # If Hinglish, use English script but mix Hindi & English.
4) Tone: {tone}  # The voice/style of the post (e.g., Motivational, Friendly).
5) Audience: {audience}  # The intended audience (e.g., Recruiters, Students).

Please ensure the post includes:
- An engaging hook or opening sentence that captures attention.
- A clear call-to-action (CTA) at the end (examples: "What are your thoughts?", "Comment below!").
- 3 to 5 relevant hashtags related to the topic and content at the end of the post.

'''

    examples = few_shot.get_filtered_posts(length, language, tag)

    if examples:
        prompt += "Use the writing style as demonstrated in the following examples:\n"

    for i, post in enumerate(examples):
        prompt += f"\nExample {i + 1}:\n{post['text']}\n"
        if i == 1:  # use at most two examples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Short", "English", "Mental Health", "Motivational", "Students"))
