import wikipedia
import wolframalpha

while True:
        input = raw_input("Q: ")

        try:
            #wolframalpha
            app_id = "*******************"
            client = wolframalpha.Client(app_id)
            result = client.query(input)
            answer = next(result.results).text
            print answer
        except:
            #wikipedia
            print wikipedia.summary(input, sentences=5)
