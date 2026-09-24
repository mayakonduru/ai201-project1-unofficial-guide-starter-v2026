def judge(question, expects, answer, results): 
  if not answer:
        return False
    return expects.lower() in answer.lower()
