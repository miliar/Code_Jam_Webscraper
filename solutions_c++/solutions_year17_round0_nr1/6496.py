#include<bits/stdc++.h>
#define rep(x,a,b) for(x=a;x<b;x++)
#define SIZE
typedef long long int ll;
using namespace std;
ll i,j,kase,m;

int main(){
	ios::sync_with_stdio(false);
	//cin.tie(0);
	ll t;
	cin>>t;
	for(kase=1;kase<=t;kase++){
		string s;
		cin>>s;
		ll k;
		cin>>k;
		ll n=s.length();
		ll ans=0;
		for(i=0;i<=n-k;i++){
			if(s[i]=='-'){
				ans++;
				for(j=i;j<i+k;j++){
					if(s[j]=='-')
						s[j]='+';
					else if(s[j]=='+')
						s[j]='-';

				}
			}	
		}
		bool flag=true;
		for(i=0;i<n;i++){
			if(s[i]=='-'){
				flag=false;
				break;
			}	
		}
		cout<<"Case #"<<kase<<": ";
		if(flag){
			cout<<ans;
		}
		else{
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;
	}
	return 0;
}

