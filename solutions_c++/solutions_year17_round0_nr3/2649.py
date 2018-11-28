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
typedef priority_queue<int> pqi;
typedef priority_queue<lld> pql;
 
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
	
	freopen("in3_3.in","r",stdin);
	freopen("o3_3.txt","w",stdout);
	int tc;
	cin>>tc;
	
	rep(i,1,tc+1)
	{
		lld n,k;
		cin>>n>>k;
		
		map<lld,lld> m;
		m[n]=1;
		pql pq;
		
		pq.push(n);
		
		//vector< pair< lld,pii > vp;
		
		lld j=0;
		while(!pq.empty())
		{
			lld top = pq.top();pq.pop();//dbg(top);
		//dbg(top);	
			if(top%2)
			{
				if(m[top/2]==0)pq.push(top/2);
				m[top/2]+=m[top]*2;
				
				j+=m[top];
				
				//vp.pb(mp(j,mp(top/2,top/2)));
			}
			else
			{
				if(m[top/2]==0)pq.push(top/2);
				if(m[top/2-1]==0)pq.push(top/2-1);
				
				m[top/2]+=m[top];
				m[top/2-1]+=m[top];
				
				j+=m[top];
				
				//vp.pb(mp(j,mp(top/2-1,top/2)));
			}
			
			if(j>=k)
			{
				cout<<"Case #"<<i<<": "<<top/2<<" "<<(top-1)/2<<endl;break;
			}
		}
		
		
	}
	return 0;
		

}
