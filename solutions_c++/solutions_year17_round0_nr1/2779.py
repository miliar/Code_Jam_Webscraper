#include <bits/stdc++.h>
using namespace std;
const int N = 1005;
string S;
inline char inv(char c){ return c == '+' ? '-' : '+';}
int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	int t, k;
	cin >> t;
	for(int tt = 1; tt <= t; tt++){
		cin >> S >> k;
		int n = S.length();
		int ans =0 ;
		bool flag =0;
		for(int i = 0; i < n; i++){
			if(S[i] == '+') continue;
			if(i > n - k){
				flag = 1;
				continue;
			}
			ans ++;
			for(int j = i; j < i + k; j++) S[j] = inv(S[j]);
		}
		string result = flag ? "IMPOSSIBLE" : to_string(ans);
		cout << "Case #"<<tt<<": "<< result << endl;
	}
}