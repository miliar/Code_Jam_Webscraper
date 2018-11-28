
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

int main(){
/*
   freopen("C-small-2-attempt0.in", "r", stdin);
   freopen("out2.txt", "w", stdout);
*/
	int test;
	scanf("%d",&test);
	lli n,k;
	REP(t,test)
	{
		scanf("%lld %lld",&n,&k);
		priority_queue<lli> pq;
		lli cnt=1ll,l,r;
		pq.push(n);
		while(true)
        {
            lli now=pq.top();
            pq.pop();
            l=now/2ll;
            r=(now-1)/2ll;
            if(cnt==k)
                break;
            pq.push(now/2);
            pq.push((now-1)/2);
            cnt++;
        }
        printf("Case #%d: %lld %lld\n",t+1,l,r);
	}
/*
    fclose(stdin);
    fclose(stdout);
*/
    return 0;
}


