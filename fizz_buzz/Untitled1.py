def fizzbuzz(n):
    for x in xrange(1,n):
        if x%3 == 0 and x%5 == 0:
            print "fizz buzz"
        elif x%3 == 0:
            print "fizz"
        elif x%5 == 0:
            print "buzz"
        else:
            print x
fizzbuzz(10)
