#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <fstream>
#include <iomanip>
#include <iso646.h>
#include <stdio.h>
#include <map>
#include <queue>
#include <string.h>

typedef long long LL;
typedef long double LD;

#define sync ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ss second
#define ff first
#define mp make_pair
#define endl "\n"
#define pb push_back
#define FilkinMaksim int main()
#define exit return 0
#define f_in freopen("input.txt", "r", stdin)
#define f_out freopen("output.txt", "w", stdout)
#define file_on f_in; f_out

//const LD M_PI = 3.14159265358979323846;
const LD EPS = 0.0000000001;
const LL INF = 1000000007;

using namespace std;

const int nmax = 10001;

//vector < double > a;

int main() {
	file_on;
	int q;
	cin >> q;
	for (int gi=1; gi<=q; gi++)
	{
		double d,min_t=0;
		int n;
		cin >> d >> n;
		for (int i = 0; i < n; i++)
		{
			double s, v, t;
			cin >> s >> v;
			if (s > d) s = 0;
			else s = d - s;
			t = s / v;
			min_t = max(t, min_t);
		}
		d = d / min_t;
		printf("Case #%d: %.6f\n", gi,d);
	}
}