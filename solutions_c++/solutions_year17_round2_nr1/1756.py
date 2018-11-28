#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS
#include <queue>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <deque>
#include <sstream>
#include <iomanip>
#define sync ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ss second
#define ff first
#define ll long long
#define mp make_pair
#define endl "\n"
#define pb push_back
#define ld long double
#define M_PI 3.14159265358979323846
#define puss vector
const ld EPS = 0.9;
const ll INF = 1000000007;
using namespace std;

int main() 
{
	freopen("in.in", "r", stdin);
	freopen("sol.out", "w", stdout);
	int t;
	cin >> t;
	for (int h = 0; h < t; h++)
	{
		double d;
		int n;
		cin >> d >> n;
		vector<pair<ld, ld> > a(n);
		ld maxt = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i].ff >> a[i].ss;
			a[i].ff = (ld)d - a[i].ff;
			maxt = max(maxt, a[i].ff / a[i].ss);
		}
		printf("Case #%d: %.6f\n", h+1, (double)d/maxt);
	}
	return 0;
}