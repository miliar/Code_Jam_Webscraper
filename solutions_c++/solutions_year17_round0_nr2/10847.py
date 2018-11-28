#include <iostream>
using namespace std;

int main(void) {

   int t = 0;
   int num = 0;
   int nextnum = 1;
   cin >> t;

   for(int i = 0; i < t; i++) {
	cin >> num;
	nextnum = num;
	while(nextnum >= 0) {
		num = nextnum;
		while(num) {
			if(num  % 10 < ((num % 100) / 10)) {
				break;
			}
			num /= 10;
			if(!num){
				cout << "Case #" << i + 1 << ": " << nextnum << endl;
                nextnum = 0;
			}
		}
		nextnum--;
	}
   }
   return 0;

}
