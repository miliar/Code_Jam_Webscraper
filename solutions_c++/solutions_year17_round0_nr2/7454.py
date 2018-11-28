#include <bits/stdc++.h>

using namespace std;

typedef long long int lli;

int main() {
	ios_base::sync_with_stdio(0);

	int z;
	cin >> z;
	for(int i = 1; i <= z; i++) {
		string s;
		cin >> s;

		for(int i = 0; i < s.size()-1; i++) {
			if(s[i+1] < s[i]) {
				while(i-1 >= 0 && s[i-1] == s[i]) i--;
				s[i]--;
				for(int j = i+1; j < s.size(); j++) s[j] = '9';
				break;
			}
		}

		int it = 0;
		while(s[it] == '0') it++;

		cout << "Case #" << i << ": " << s.substr(it, -1) << endl;
	}

	return 0;
}


