import openai


api_key = ""


openai.api_key = api_key


def ask_ai(question):
    conversation_history = [
        {"role": "system", "content": "Sen yardımsever bir yapay zeka asistanısın."},
        {"role": "user", "content": question},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        max_tokens=300,
        temperature=0.8,
    )

    for choice in response["choices"]:
        if "message" in choice and "content" in choice["message"]:
            return choice["message"]["content"]

    return response["choices"][0]["message"]["content"]


def movie_question_maker(q1, q2, q3, q4):
    subQuestion1 = "Bugün " + q1 + " kategorisinde bir film izlemek istiyorum. "
    subQuestion2 = q2 + " yılı civarında vizyona girmiş bir film izlemek istiyorum. "
    subQuestion3 = "IMDB puanı " + q3 + " ve üzeri bir film izlemek istiyorum. "
    
    if(q4 != None):
        subQuestion4 = q4 + " oyuncularının olmasını istiyorum. Eğer bu oyuncular yoksa öneri olarak farklı bir film önerebilirsin."
    else:
        subQuestion4 = ""

    rules = "Yalnızca tek satır olacak şekilde filmin adını cevap olarak ver. Başka hiçbir yorum ekleme."

    question =  subQuestion1 + subQuestion2 + subQuestion3 + subQuestion4 + rules
    return question


def tvseries_question_maker(q1, q2, q3, q4):
    subQuestion1 = "Bugün " + q1 + " kategorisinde bir dizi izlemek istiyorum. "
    subQuestion2 = q2 + " yılı civarında vizyona girmiş bir dizi izlemek istiyorum. "
    subQuestion3 = "IMDB puanı " + q3 + " ve üzeri bir dizi izlemek istiyorum. "
    
    if(q4 != None):
        subQuestion4 = q4 + " oyuncularının olmasını istiyorum. Eğer bu oyuncular yoksa öneri olarak farklı bir dizi önerebilirsin."
    else:
        subQuestion4 = ""

    rules = "Yalnızca tek satır olacak şekilde dizinin adını cevap olarak ver. Başka hiçbir yorum ekleme."

    question =  subQuestion1 + subQuestion2 + subQuestion3 + subQuestion4 + rules
    return question

def music_question_maker(q1, q2, q3, q4):
    subQuestion1 = "Bugün " + q1 + " kategorisinde bir müzik dinlemek istiyorum. "
    subQuestion2 = q2 + " bir müzik olmasını istiyorum. "
    subQuestion3 = q3 + " döneminden bir müzik olmasını istiyorum. "
    subQuestion4 = q4 + " ruh halime uygun bir müzik olmasını istiyorum. "

    rules = "Yalnızca tek satır olacak şekilde müziğin adını ve sanatçısını cevap olarak ver. Başka hiçbir yorum ekleme."

    question =  subQuestion1 + subQuestion2 + subQuestion3 + subQuestion4 + rules
    return question
