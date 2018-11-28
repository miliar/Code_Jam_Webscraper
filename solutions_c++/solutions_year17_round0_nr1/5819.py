#include <iostream>
using namespace std;

int n, k, tt, tc, ans;
string s;

int flip(int a, int k, int len){
	if(s[a] == '-'){
		for(int i = 1; i < k; i++){
			if(a+i >= len || s[a+i] == '-') return false;
		}
		if(a+k-1 < len && s[a+k-1] == '-'){
			for(int i = a; i < a+k; i++) s[i] = '+';
			return true;
		} else {
			return false;
		}

	}
	return false;
}

int allmin(int a, int k, int len){
	if(a+k >= len) return false;
	for(int i = a; i < a+k; i++){
		if(s[i] == '+') return false;
	}
	for(int i = a; i < a+k; i++){
		s[i] = '+';
	}
	return true;
}

int main(){
	cin >> tt;
	for(int tc = 1; tc <= tt; tc++){
		ans = 0;
		cin >> s >> k;
		int i = 0, len = s.length();
		while(i < len){
			if(s[i] == '+'){
				i++;
				continue;
			}
			if(s[i] == '-'){
				if(flip(i, k, len)){
					ans += 2;
					i += k;
				} else {
					if(i+k-1 >= len) break;
					for(int j = i; j < i+k; j++){
						if(s[j] == '+') s[j] = '-'; else s[j] = '+';
					}
					ans++;
					i++;
				}
			}
		}
		if(ans != -1){
			for(int i = 0; i < len; i++){
				if(s[i] == '-'){
					cout << "Case #" << tc << ": IMPOSSIBLE\n";
					break;
				}
				if(i == len-1){
					cout << "Case #" << tc << ": " << ans << "\n";
				}
			}
		}
	}
}