#include <bits/stdc++.h>
#define MAX 1000005
#define ll long long
#define upperlimit 1000100
#define INF 1e18
#define eps 1e-8
#define endl '\n'
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define MOD 1000000007
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define csl ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
 
ll gcd(ll n1,ll n2){
	if(n1%n2==0)return n2;
	return gcd(n2,n1%n2);
}
ll powmod(ll base,ll exponent)
{
	ll ans=1;
	while(exponent){
		if(exponent&1)ans=(ans*base)%MOD;
		base=(base*base)%MOD;
		exponent/=2;
	}
	return ans;
}
pair <double,double > horse[MAX];
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		double d,n;
		cin>>d>>n;
		for(int i=0;i<n;i++)
			cin>>horse[i].FF>>horse[i].SS;
		sort(horse,horse+(int)n);
		double pos=horse[0].FF,speed=horse[0].SS,time=0.0;
		for(int i=1;i<n;i++)
		{
			if(horse[i].SS>=speed)
			{
				//time+=(d-pos)/speed;
				break;
			}
			double temp=horse[i].SS*pos-speed*horse[i].FF;
			temp/=(horse[i].SS-speed);
			if(temp>d+eps)
			{
				//time+=(d-pos)/speed;
				break;
			}
			else
			{
				time+=(temp-pos)/speed;
				pos=temp;
				speed=horse[i].SS;
			}
			//cout<<i<<" "<<pos<<" "<<speed<<endl;
		}
		time+=(d-pos)/speed;
		cout<<"Case #"<<tt<<": ";
		time=d/time;
		//cout<<time<<endl;
		printf("%0.9llf\n",time);
	}
	//cout<<t<<endl;
	return 0;
}