#include "bits/stdc++.h"
#define MAXN 100009
#define INF 1000000007
#define mp(x,y) make_pair(x,y)
#define all(v) v.begin(),v.end()
#define pb(x) push_back(x)
#define wr cout<<"----------------"<<endl;
#define ppb() pop_back()
#define tr(ii,c) for(typeof((c).begin()) ii=(c).begin();ii!=(c).end();ii++)
#define ff first
#define ss second
#define my_little_dodge 46
using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
template<class T>bool umin(T& a,T b){if(a>b){a=b;return 1;}return 0;}
template<class T>bool umax(T& a,T b){if(a<b){a=b;return 1;}return 0;}
PII arr[MAXN];
int main(){
	cout.precision(10);
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		int n,k;
		scanf("%d%d",&n,&k);
		for(int i=1;i<=n;i++)
			scanf("%d%d",&arr[i].ff,&arr[i].ss);
		sort(arr+1,arr+n+1);	
		vector<long double>now;
		long double ans=0;
		for(int i=1;i<=n;i++){
			if(i>=k){
				long double res=arr[i].ff*1.0*arr[i].ff+2.0*arr[i].ff*1.0*arr[i].ss;
				sort(all(now));
				for(int j=(int)now.size()-1;j>(int)now.size()-k;j--)
					res+=now[j];
				umax(ans,res);	
			}
			now.pb(2.0*arr[i].ff*1.0*arr[i].ss);
		}
		cout<<fixed<<"Case #"<<test<<": "<<ans*acos(-1)<<endl;
	}
	return 0;
}
