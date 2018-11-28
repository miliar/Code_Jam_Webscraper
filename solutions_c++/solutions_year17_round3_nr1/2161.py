/*  chuckie   */
#include <bits/stdc++.h>
#define CHUCKIE

 
#define cint(d) scanf("%d", &d)
#define cint2(a, b) scanf("%d %d", &a, &b)
#define cint3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define cint4(a, b, c, d) scanf("%d %d %d %d", &a, &b, &c, &d)
 
#define clong(d) scanf("%lld", &d)
#define clong2(a, b) scanf("%lld %lld", &a, &b)
#define clong3(a, b, c) scanf("%lld %lld %lld", &a, &b, &c)
#define clong4(a, b, c, d) scanf("%lld %lld %lld %lld", &a, &b, &c, &d)
 
const long long MOD = 1000000007;
#define MODSET(d) if ((d) >= MOD) d %= MOD;
#define MODR(d) ((d)>=MOD?(d)%MOD:(d))
#define MODNEGSET(d) if ((d) < 0) d = ((d % MOD) + MOD) % MOD;
#define MODADDSET(d) if ((d) >= MOD) d -= MOD;
#define MODADDWHILESET(d) while ((d) >= MOD) d -= MOD;
 
#define foreach(it,c) for(__typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++) 
#define MAX 1000000
#define ll long long
#define mp make_pair
#define pb push_back
#define pi acos(-1)
 
using namespace std;

typedef vector<int> vi;
typedef pair<double,int> di;

vector<vector<int> > arr;
double memo[1001][1001];
int rad[1001][1001];
int n,k;

di dp(int idx, int currk )
{
	//cout<<"im in"<<"\n";
	
	if(currk==0) return di(0,0);
	if(idx>=n) return di(0,0);
	
	if(memo[idx][currk]!=-1)return di(memo[idx][currk],rad[idx][currk]);
	
	di p1=dp(idx+1,currk);
	di p2=dp(idx+1,currk-1);
	
	double ans2= p2.first +2*pi*arr[idx][0]*arr[idx][1] + pi*(arr[idx][0]*arr[idx][0] - p2.second*p2.second);
	double ans1= p1.first;
	
	
	memo[idx][currk]=max(ans2,ans1);
	
	if(ans2>ans1)
	rad[idx][currk]=arr[idx][0];
	
	else rad[idx][currk]=p1.second;
	
	return di(memo[idx][currk],rad[idx][currk]);
	
}



int main()
{
	
	#ifdef CHUCKIE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	
	int t;
	cin>>t;
	
	for(int z=0;z<t;z++)
	{
		
		cin>>n>>k;
		arr.clear();
		arr.resize(n+5);
		
		for(int i=0;i<1001;i++)for(int j=0;j<1001;j++)memo[i][j]=-1;
		
		int r,h;
		
		for(int i=0;i<n;i++)
		{
			cin>>r>>h;
			arr[i].pb(r);
			arr[i].pb(h);
		}
		
		sort(arr.begin(),arr.begin()+n);
		reverse(arr.begin(), arr.begin()+n);
		
		double amx=0;
		if(n<=10)
		{
			for(int i=0; i< (1<<n); i++)
			{
				int s=0;
				double prev=0;
				double ans=0;
				for(int j=n-1; j>=0;j--)
				{
					if( (i & (1<<j)) >0)
					{
						s++;
						ans+=pi*(pow(arr[j][0],2) - prev*prev) + 2*pi*arr[j][0]*arr[j][1];
						prev=arr[j][0];
					}
				}
				
				
				if(s==k)amx=max(amx,ans);
				
			}
		}
		
		
		cout<<fixed<<setprecision(10);
		cout<<"Case #"<<z+1<<": "<<amx<<"\n";
		
	}
	
	return 0;
}
