#include<iostream>
#include<cstdio> 
#include<cstring>
#include<string>
#include<cmath>
using namespace std;
const int INF = 1000000;

int T, K;
string S; 

int solve(){
	cin >> S;
	cin >> K;
	int len = S.length();
	int cnt = 0; 
	for(int i = 0; i <= len - K; i ++){
		if(S[i]	== '-'){
			for(int d = 0; d < K; d ++){
				S[i + d] = S[i + d] == '+'? '-' : '+'; 
			}
			cnt += 1; 
		}
	}
	bool right = true; 
	for(int i = len - K; i < len; i++){
		if(S[i] == '-')
			right = false;
	}
	if(right) return cnt; 
	else return -1; 
}

int main(){
	cin >> T; 
	int ans; 	
	for(int i = 0; i < T; i++){
		ans = solve();
		if(ans >= 0)
			cout << "Case #"<< (i+1) << ": " << ans << endl; 
		else 
			cout << "Case #"<< (i+1) << ": " << "IMPOSSIBLE" << endl;
	}
	
	return 0;
}
