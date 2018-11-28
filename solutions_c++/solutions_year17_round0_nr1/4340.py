#include <bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(0);

	int t,tc=0,i,j,k,n,b,e,l,r;
	string s;
	cin >> t;
	while(t--){
		cin >> s >> k;
		cout << "Case #" << ++tc << ": ";
		r=0, n=s.size();
		for(i=0;i<n;){
			if(s[i]=='-'){
				b=i, e=i+k, l=-1;
				if(e<n){
					for(j=b;j<e;++j){
						if(s[j]=='-') s[j]='+';
						else {
							if(l==-1) l=j;
							s[j]='-';
						}
					}
					if(l==-1) l=e;
					i=l;
					++r;
				}else{
					l=0;
					for(j=n-1;j>=n-k;--j)
						l+=(s[j]=='-');
					if(l==k) cout << r+1 << '\n';
					else if(l==0) cout << r << '\n';
					else cout << "IMPOSSIBLE\n";
					break;
				}
			}else {
				++i;
				if(i==n) cout << r << '\n';
			}
		}
	}
	return 0;
}