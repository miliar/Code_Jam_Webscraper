#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	
	for(int z = 1; z <= t; z++){
		cout << "Case #" << z << ": ";
		string s;
		cin >> s;
		int k;
		cin >> k;
		int res = 0;
		bool flag = false;
		for(int i = 0; i <= s.size() - k; i++){
			if(s[i] == '-'){
				res++;
				for(int j = i; j < i+k; j++){
					s[j] = (s[j] == '-' ? '+':'-');
				}
			}
		}

		for(int i = s.size() - k; i < s.size(); i++){
			flag |= (s[i] == '-');
		}
		if(flag) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}
	
	return 0;
}
