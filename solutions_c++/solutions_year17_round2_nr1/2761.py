#include <iostream>
#include <fstream>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <functional>
#include <string>
#include <cstdio>
#include <cstring>
#include <utility>
#include <queue>
#include <climits>
#include <vector>
#include <iomanip>
#include <algorithm>

#define L(a) (int)((a).size())
#define sqr(x) ((x) * 1ll * (x))
#define vi vector<int>
#define mp make_pair
#define pub push_back
#define pob pop_back
#define ii pair<int, int>
#define vii vector <ii>
#define all(s) (s).begin(),(s).end()
#define fore(i, l ,r) for(int i = (int)l; i < (int)r; i++)
#define TRACE(x) cerr << #x << " : " << x << endl
#define _ << " - " <<

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

const ld EPS = 1e-9;
const ld PI = acos(-1);
const int MOD = (int)1e9 + 7;
const int INF32 = (int)1e9;
const int INF64 = (ll)1e19;

using namespace std;

int main()
{
	int test;
	//ifstream fin("input.in");
	//ofstream fout("output.txt");
	cin >> test;
	fore(tc, 1, test + 1)
	{
		double d;
		int n;
		cin >> d >> n;
		double speed = 1e14;
		fore(i, 0, n)
		{
			double k, s;
			cin >> k >> s;
			if (k >= d)
				continue;
			double t = (d - k) / s;
			speed = min(speed, d / t);
		}
		cout << "Case #" << tc << ": " << fixed << setprecision(6) << speed << endl;
	}
}