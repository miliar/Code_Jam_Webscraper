/*
TASK: C. Bathroom Stalls
LANG: C++
*/
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back((x))
#define FOR(i,st,ed) for(int (i)=(st);(i)<(ed);(i)++)
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long LL;

long long N,M,T;
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("C-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int i,j,k;
	cin >> T;
	long long a,b,c;
	int tt=0;
	while(T--)
	{
	    tt++;
	    cin >> N >> M;
	    priority_queue<pair<long long,long long> > pq;
	    pq.push({N,1});
	    while(true)
        {
            tie(a,b) = pq.top();
            pq.pop();
            while(!pq.empty() && pq.top().X==a)
            {
                b+=pq.top().Y;
                pq.pop();
            }
            M-=b;
            if(M<=0)    break;
            a--;
            if(a%2==0)
                pq.push({a/2,b*2});
            else
            {
                pq.push({a/2+a%2,b});
                pq.push({a/2,b});
            }
        }
        a--;
        b=a/2+a%2;
        c=a/2;
        printf("Case #%d: %lld %lld\n",tt,b,c);
	}
	return 0;
}
