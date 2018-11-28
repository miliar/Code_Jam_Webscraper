#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
//#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(i, a, n) for(int i=(a), __ ## i=(n); i<__ ## i; i++)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";REP(__prv,sz(X)-1)cout<<(X)[__prv]<<",";if(sz(X))cout<<*(X).end();cout<<"}"<<endl;}

template<class T> ostream &operator<<(ostream &os, const vector<T> &vec)
{
	os << '{';
	REP(i, sz(vec))
	{
		os << vec[i];
		if (i + 1 != sz(vec))
			os << ',';
	}
	os << '}';
	return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &par)
{
	os << '(' << par.X << ',' << par.Y << ')';
	return os;
}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

int gcd(int x, int y)
{
	return y ? gcd(y, x % y) : abs(x);
}

template<class T> T sqr(T x)
{
	return x * x;
}



int main()
{
	//    if (!freopen("1.in", "r", stdin))
	//    {
	//        cerr << "No input file" << endl;
	//        return 1;
	//    }
	//    if (!freopen("1.out", "w", stdout))
	//    {
	//        cerr << "Error creating output file" << endl;
	//        return 1;
	//    }
	ios::sync_with_stdio(false);


	FILE *f, *g;
	freopen_s(&f, "input.txt", "r", stdin);
	freopen_s(&g, "output.txt", "w", stdout);
	

	int t;
	cin >> t;

	for (int tr = 0; tr < t; tr++) {
		int N, R, G, B, O, V, Y;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		if (R > (Y + B)) {
			cout << "Case #" << tr + 1 << ": ";
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (Y > (R + B)) {
			cout << "Case #" << tr + 1 << ": ";
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (B > (Y + R)) {
			cout << "Case #" << tr + 1 << ": ";
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		vector < pair < int, char> >  mass(3);
		mass[0] = make_pair(R, 'R');
		mass[1] = make_pair(Y, 'Y');
		mass[2] = make_pair(B, 'B');
		sort(mass.begin(), mass.end(), std::greater<pair < int, char > > ());

		string ans = "";

		cout << "Case #" << tr + 1 << ": ";
		while ((mass[0].first+ mass[1].first+mass[2].first) != 0) {
			ans += mass[0].second;
			mass[0].first--;
			if (mass[1].first > 0) {
				ans += mass[1].second;
				mass[1].first--;
			}
			sort(mass.begin(), mass.end(), std::greater<pair < int, char > >());
		}

		bool cyk = true;
		if (ans[0] == ans[N - 1])
			for (int i = 1; i<N-1 && cyk; i++)
				for (int j = i; j < N-1 && cyk; j++)
					if (ans[i - 1] != ans[j + 1] && ans[j]!= ans[0] && ans[i]!= ans[0]) {
						string part = ans.substr(i, j);
						string part1 = ans.substr(0, i);
						string part2 = ans.substr((j + 1), N - 1);
						ans = part1 + part2 + part;
						cyk = false;
						break;
					}
		 cout << ans << endl;
	}

	return 0;
}