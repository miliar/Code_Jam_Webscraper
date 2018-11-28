//SHRESTHA
//IIT INDORE
 
#include <bits/stdc++.h>
using namespace std;
 
#define f 	first
#define s 	second
#define pp 	push
#define pb 	push_back
#define eb	emplace_back
#define pf 	push_front
#define mp 	make_pair
 
typedef long long int 	lld;
typedef long double 	ldb;
typedef vector<int> 	vi;
typedef vector<lld> 	vl;
typedef pair<int,int> 	pii;
typedef pair<lld,lld> 	pll;
typedef map<int,int> 	mii;
typedef map<lld,lld> 	mll;
typedef set<int> 	si;
typedef set<lld> 	sl;
typedef stack<int>	stki;
typedef stack<lld> 	stkl;
typedef vector<pii> 	vii;
typedef vector<pll> 	vll;
 
#define pi(x) 	printf("%d", x)
#define gi(x) 	scanf("%d", &x)
#define gl(x) 	scanf("%lld", &x)
#define pl(x) 	printf("%lld",(lld)x)
#define gc(x)	scanf("%c", &x)
#define pc(x)	printf("%c", x)
#define gs(x)   scanf("%s",&x)
#define ps(x)   printf("%s",x)
#define gd(x)	scanf("%f",&x)
#define gld(x)  scanf("%lf",&x)
#define pd(x)	printf("%f",x)
#define pld(x)  printf("%lf",x)
#define lb 	printf("\n")
#define sp	printf(" ")
 
#define gti(x,y) scanf("%d %d",&x,&y)
#define gtl(x,y) scanf("%lld %lld",&x,&y)
 
#define rep(i,a,b)  for(int i=a;i<b;i++)
#define repd(i,a,b) for(int i=a;i>b;i--)
 
#define all(c) c.begin(),c.end()
#define dbg(x) cerr << #x << " = " << x << endl
 
 
#define INF 1e9
const lld mod = 1e9 + 7;
 
 
#define boost1 ios::sync_with_stdio(false);
#define boost2 cin.tie(0);

int main()
{
	boost1;boost2;
	freopen("in2.in","r",stdin);
	freopen("o4.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int p=1;p<=tc;p++)
	{
		lld n;
		cin>>n;
		
		vector<int> v;
		
		lld g=n;
		int l=0;
		while(g!=0)
		{
			int r=g%10;
			v.pb(r);
			g/=10;l++;
		}
		
		reverse(all(v));
		
		rep(k,0,l)
		rep(i,0,l-1)
		{
			if(v[i]>v[i+1])
			{
				v[i]--;
				v[i+1]=9;
				
				rep(j,i+2,l)v[j]=9;
			}
		}
		
		cout<<"Case #"<<p<<": ";
		for(auto c:v)
		if(c!=0)
		cout<<c;
		
		cout<<endl;
	}
	return 0;
}
