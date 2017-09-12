from __builtin__ import exit
if __name__ == '__main__':
    n = int(raw_input())
if ((n%2) != 0):
    print "Weird"
    exit
elif (2 < n < 5):
    print "Not Weird"
    exit
elif (6 < n < 20):
    print "Weird"
    exit
elif (n > 20):
    print "Not Weird"
    exit