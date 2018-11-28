#define  _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:256000000")

#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>
#include <deque>
#include <queue>
#include <iomanip>
#include <fstream>
#include <string>
#include <functional> 

#define ll long long 
#define ld long double 
#define fi(n) for(ll i = 0; i < (n); i++)
#define FOR(i, k, n) for(ll i = (k); i < (n); i++)
#define all(a) (a.begin(), a.end())

const int INF = 2147483647;
const int mod = 1e9 + 7;
const long long lINF = 9223372036854775807;

using namespace std;

#define cin in
#define cout out

ifstream in;
ofstream out;

int main()
{
	in.open("A-large.in");
	out.open("output.out");

	int T;
	cin >> T;
	FOR(tc, 1, T + 1)
	{
		int n, m;
		cin >> n >> m;
		vector<string> v(n);
		fi(n)
			cin >> v[i];

		FOR(i, 0, n)
			FOR(j, 1, m)		
				v[i][j] = ((v[i][j] == '?') ? v[i][j - 1] : v[i][j]);
		
		FOR(i, 0, n)
			for(int j = m - 2; j >= 0; j--)
				v[i][j] = ((v[i][j] == '?') ? v[i][j + 1] : v[i][j]);
		
		FOR(j, 0, m)
			FOR(i, 1, n)
				v[i][j] = ((v[i][j] == '?') ? v[i - 1][j] : v[i][j]);
		
		FOR(j, 0, m)
			for(int i = n - 2; i >= 0; i--)
				v[i][j] = ((v[i][j] == '?') ? v[i + 1][j] : v[i][j]);
	
		cout << "Case #" << tc << ": " << endl;
		for (auto e : v)
			cout << e << endl;
	}
	return 0;
}





