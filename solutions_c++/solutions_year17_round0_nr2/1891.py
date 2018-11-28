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

const int MAX = 1010;
VI A;

bool ok()
{
	FOR(i,1,SZ(A))
	{
		if(A[i]<A[i-1])return false;
	}
	return true;
}
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	FOR(tt,0,t)
	{
		string s;
		cin>>s;
		int n =SZ(s);
		A.clear();
		FOR(i,0,SZ(s))
		{
			A.PB( s[i]-'0');
		}

		if(!ok())
		{
			RFOR(i,n,0)
			{
				if(A[i]>0)
				{
					--A[i];
					if(ok())
						break;
				}
				A[i] = 9;
			}
		}
		cout<<"Case #"<<tt+1<<": ";
		reverse(ALL(A));
		while(SZ(A)>1 && A.back()==0)A.pop_back();

		RFOR(i,SZ(A),0)cout<<A[i];
		cout<<"\n";

	}
}
