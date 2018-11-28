#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main() {
	int T;
	cin >>T;

	for(int t = 1; t <= T; ++t) {
		string num;
		cin >> num;

		int RMT;
		for(RMT = 0; RMT < num.size() - 1; ++RMT) {
			if(num[RMT+1] < num[RMT])
				break;
		}

		if(RMT + 1 == num.size())
			cout <<"Case #" <<t <<": "<< num <<endl;
		else {
			bool chk = false;
			while(RMT + 1 > 1) {
				if(num[RMT] > num[RMT - 1]) {
					--num[RMT];
					for(int i = RMT + 1; i < num.size(); ++i)
						num[i] = '9';
					
					cout <<"Case #" <<t <<": "<< num <<endl;
					chk = true;
					break;
				}
				else 
					--RMT;
			}
			if(!chk) {
				for(int i = RMT + 1; i < num.size(); ++i)
					num[i] = '9';
				if(num[RMT] == '1')
					num.erase(0, 1);
				else
					--num[RMT];

				cout <<"Case #" <<t <<": "<< num <<endl;
			}
		}	
	}

	return 0;
}