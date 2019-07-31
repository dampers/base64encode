from django.shortcuts import render
from PIL import Image
import binascii

# Create your views here.

def home(request):
    return render(request, 'encode/home.html')

def str2bin(message):
    binary = bin(int(binascii.hexlify(message.encode()), 16))
    return binary[2:].encode()

def encode64(request):
    full_text = request.GET['fulltext']
    binary = str2bin(full_text)
    return render(request, 'encode/encode64.html', {'fulltext':binary})