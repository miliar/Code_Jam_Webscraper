/* Eat a live frog first thing in the morning,
   and nothing worse will happen to you the rest of the day */

/* You can't connect the dots looking forward 
   you can only connect them looking backwards. */

/* Nothing is impossible; impossible itself says "I'm possible" */

#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define ull unsigned long long
#define boost ios_base::sync_with_stdio(false);cin.tie(0);cout.precision(10);cout << fixed;
#define dbset(x) for(int i=0 ; i<x.size(); i++) cerr << x[i] << " "; cerr << endl;
#define inf 1000000007
#define INF 1000000000000000000LL
#define PI 3.14159265358979323846
#define mod 1000000007
#define mod1 1000696969
#define flusz fflush(stdout);
#define VI vector<int>
#define VPI vector < pair<int,int> >
#define PII pair<int, int>
#define BIT bitset<N>
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define eb emplace_back
#define endl '\n'
#define REP(x, y) for(int x = 0; x < (y); ++x)
#define FOR(x, y, z) for(int x = y; x <= (z); ++x)
#define FORR(x, y, z) for(int x = y; x >= (z); --x)
using namespace std;

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)

#define int long long
#define double long double
#define N 107

int test;

int n,q;

int a[N],b[N]; // odleglosc, predkosc

int x,y;

double dp[N];

int dist[N][N];

set <pair<double,int>> s;

void solve()
{
	cin >> n >> q;

	FOR(i,1,n)
	{
		cin >> a[i] >> b[i];
	}

	FOR(i,1,n)
	{
		FOR(j,1,n)
		{
			cin >> dist[i][j];

			if (dist[i][j]==-1)
			{
				dist[i][j]=INF; // pamietaj
			}
		}
	}

	FOR(k,1,n)
	{	
		FOR(i,1,n)
		{
			FOR(j,1,n)
			{
				if (dist[i][j] > dist[i][k]+dist[k][j])
					dist[i][j]=dist[i][k]+dist[k][j];
			}
		}
	}
/*
	FOR(i,1,n)
	{
		FOR(j,1,n)
		{
			cout << dist[i][j] << " ";
		}
		cout<< endl;
	}

	cin >>x  >> y;*/

	FOR(i,1,q)
	{
		cin >> x >> y;

		s.clear();

		FOR(j,1,n)
		{
			dp[j]=INF;
		}

		dp[x]=0;
		s.insert(mp(0,x));

		while(!s.empty())
		{
			auto it1=s.begin();

			auto it=*it1;

			s.erase(it1);

			FOR(j,1,n)
			{
				if ( dist[it.nd][j] <= a[it.nd] && dp[j]>dp[it.nd]+(double)dist[it.nd][j]/b[it.nd])
				{
					auto it2=s.find(mp(dp[j],j));

					if (it2!=s.end())
						s.erase(it2);

					dp[j]=dp[it.nd]+(double)dist[it.nd][j]/b[it.nd];

					s.insert(mp(dp[j],j));
				}
			}
		}

		cout << dp[y] << " ";
	}

	cout << endl;

       return;
}

int32_t main()
{
    boost

    cin >> test;

    FOR(i,1,test)
    {
    	  cout << "Case #" << i <<": ";
         solve();
    }

  return 0;
}
