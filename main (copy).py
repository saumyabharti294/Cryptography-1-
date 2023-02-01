from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
def generate_key():
 private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,
 )
 public = private_key.public_key() #inbuilt
 return private_key,public

def sign(message,private_key):
    message = bytes(str(message), 'utf-8')
    signature = private_key.sign(
     message,
     padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
    )
    return signature

def verify(message,sig,public):
 message = bytes(str(message), 'utf-8')
 try:
  public.verify(
    sig,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
  )
  return True
 except InvalidSignature:
  return False
 except:
   print("Error executing public key")
   return False
   

if __name__=='__main__':
  
   pr,pu=generate_key()     #user1
   pr1,pu1 = generate_key()  #user2
   #print(pr)
   #print(pu)
   
   message ="Hi I am eucalyptus"
   sig = sign(message,pr)
   #print(sig)
   correct = verify(message,sig , pu) #here public key can be changed as per user1 or user2 to chcek the code functionality
   if correct:
    print("successful")
   else:
    print("Failed")
   