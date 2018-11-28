#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<utility>
#include<set>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<cctype>


#define pb push_back
#define mp make_pair
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define ren(i,a,b) for(int i=a;i>=b;i--)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define pii pair<int,int>
#define vll vector<long long int>
#define vii vector<int>
#define gi(n) scanf("%d",&n)
#define gll(n) scanf("%lld",&n)
#define gstr(n) scanf("%s",n)
#define gl(n) cin >> n
#define oi(n) printf("%d",n)
#define oll(n) printf("%lld",n)
#define ostr(n) printf("%s",n)
#define ol(n) cout << n
#define os cout<<" "
#define on cout<<"\n"
#define o2(a,b) cout<<a<<" "<<b
#define all(n) n.begin(),n.end()
#define present(s,x) (s.find(x) != s.end())
#define cpresent(s,x) (find(all(s),x) != s.end())
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef vector<vector<ll> > mat;

int dp[2][2][1505][1505],mx=1e8+7;

int main()
{ios_base::sync_with_stdio(false);
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,t1=0;
gl(t);
while(t--)
{
	t1++;
	ol("Case #");ol(t1);ol(": ");
	int pos[25*100];
	int n,m;
	cin>>n>>m;
	rep(i,0,(25*100)-1)pos[i]=-1;
	rep(i,0,1504)rep(j,0,1504)dp[0][0][i][j]=dp[0][1][i][j]=dp[1][0][i][j]=dp[1][1][i][j]=mx;
	rep(i,0,n-1)
	{
		int a,b;
		cin>>a>>b;
		rep(j,a,b-1)pos[j]=0;
	}
	rep(i,0,m-1)
	{
		int a,b;
		cin>>a>>b;
		rep(j,a,b-1)pos[j]=1;
	}
	if(pos[0]!=0)dp[0][0][0][1]=1;
	if(pos[0]!=1)dp[1][1][0][0]=1;
	int tot=24*60;
	rep(i,1,(24*60)-1)
	{
		if(pos[i]!=1)
		dp[0][1][i][0]=min(dp[0][1][i][0],min(dp[0][1][i-1][0],1+dp[0][0][i-1][0])),dp[1][1][i][0]=min(dp[1][1][i][0],min(dp[1][1][i-1][0],1+dp[1][0][i-1][0]));
		rep(j,1,(24*60))
		{
			if(pos[i]!=0)
			dp[0][0][i][j]=min(dp[0][0][i][j],min(1+dp[0][1][i-1][j-1],dp[0][0][i-1][j-1])),dp[1][0][i][j]=min(dp[1][0][i][j],min(1+dp[1][1][i-1][j-1],dp[1][0][i-1][j-1]));
			if(pos[i]!=1)
			dp[0][1][i][j]=min(dp[0][1][i][j],min(1+dp[0][0][i-1][j],dp[0][1][i-1][j])),dp[1][1][i][j]=min(dp[1][1][i][j],min(1+dp[1][0][i-1][j],dp[1][1][i-1][j]));
		}
	}
	//ol(dp[1][1259][tot/2]);on;
	/*rep(i,0,9)
	{
		rep(j,0,i+1)
		{
			o2(i,j);os;o2(dp[0][i][j],dp[1][i][j]);on;
		}
	}*/
	/*rep(i,0,tot-1)
	{
		if(pos[i]==0)
		{
			ol(i);on;
		}
	}*/
	int ans=min(dp[0][0][tot-1][tot/2]-1,dp[0][1][tot-1][tot/2]);
	ans=min(ans,min(dp[1][0][tot-1][tot/2],dp[1][1][tot-1][tot/2]-1));
	ol(ans);on;
}
return 0;
}


