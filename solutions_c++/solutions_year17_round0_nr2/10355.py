#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	bool tidy;
	ll t,n,d;
	string s;
	cin >> t;
	for(int j=1;j<=t;++j){
		tidy=false;
		cin >> n;
		while(!tidy){
			s=to_string(n);
			tidy=true;
			d=s[0]-'0';
			for(int i = 1;i<s.size() && tidy;++i){
				if((s[i]-'0')<d) tidy=false;
				else d=s[i]-'0';
			}
//			cout << n << endl;
			--n;
		}
		printf("Case #%d: %d\n",j,n+1);
	}
}
