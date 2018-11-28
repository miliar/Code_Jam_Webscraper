#include <iostream>
#include <string>
using namespace std;
void swap(string &s, int st, int e){
	for(int i = st; i <= e; i++) {
		if(s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
}

int main() {
	string s;
	int k;
	int t;
	cin >> t;
	for(int T = 1; T <= t; T++){
		cin >> s;
		cin >> k;
		int n = s.size();
		int left = 0, right = n-1;
		int ans = 0;
		for(;;){
			while(s[left] == '+') left++;
			if(left+k-1 < n) { 
				swap(s, left, left+k-1); 
				ans++;
			}
			else break;
		}

		for(;;){
			while(s[right] == '+') right--;
			if(right-k+1 >= 0) { 
				swap(s, right-k+1,right); 
				ans++;
			}
			else break;
		}


		bool can = true;
		cout << "Case #" << T << ": "; 
		for(int i = 0; i < n; i++) if(s[i] !='+') { can = false; break;}
		if(can) cout << ans << "\n"; else cout << "IMPOSSIBLE\n";
	}
}
