/* Hav4ik krasav4ik */

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iomanip>

#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)
#define for1(i, n) for (int i = 1; i <= n; i++)
#define forr(i, n) for (int i = n; i-- > 0; )

#define forab(i, a, b) for (int i = a; i < b; i++)
#define forrab(i, a, b) for (int i = b; i-- > a; )

#define all(a) a.begin(), a.end()
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)


typedef unsigned long long int ulli;
typedef long long int lli;
typedef long double lld;

typedef pair<int, int> pii;

int r[1001];
int h[1001];
pii p[1001];
pii d[1001];

void solve_case(int casenum)
{
	int k, n;
	cin >> n >> k;

	forn(i, n){
		cin >> p[i].first >> p[i].second;
	}


	double smax = 0.0;
	sort(p, p+n, [](pii a, pii b){ return a.first > b.first; });
	forn(i, n - k + 1){
		forn(j, n - i){
			d[j] = p[j + i];
		}
		sort(d+1, d+n-i, [](pii a, pii b)
			{ double sa = (2*double(a.first)*M_PI) * a.second;
			  double sb = (2*double(b.first)*M_PI) * b.second;			

			return sa > sb;});
//		forn(j, n-i)
//			cerr << d[j].first << "-" << d[j].second << " ";
	//	int rmax = (*max_element(d, d+k, [](pii a, pii b) 
	//		{return a.first < b.first;})).first;
		double rmax = d[0].first;

		double bases = double(rmax) * double(rmax) * M_PI;
		double sss= .0;
		forn(j, k){
			double ddd = (2 * double(d[j].first) * M_PI) * double(d[j].second);
			sss += ddd;
//			cerr << ddd << endl;
		}
		
		sss += bases;
//		cerr << " : " << k << " " << sss << " --- " << rmax << endl;
		if (sss > smax)
			smax = sss;
	}


	

//	sort(p, p+n, [](pii a, pii b){ return a.first > b.first });



	cout << "Case #" << casenum << ": " << 
		fixed << setprecision(7) << smax << endl;
}

int main() {
	int numof_cases;
	cin >> numof_cases;
	
	for1(casenum, numof_cases)
		solve_case(casenum);

	return 0;
}
