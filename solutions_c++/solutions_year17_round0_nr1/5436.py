#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int a = 1; a <= t; a++){
		string s;
		int thr, rpc =  0, k;
		cin >> s >> k;
		int size = s.size();
		bool impossible = false;
 			for(int i = 0; i < size; i++){
				thr = 0;
				for(int j = i; j < i + k; j++){
					if(s[j] == '-') thr++;
					else if(s[j] == '+' && thr > 0) thr++;
				}
			if(thr == k){
				for(int j = i; j < i + k; j++){
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
				rpc++;
			}
			}
			for(int i = 0; i < size; i++){
				if(s[i] == '-'){
					impossible = true;
					break;
				}
			}
		if(impossible) 	cout << "Case #" << a << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << a << ": " << rpc << endl;
		}
	return 0;
}