
#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i (1<<30)-1

lli memo[1005][1005];
int n,k;
pair<lli,lli> arr[1005];

lli dp(int idx,int cnt)
{
	if(cnt==k)
		return 0;
	if(idx>=n)
		return -inf_i;
	if(memo[idx][cnt]!=-1ll)
		return memo[idx][cnt];
	lli val;
	if(cnt==k-1)
		val=arr[idx].first*arr[idx].first+2ll*arr[idx].first*arr[idx].second;
	else
		val=2ll*arr[idx].first*arr[idx].second;
	return memo[idx][cnt]=max(dp(idx+1,cnt),val+dp(idx+1,cnt+1));
}

int main(){
/*
   freopen("A-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);
*/
	int test;
	scanf("%d",&test);
	REP(t,test)
	{

		scanf("%d %d",&n,&k);
		REP(i,n)
			scanf("%lld %lld",&arr[i].first,&arr[i].second);
		sort(arr,arr+n);
		mset(memo,-1ll);
		printf("Case #%d: %.9lf\n",t+1,PI*dp(0,0));
	}

/*
    fclose(stdin);
    fclose(stdout);
*/
    return 0;
}

