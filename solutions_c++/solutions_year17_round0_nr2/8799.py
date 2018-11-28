#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, T;



	cin >> T;
	string s;

	for(t = 1; t <= T; ++t){
		cin.ignore(256, '\n');
		cin >> s;

		s = "0" + s;
		int tam = s.size();

		for(int i = tam - 1; i > 0; --i){
			if(s[i] < s[i-1]){
				s[i-1]--;
				s = s.substr(0, i) + string(tam - i,'9');
			}
		}

		printf("Case #%d: ", t);
		bool xgh = false;
		for(auto & c : s){
			if(c != '0') xgh = true;
			if(xgh) cout << c;
		}
		cout << "\n";
	}

	return 0;
}
