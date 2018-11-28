#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define RFOR(i,b,a) for (int i = (b)-1; i >= (a); --i)
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
const LL LINF = 1LL * INF * INF;

map<LL,LL> m;

const int MAX = 1010;
bool A[MAX];
int L[MAX];
int R[MAX];

pair<LL,LL> solve(LL n,LL k)
{
	m.clear();
	m[n] = 1;
	while(true)
	{
		LL val = m.rbegin()->first-1;
		LL cnt = m.rbegin()->second;
		m.erase(val+1);
		LL mn = val/2;
		LL mx = val-mn;
	//	cerr<<val<<" "<<mn<<" "<<mx<<endl;
		if(cnt>=k)
		{
			return MP(mx,mn);
		}else
		{
			k -= cnt;
			m[mn]+=cnt;
			m[mx]+=cnt;
		}
	}
	throw;
}

PII brut(int n,int k)
{
	FILL(A,0);
	PII lst;
	FOR(it,0,k)
	{
		int pr = -1;
		FOR(i,0,n)
		{
			L[i] = pr;
			if(A[i])pr=i;
		}
		pr = n;
		RFOR(i,n,0)
		{
			R[i] = pr;
			if(A[i])pr=i;
		}

		PII bst=MP(-1,-1);
		int x;
		FOR(i,0,n)
		{
			if(A[i])continue;
			int dr=R[i]-i-1;
			int dl = i-L[i]-1;
			PII cur = MP(min(dr,dl),max(dr,dl));
			if(cur>bst)
			{
				bst = cur;
				x=i;
			}
		}

		lst = bst;
		A[x] = 1;
	}

	return lst;
}
int main()
{
	freopen("C.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	FOR(tt,0,t)
	{
		LL n,k;
		cin>>n>>k;

	//	PII br = brut(n,k);

//		swap(br.first,br.second);
		pair<LL,LL> s = solve(n,k);
/*
		if(s!=br)
		{
			cerr<<n<<" "<<k<<endl;
			cerr<<br.first<<" "<<br.second<<endl;
			cerr<<s.first<<" "<<s.second<<endl;
			throw;
		}
*/

		cout<<"Case #"<<tt+1<<": ";

		cout<<s.first<<" "<<s.second;
		cout<<"\n";

	}
}
