/*input
4
-------+ 8
+++++ 4
-+-+- 4
++-++ 2
*/

#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define pb push_back
#define ll long long

int main(){
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios_base::sync_with_stdio(false);cin.tie(0);
	ll t,k,i,j,z,len,ans,f;
	string s;
	cin>>t;
	for(z=1;z<=t;z++){
		cin>>s>>k;
		len=s.size();
		ans=0;f=0;
		for(i=0;i<len-k+1;i++){
			if(s[i]=='-'){
				ans++;
				for(j=i;j<i+k;j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		for(i=0;i<len;i++){
			if(s[i]=='-'){
				f=1;break;
			}
		}
		if(f==0)
			cout<<"Case #"<<z<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<"\n";
	}
	return 0;
}
