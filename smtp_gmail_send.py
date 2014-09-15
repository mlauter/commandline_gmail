import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

if __name__ == '__main__':
    from_addr = input("Enter your gmail address:\n")
    to_addr_list = []
    print("Enter the addresses of your recipients.\nWhen you are done, type 'done'\n")
    while 1:
        usrinput = input("Enter the address of a recipient:\n")
        if usrinput == "done":
            break
        else:
            to_addr_list.append(usrinput)
    cc_addr_list = []
    print("Enter addresses to cc.\nWhen you are done, type 'done'\n")
    while 1:
        usrinput = input("Enter an address to cc:\n")
        if usrinput == "done":
            break
        else:
            cc_addr_list.append(usrinput)
    subject = input("Enter a subject:\n")
    message = input("Enter your message:\n")
    login = input("Enter your gmail username: ")
    password = input("Enter your gmail app password: ")

    sendemail(from_addr = from_addr,
              to_addr_list = to_addr_list, 
              cc_addr_list = cc_addr_list,
              subject = subject, 
              message = message,
              login = login,
              password = password)

