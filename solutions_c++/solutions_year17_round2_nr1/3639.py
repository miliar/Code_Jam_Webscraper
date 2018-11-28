// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug = true;
const double EPS = 1e-9;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector < int >VI;
typedef vector < string > VS;
typedef vector < VI > VVI;
typedef pair < int, int >PII;
typedef pair < int, PII > PIII;

int main()
{
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; ++t) {
	LL d, n;

	cin >> d >> n;

	LL k[n], s[n];


	for (int i = 0; i < n; ++i) {
	    cin >> k[i] >> s[i];
	}

        double t_res =  0;

        for (int i = 0; i < n; ++i) {

		double t_i =
		    ((double) d - (double) k[i]) / ((double) s[i]);


		if (t_res < t_i - EPS) {
                    t_res = t_i;
		}

	}

	cout << "Case #" << t << ": ";

        printf("%.7f", ((double) d / t_res));

        cout << "\n";
    }
    return 0;
}
