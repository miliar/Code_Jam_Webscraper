#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define RFOR(i,b,a) for (int i = (b)-1; i >= (a); i--)
#define ITER(it,a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define FILL(a,value) memset(a, value, sizeof(a))

#define SZ(a) (int)a.size()
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double PI = acos(-1.0);
const int INF = 1000 * 1000 * 1000 + 7;
const LL LINF = INF * (LL) INF;

const int MAX = 500500;

int cnt[5];

int n,p;


bool take(int len,int md)
{
	if(len == 0)return md == 0;

	FOR(i,0,p)
	if(cnt[i])
	{
		--cnt[i];
		--n;
		if(take(len-1,(md+i)%p))return true;
		++cnt[i];
		++n;
	}

	return false;
}

void solve()
{
	FILL(cnt,0);
	cin>>n>>p;
	FOR(i,0,n)
	{
		int x;
		cin>>x;
		x%=p;
		++cnt[x];
	}

	int ans = 1;
	while(true)
	{
		bool f = false;
		FOR(k,1,5)
		{
			if(take(k,0)){f=true;break;}
		}
		if(!f)break;

		if(n)ans++;
	}

	cout<<ans<<"\n";
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//ios::sync_with_stdio(0);cin.tie(0);

	int T;
	cin>>T;
	FOR(test,0,T)
	{
		cout<<"Case #"<<test+1<<": ";
	//	cerr<<test<<endl;
		solve();
	}
}
