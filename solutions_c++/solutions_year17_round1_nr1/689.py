#include <bits/stdc++.h>
using namespace std;
typedef long long				ll;
typedef pair<int,int >			pii;
#define V						vector
#define SYNC					ios_base::sync_with_stdio(0);cin.tie(0);
#define rep(i,b)				for(int i=0;i<b;i++)
#define repn(i,n)				for(int i=1;i<=n;i++)
#define ALL(x)					(x).begin(),(x).end()
#define fi						first
#define se						second
#define pb						push_back
#define dzx						cerr<<"here";
const ll MOD=1e9+7,INF=9e18;
const int inf=2e8;
/* cent π */
int main(){SYNC
	int T;
	cin>>T;
	repn(tc,T){
		cout<<"Case #"<<tc<<":\n";
		int r,c;
		cin>>r>>c;
		string s[r];
		
		for(int i=0;i<r;i++){
			cin>>s[i];
		}
		int le=0;
		bool f=false;
		for(int i=0;i<r;i++){
			f=false;
			int last=0;
			for(int j=0;j<c;j++){
				if(s[i][j]!='?'){
					f=true;
					for(int k=last;k<=j;k++){
						for(int l=0;l<=le;l++){
							s[i-l][k]=s[i][j];
						}
					}
					last=j+1;
				}
			}
			if(f){
				for(int k=last;k<c;k++){
					for(int l=0;l<=le;l++){
						s[i-l][k]=s[i][last-1];
					}
				}
			}
			if(!f)
				le++;
			else
				le=0;
		}
		for(int k=r-le;k<r;k++){
			for(int j=0;j<c;j++){
				s[k][j]=s[r-le-1][j];
			}
		}
		for(int i=0;i<r;i++){
			cout<<s[i]<<"\n";
		}
	}
	return 0;
}