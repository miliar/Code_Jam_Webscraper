#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main(void) {
	string tmpin;
	getline(cin, tmpin);

	int count = stoi(tmpin);

	for(int x = 0; x < count; ++x) {
		getline(cin, tmpin);
		unsigned long long num = stoull(tmpin);

		string tmptmpin = tmpin;

		while(true) {
			sort(tmptmpin.begin(), tmptmpin.end());
			if(tmpin == tmptmpin) break;

			unsigned long long magnitude = 0;

			while(true) {
				sort(tmptmpin.begin(), tmptmpin.end());
				if(tmpin == tmptmpin) break;

				bool hadtobreak = false;
				for(int i = 0; i < tmpin.size()-magnitude; ++i) {
					if(tmpin[tmpin.size()-magnitude-1] < tmpin[tmpin.size()-magnitude-2-i]) {
						hadtobreak = true;
						break;
					}
				}

				if(!hadtobreak) {
					++magnitude;
					continue;
				}

				if(!magnitude)
					--num;
				else {
					unsigned long long calced = pow(10, magnitude);
					num -= num % calced + 1;
				}

				tmpin = to_string(num);
				tmptmpin = tmpin;
			}
		}

		cout << "Case #" << (x + 1) << ": " << num << endl;
	}

	return 0;
}
