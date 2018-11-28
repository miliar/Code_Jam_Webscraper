//Blake Oliveira :)

#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

void setNine(string &strnum, int pos) {
	for(int i = pos; i < strnum.size(); ++i)
		strnum[i] = '9';
}

void main() {
	int num, i = 0;
	unsigned long long mod;
	cin >> num;
	while(num--) {
		if(i != 0)
			cout << endl;

		cin >> mod;

		bool check = false;
		string strnum = to_string(mod);

		for(int i = 0; i < strnum.size() - 1; ++i) {
			if(strnum[i] > strnum[i + 1]) {
				for(int j = i + 1; j > 0; --j) {
					if(strnum[j] - 1 == '0' - 1 || strnum[j - 1] > strnum[j]) {
						strnum[j] = '9';
						strnum[j - 1]--;
						check = true;
					}
				}
				if(!check)
					strnum[i] -= 1;
				check = false;
				setNine(strnum, i + 1);
			}
		}

		i++;
		cout << "Case #" << i << ": " << atoll(strnum.c_str());
	}
}