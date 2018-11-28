#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(int argv, const char **args) {
	ifstream cin(args[1]);
	ofstream cout(args[2]);
	int tcn;// test case number
	cin >> tcn;

	map<unsigned long long, unsigned long long> counter;
	unsigned long long n, k, occupied = 0,  availible = 1, num1, num2, tmp1, tmp2, tmpCount;
	for (int i = 1; i <= tcn; i++) {
		cin >> n >> k;
		// cout << n << " haha "<< k << endl;

		occupied = 0,  availible = 1;// pain in the ass.....to save memory, I move the original statement out of for loop, caused bug...
		num1 = num2 = n;
		counter[num1] = 1;
		// num1 = (n-1)/2;
		// num2 = n/2;
		// counter[num1] = 1;
		// if (num1 == num2) {
		// 	counter[num2] += 1;
		// } else{
		// 	counter[num2] = 1;
		// }
		
		while (occupied + availible < k) {//not perfect but useful, all 0, 1 seats case truly availble < availble
			tmp1 = (num1-1)/2;
			tmp2 = num2/2;

			// cout << "debugging: " << num1 << ": "  << counter[num1] << " " << num2 << ": " << counter[num2] << endl;

			tmpCount = 0;
			counter[tmp1] = counter[num1];

			if (num1%2 == 0) {
				tmpCount += counter[num1];
			} else {
				counter[tmp1] += counter[num1];
			}

			if (num1 != num2) {
			tmpCount += counter[num2];
			if (num2%2 == 0) {
				counter[tmp1] += counter[num2];
			}else {
				tmpCount += counter[num2];
			}
		}

			if (tmp1 == tmp2) {
				counter[tmp1] += tmpCount;
			}else {
				counter[tmp2] = tmpCount;
			}

			num1 = tmp1;
			num2 = tmp2;
			occupied += availible;
			availible *= 2;
		}


// cout << "Final debugging: " << num1 << ": "  << counter[num1] << " " << num2 << ": " << counter[num2] << endl;
		unsigned long long finalSize;
		if (num1 < num2) {
			finalSize = (k-occupied <= counter[num2])?num2:num1;
		}else {
			finalSize = num1;
		}
		cout << "Case #" << i << ": " << finalSize/2 << " " << (finalSize-1)/2 << endl;
	}
	return 0;
}