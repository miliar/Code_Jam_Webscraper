#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
string S;
int K;
void flip(int ind){
	for (int i = ind; i < ind + K; i++){
		if (S[i] == '-') S[i] = '+';
		else S[i] = '-';
	}
}
bool check(){
	for (int i = 0; i < S.size(); i++){
		if (S[i] == '-') return false;
	}
	return true;
}
int main(){
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		if (t != 0) cout << endl;
		cin >> S >> K;
		int ans = 0;
		for (int i = 0; i <= S.size() - K; i++){
			if (S[i] == '-'){
				flip(i);
				ans++;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if (check()) cout << ans;
		else cout << "IMPOSSIBLE";
	}
	int de;
	cin >> de;
}
