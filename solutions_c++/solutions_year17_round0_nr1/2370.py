#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int T, K;

string s0, s1, s2;

int solve(string s){
	int n = s.size(), d, ans=0;
	d = n-K+1;
	for(int i=0; i<d; i++){
		if(s[i]=='-'){
			ans++;
			for(int j=0; j<K; j++){
				if(s[i+j]=='-') s[i+j] = '+';
				else s[i+j] = '-';
			}
		}
	}
	for(int i=0; i<n; i++) if(s[i]=='-') ans=-1;
	return ans;
}

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> s0 >> K;
		s1 = s0;
		s2 = s0;
		reverse(s2.begin(), s2.end());
		int a = solve(s1);
		if(a<0) a = solve(s2);
		else a = min(a, solve(s2));
		cout << "Case #" << t << ": ";
		if(a<0) cout << "IMPOSSIBLE";
		else cout << a;
		cout << "\n";
	}
	return 0;
}
