#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sz(x) ((int)x.size())
#define clr(a,b) memset(a,b,sizeof(a))
typedef long long ll;
const int maxn=1e3+7;
const int INF=1e9+7;
int n,m,t,d,k[maxn],s[maxn];
int main(){
#ifdef AC
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
#endif
	cin>>t;
	int tcase=1;
	while(t--){
		printf("Case #%d: ",tcase++);
		cin>>d>>n;
		double ti=0;
		for(int i=0;i<n;i++){
			cin>>k[i]>>s[i];
			double tt=(double)(d-k[i])/(double)s[i];
			ti=max(ti,tt);
		}
		printf("%.8f\n",(double)d/ti);
	}
	return 0;
}

