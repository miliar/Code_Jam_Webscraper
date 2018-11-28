#include <bits/stdc++.h>
#define N 10
#define M 18

using namespace std;
typedef long long ll;
int t;
string s;
int k;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin>>t;
	for(int c=1;c<=t;++c) {
		cin>>s;
		int n = s.length();
		ll ans = 0;
		int maximum = 0;
		for(int i=n-2;i>=0;--i) {
			int c1 = s[i]-'0';
			int c2 = s[i+1]-'0';
			if(c1>c2) {
				s[i] = c1-1+'0';
				for(int j=i+1;j<n;++j)
					s[j]='9';
			}
		}
		string final_string="";
		int k = 0;
		for(;k<n;++k) if(s[k]!='0') break;
		for(;k<n;++k) {
			final_string = final_string+s[k];
		}
		cout<<"Case #"<<c<<": "<<final_string<<endl;
	}
	return 0;
}
