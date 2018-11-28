#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
int T, k, ans;
string s;
char c = '+' + '-';
int main(){
	ifstream inp;
	inp.open ("a.inp");
	ofstream oup;
	oup.open("a.out");
	inp>>T;
	F(t, T){
		inp>>s>>k;
		int ans = 0;
		f(i, s.size()-k+1){
			if (s[i] == '-'){
				for (int j = i; j<i+k; j++){
					s[j] = c-s[j];
				}
				ans++;
			}
		}
		bool fail = 0;
		f(i, s.size()) if (s[i] == '-') {
			fail = 1;
		}
		oup<<"Case #"<<t<<": ";
		if (fail) oup<<"IMPOSSIBLE"<<endl;
		else oup<<ans<<endl;
	}
}

