#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
#include <time.h>
#include <queue>
#include <stack>
#include <map>
#include <climits>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		std::string num;
		cin >> num;
		
		bool good = false;
		while (!good) {
			bool nineFill = false;
			for (int i = 1; i < num.length(); ++i) {
				if (nineFill) {
					num[i] = '9';
				}
				else{
					int c2 = num[i] - '0';
					int c1 = num[i - 1] - '0';

					if (c1 > c2) {
						num[i] = '9';
						num[i - 1] = '0' + c1 - 1;
						nineFill = true;
					}
				}
			}
			good = !nineFill;
		}
		cout << "Case #" << t << ": " << atoll(num.c_str()) << endl;
	}
	return 0;
}