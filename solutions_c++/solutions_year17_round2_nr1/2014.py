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
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
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
		int N;
		double D;
		cin >> D >> N;

		vector <pair<double, double >> H(N);
		vector < double > T(N);
		for (int i = 0; i < N; i++)
			cin >> H[i].first >> H[i].second;

		//H[N] = make_pair(0,100000);

		sort(H.begin(), H.end());

		T[N - 1] = (D - H[N - 1].first) / H[N - 1].second;

		for (int i = N-2; i>=0; i--) {
			double  dist1 = H[i].first;
			double  sp1 = H[i].second;

			dist1 = D - dist1;

			double time = dist1 / sp1;

			if (time < T[i+1]) time = T[i + 1];
			T[i] = time;
		}
		std::cout << std::fixed;
		cout << "Case #" << tr+1 << ": " << std::setprecision(6) << D/T[0] << endl;
	}

	return 0;
}