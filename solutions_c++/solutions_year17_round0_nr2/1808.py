#include <iostream>

using namespace std;

// logN
bool is_tidy(long long n, long long& next)
{
   long long temp = n;
   long long last_digit = n % 10;
   long long base = 1;
   temp /= 10;
   while (temp != 0) {
       long long now_digit = temp % 10;
       if (now_digit > last_digit) {
           long long sum = 0;
           while (temp != 0) {
               sum += ((temp % 10) * base * 10);
               base *= 10;
               temp /= 10;
           }
           next = sum - 1;
           return false;
       }
       last_digit = now_digit;
       temp /= 10;
       base *= 10;
   }
   return true;
}

int main(void)
{
    long long t;
    cin >> t;
    for (long long i = 0; i < t; ++i) {
        long long n;
        cin >> n;
//        for (long long j = n; j >= 0; --j) {
        long long j = n;
        while (j >= 0) {
            long long next = -1;
            if (is_tidy(j, next)) {
                cout << "Case #" << (i + 1) << ": " << j << endl;
                break;
            } else {
                j = next;
            }
        }
    }
    return 0;
}

