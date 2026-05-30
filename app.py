print("CyberGuard AI")

question = input("Ask a cybersecurity question: ")

if "phishing" in question.lower():
    print("Phishing is a social engineering attack used to steal sensitive information.")
elif "ransomware" in question.lower():
    print("Ransomware encrypts files and demands payment.")
else:
    print("I don't know that answer yet.")
