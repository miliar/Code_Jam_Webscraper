using namespace std;
#include <bits/stdc++.h>
#define pb push_back
#define um unordered_map
#define us unordered_set
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline int two(int n) { return 1 << n; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ull> vull;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const char* file = "data.in";

int main()
{
	ifstream in;
	in.open(file);
	ofstream out;
	out.open("data.out");
	
	int t;
	in >> t;
	
	REP(tt,t)
	{
		int n, q;
		in >> n >> q;
		vector<vector<int>> dist(n);
		vpii horses(n);
		vector<double> dp(n,0);
		vector<ull> distij(n,0);
		REP(i,n)
		{
			dist[i].resize(n);
		}
		REP(i,n)
		{
			in >> horses[i].first >> horses[i].second;
		}
		REP(i,n*n){
			in >> dist[i/n][i%n];
		}
		ull sum = dist[0][1];
		for (int i=1;i<n;++i)
			{
				distij[i] = sum;
				if (i == n-1) break;
				sum += dist[i][i+1];
			}
		int start,end;
		in >> start >> end;
		for (int i=1;i<n;++i)
		{
			double min = numeric_limits<double>::max();
			for (int j=0;j < i;++j)
			{
				ull distt = distij[i] - distij[j];
				double time;
				if (horses[j].first >= distt)
					time = dp[j] + (distt / (horses[j].second + 0.0));
				else continue;
				if (time < min)
					min = time;
			}
			dp[i] = min;
		}
		out << fixed << "Case #" << tt + 1 << ": " << dp[n-1] << endl;
	}
	in.close();	
	out.close();
}