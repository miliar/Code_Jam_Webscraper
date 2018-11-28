#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
typedef pair<int, int>          pii;
#define V			 vector
#define SYNC		 ios_base::sync_with_stdio(0);cin.tie(0); 
#define rep(i,b)     for(int i=0;i<b;i++)
#define repn(i,n) 	 for(int i=1;i<=n;i++)
#define ALL(x)  	 (x).begin(), (x).end()
#define fi           first
#define se           second
#define pb 		     push_back
#define dzx 		 cerr<<"here";
const ll MOD=1e9+7,INF=1e18;
const int inf=1e8;
/* cent π */
int main(){SYNC
	int T;
	cin>>T;
	repn(tc,T){
		cout<<"Case #"<<tc<<": ";
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=0;
		for(int i=0;i<s.size();i++){
			if(s[i]=='-'){
				ans++;
				if(i+k > s.size()){
					ans=-1;
					break;
				}
				for(int j=i;j<i+k;j++){
					if(s[j]=='-'){
						s[j]='+';
					}
					else
						s[j]='-';
				}
			}
		}
		if(ans==-1){
			cout<<"IMPOSSIBLE";
		}
		else
			cout<<ans;
		cout<<"\n";
	}
	return 0;
}