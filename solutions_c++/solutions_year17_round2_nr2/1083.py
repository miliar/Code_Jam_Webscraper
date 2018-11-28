using namespace std;
#include <bits/stdc++.h>
#define pb push_back
#define um unordered_map
#define us unordered_set
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define all(x) x.begin(),x.end()
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
		int n;
		in >> n;
		bool ok = true;
		vi nums(6);
		REP(i,6)
		{
			int x;
			in >> x;
			nums[i] = x;
			if (x > n/2)
			{
				ok = false;
			}
		}
		if (!ok)
		{
			out << "Case #" << tt+1<< ": IMPOSSIBLE\n";
			continue;
		}
		out << "Case #" << tt+1<< ": ";
		int prev;
		vector<char> c = {'R','A', 'Y','A','B'};
		string s(n,'a');
		if (*max_element(all(nums)) == nums[0])
			prev = 0;
		else if (*max_element(all(nums)) == nums[2])
			prev = 2;
		else
			prev = 4;
		s[0] = c[prev];
		nums[prev]-=1;
		FOR(i,1,n-1)
		{
			if (prev == 0)
			{
				if (*max_element(all(nums)) == nums[2])
					prev = 2;
				else prev = 4;
			}
			else if ( prev == 2)
			{
				if (*max_element(all(nums)) == nums[0])
					prev = 0;
				else prev = 4;
			}
			else {
				if (*max_element(all(nums)) == nums[0])
					prev = 0;
				else prev = 2;
			}
			s[i] = c[prev];
			nums[prev]-=1;
		}
		if (s[n-1] == s[0])
		{
			char t = s[n-1];
			s[n-1] = s[n-2];
			s[n-2] = t;
		}
		out << s << endl;
	}
	in.close();	
	out.close();
}