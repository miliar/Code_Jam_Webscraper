#include<bits/stdc++.h>

#define li long int
#define lli long long int
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define sli(n) scanf("%ld",&n)
#define slli(n) scanf("%lld",&n)
#define sf(n) scanf("%f",&n)
#define sstr(s) scanf("%s",s)

const int mod = 10000009;
const lli MOD = 1000000007;

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large-output0.txt","w",stdout);

	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		double D;
		int N;
		cin>>D>>N;
		
		double high_time=-1;
		for(int i=1;i<=N;i++){
			double ki,sp;
			cin>>ki>>sp;
			
			double treq = (D-ki)/sp;
			if(treq > high_time)
				high_time=treq;
		}
		
		double ans = (double) D/high_time;
		cout<<fixed<<"Case #"<<t<<": "<<ans<<"\n";
	}
	
	return 0;
}
