using namespace std;
#include <bits/stdc++.h>
#define pb push_back
#define um unordered_map
#define us unordered_set
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)

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
		ull d;
		int n;
		in >> d >> n;		
		ull k, s;
		double maxspeed = 0, maxtime = 0;
		REP(i,n)
		{
			in >> k >> s;
			double t = (d-k)/(s+0.0);
			if (t > maxtime)
			{
				maxtime = t;
				maxspeed = d / t;
			}
		}
		out << fixed << "Case #" << tt+1 << ": " << maxspeed << endl;
	}
	in.close();	
	out.close();
}