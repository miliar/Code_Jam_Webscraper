#include <iostream>
#include <stdint.h>
#include <string>
using namespace std;

bool isTidy (int64_t &in) {
    int64_t n = in;
    int prev = n % 10, count=0;
    while(n > 0) {
        if((n % 10) > prev) {
            n--;
            while(count != 0) {
              n=n*10+9;
              count--;
            }
            in = n;
            return false;
        }
        count++;
        prev = n % 10;
        n /= 10;
    }
    return true;
}

int main() {
	int t;
	cin >> t;
	for(int caseCount = 1; caseCount <= t; caseCount++) {
	   int64_t n;
	   cin >> n;
	   while(!isTidy(n));
	   cout << "Case #" << caseCount << ": " << n << endl;
	}
	return 0;
}
