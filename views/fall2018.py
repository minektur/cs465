from flask import render_template

from config import app
from .schedule import *

@app.route('/fall-2018/schedule')
def fall2018schedule():
    static = '/static/lectures/v1/'
    pubs = '/static/pubs/'
    term = '/fall-2018/'
    s = Schedule()

    s.week()

    d = s.day("September 4")

    d.lecture("Cryptography")
    d.reading("Chapter 1")
    d.slide("Introduction",static + 'Introduction.pdf')
    d.slide("Terminology",static + 'Terminology.pdf')
    d.assignment("Homework #1",term + 'homework/homework1')
    
    d = s.day("September 6")
    d.reading("Chapter 2")
    d.slide("Cryptography",static + 'Cryptography.pdf')
    d.slide("AES",static + 'AES.pdf')
    d.lecture("Cryptography")

    s.week()

    d = s.day("September 11")
    d.lecture("AES")
    d.reading("Chapter 3.1 - 3.3.4")
    d.slide("AES",static + 'AES.pdf')

    d = s.day("September 12")
    d.assignment("Homework #2",term + 'homework/homework2')    

    d = s.day("September 13")
    d.lecture("Block Cipher Modes, Authenticated Encryption Modes, and Padding")
    d.reading("Chapter 3.1 - 3.3.7")
    d.reading("How to Choose an Authenticated Encryption Mode (optional)", "https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/")
    d.reading("The Galois/Counter Mode of Operation (GCM) (optional)","http://luca-giuzzi.unibs.it/corsi/Support/papers-cryptography/gcm-spec.pdf")
    d.slide("Block Cipher Modes",static + 'BlockCipherModes.pdf')
    

    s.week()

    d = s.day("September 18")
    d.lecture("Cryptographic Hash Functions")
    d.reading("Chapter 5")
    d.reading('NIST Hash Project (optional)','http://csrc.nist.gov/groups/ST/hash/index.html')
    d.reading('Chinese researchers find first SHA-1 collision 2005','https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html')
    d.reading("Google announces practical collision SHA-1, Feb 2017","https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html")
    d.slide("Cryptographic Hash Functions",static + 'CryptographicHashFunctions.pdf')
    d.assignment("Homework #3",term + 'homework/homework3')

    d = s.day("September 20")
    d.lecture("MAC")
    d.reading("Chapter 3.4, 5.7")
    d.reading("SHA-1 spec",pubs + 'fips180-3_final.pdf')
    d.reading("Why I hate CBC-MAC","https://blog.cryptographyengineering.com/2013/02/15/why-i-hate-cbc-mac/")
    d.slide("MAC",static + "MAC.pdf")

    d = s.day("September 21")
    d.assignment("Project #1: AES",term + 'projects/project1')
    
    s.week()

    d = s.day("September 25")
    d.lecture("Hash Attack")
    d.assignment("Homework #4",term + 'homework/homework4')
    
    d = s.day("September 27")
    d.reading("Chapter 4.4")
    d.lecture("Diffie-Hellman")
    d.slide("Diffie-Hellman",static + "Diffie-Hellman.pdf")

    d = s.day("September 29")
    d.assignment("Project #2: Hash Attack", term + 'projects/project2')
    
    s.week()
    d = s.day("October 2")
    d.lecture("Discuss Homework #5 and Modular Exponentiation")
    d.assignment("Homework #5",term + 'homework/homework5')
    
    d = s.day("October 4")
    d.reading("Chapter 4.3")
    d.lecture("RSA")
    d.slide("RSA",static + "RSA.pdf")
    
    d = s.day("October 5")
    d.assignment("Project #3: MAC Attack", term + 'projects/project3')
    
    s.week()

    d = s.day("October 9")
    d.lecture("No class -- office hours")    
    
    d = s.day("October 11")
    d.reading("Chapter 4.6 - 4.8")
    d.lecture("Public Key Infrastructure and Certificates")
    d.slide("PKI",static + "PKI.pdf")
    d.assignment("Homework #6",term + 'homework/homework6')

    s.week()

    d = s.day("October 15")
    d.assignment("Project #4: Diffie-Hellman", term + 'projects/project4')

    d = s.day("October 16")
    d.lecture("Exam Review")
    d.assignment("Homework #7",term + 'homework/homework7')
    d.reading("Midterm 1 Study Guide","help/study-guide-midterm1")

    d = s.day("October 17")
    d.assignment("Exam #1 first day in the testing center")

    d = s.day("October 18")
    d.lecture("No Class")

    d = s.day("October 20")
    d.assignment("Exam #1 last day in the testing center")

    s.week()

    d = s.day("October 23")
    d.lecture("TLS")
    d.slide("TLS",static + "TLS.pdf")
    d.reading("The First Few Milliseconds of an HTTPS Connection","http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html")
    d.reading("The Illustrated TLS Connection","https://tls.ulfheim.net/")
    
    d = s.day("October 25")
    d.lecture("TLS, Project #5 Discussion")

    d = s.day("October 27")
    d.assignment("Project #5: RSA", term + 'projects/project5')

    s.week()

    d = s.day("October 30")
    d.lecture("TLS")
    d.reading("Chapter 10.3")
    d.slide("TLS Research",static + "TLSResearch.pdf")
    d.assignment("Homework #8",term + 'homework/homework8')
    
    d = s.day("November 1")
    d.lecture("Exam Review")

    d = s.day("November 2")
    d.assignment("Project #6: TLS", term + 'projects/project6')

    s.week()

    d = s.day("November 6")
    d.lecture("Passwords")
    d.reading("Chapter 7.3")
    d.slide("Passwords",static + "Passwords.pdf")
    d.reading("Easy Ways to Build a Better P@$5w0rd (NIST)", "https://www.nist.gov/blogs/taking-measure/easy-ways-build-better-p5w0rd")
    d.reading("How to Devise Passwords That Drive Hackers Away","https://www.nytimes.com/2012/11/08/technology/personaltech/how-to-devise-passwords-that-drive-hackers-away.html")
    
    
    d = s.day("November 8")
    d.assignment("Homework #9", term + 'homework/homework9')
    d.lecture("Passwords")
    d.reading("An Administrator's Guide to Password Research","https://www.microsoft.com/en-us/research/publication/an-administrators-guide-to-internet-password-research/")
    d.reading("The Quest to Replace Passwords: A Framework for Comparative Evaluation of Web Authentication Schemes","https://ieeexplore.ieee.org/document/6234436")

    d = s.day("November 10")
    d.assignment("Project #7: Password Cracking", term + 'projects/project7')

    s.week()

    d = s.day("November 13")
    d.lecture("Buffer Overflow")
    d.slide("Buffer Overflow",static + "BufferOverflow.pdf")
    d.reading("Chapter 11.2")
    d.reading("Smashing the Stack For Fun and Profit","http://www.phrack.org/issues/49/14.html#article")
    d.reading("Smashing the Stack For Fun and Profit (Today)","https://travisf.net/smashing-the-stack-today")
    d.reading("Smashing the Stack in 2011","https://paulmakowski.wordpress.com/2011/01/25/smashing-the-stack-in-2011/")
    d.reading("Smashing the Modern Stack for Fun and Profit","https://www.ethicalhacker.net/columns/heffner/smashing-the-modern-stack-for-fun-and-profit/")
    
    d = s.day("November 15")
    d.lecture("Buffer Overflow")
    d.assignment("Homework #10", term + 'homework/homework10')

    s.week()
    
    d = s.day("November 20")
    d.lecture("No Class -- Friday Instruction")
    d.assignment("Project #8: Buffer Overflow", term + 'projects/project8')
    
    d = s.day("November 22")
    d.lecture("Thanksgiving Holiday")

    s.week()

    d = s.day("November 27")
    d.lecture("Secure Email")
    d.slide("Secure Email",static + "SecureEmail.pdf")
    d.assignment("Homework #11",term + 'homework/homework11')
    
    d = s.day("November 29")
    d.lecture("Exam Review")

    d = s.day("November 30")
    d.assignment("Project #9: Extracting Secrets", term + 'projects/project9')

    s.week()

    d = s.day("December 4")
    d.lecture("No Class")
    d.assignment("Homework #12", term + 'homework/homework12')
    
    d = s.day("December 5")
    d.assignment("Exam #2 first day in testing center")

    d = s.day("December 8")
    d.assignment("Exam #2 last day in testing center (ends at 3pm)")

    s.week()

    d = s.day("December 11")
    d.lecture("Social Engineering")
    d.assignment("Project #10: PGP and S/MIME", term + 'projects/project10')
    d.slide("Demystifying the Secure Enclave Processor","https://www.youtube.com/watch?v=7UNeUT_sRos")
    
    d = s.day("December 13")
    d.lecture("Signal")
    d.slide("Signal",static + "Signal.pdf")
    d.assignment("Project #11: Extra Credit", term + 'projects/project11')

    
    return render_template('fall-2018/schedule.html',active='schedule', weeks=s.weeks)
