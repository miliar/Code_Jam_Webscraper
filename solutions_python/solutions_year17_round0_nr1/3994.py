
def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
      results = count_flips(n,m)
      print "Case #{}: {}".format(i, results)
      # check out .format's specification for more form
      
def count_flips(pancakes, flipper):
    flipper_size = int(flipper);
    pancake_bits = pancakes.replace('-', '0').replace('+', '1')
    return count_bit_flips([pancake_bits], flipper_size, tested={ pancake_bits: True });

def count_bit_flips(to_test, flipper_size, tested={}, count=0):
    next_to_test = []
    while len(to_test) > 0:
        pancake_bits = to_test.pop();
        if pancake_bits.count('1') == len(pancake_bits):
            return count
        number_of_pancakes = len(pancake_bits);
        for position in xrange(0, number_of_pancakes):
            #print position + int(flipper_size)
            if position + flipper_size > (number_of_pancakes-1):
                flipped = flip(pancake_bits, number_of_pancakes - flipper_size , flipper_size )

                if flipped not in tested:
                    next_to_test.append(flipped)
                    tested[flipped] = True
                break;
            else:
                flipped = flip(pancake_bits,position, flipper_size)
                if flipped not in tested:
                    next_to_test.append(flipped)
                    tested[flipped] = True

    if len(next_to_test) == 0:
        return 'IMPOSSIBLE'
    count += 1
    return count_bit_flips(next_to_test, flipper_size, tested, count )



def flip(pancake_bits, start, flipper):
    replace = '';
    for pancake in pancake_bits[start: start + flipper]:
        if pancake == '1':
            replace += '0'
        else:
            replace += '1'
    results = pancake_bits[0:start] + replace +  pancake_bits[start + flipper:]
    return results;
    

  
if __name__ == '__main__':
    main();
