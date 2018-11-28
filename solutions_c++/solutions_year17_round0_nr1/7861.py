#include <iostream>
#include <string>

using namespace std;


int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		int k, c = 0;
		string p;
		cin >> p >> k;
		for (int i = 0; i <= int(p.size()) - k; ++i){
			if (p[i] == '-'){
				for (int j = i; j < i + k; ++j){
					     if (p[j] == '-') p[j] = '+';
					else if (p[j] == '+') p[j] = '-';
				//	else cerr << "ayy lmao" << endl;
				}
				++c;
			}
		}
		cout << "Case #" << t << ": ";
		bool b = true;
		for (int i = int(p.size()) - k + 1; b and i < int(p.size()); ++i) if (p[i] == '-') b = false;
		if (b) cout << c;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
