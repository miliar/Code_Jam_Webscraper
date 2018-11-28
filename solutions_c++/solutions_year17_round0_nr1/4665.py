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
	string pancake;
	int flip_size;
	cin >> pancake >> flip_size;

	int total_flips = 0;

	for (int i = 0; i + flip_size <= SZ(pancake); ++i) {
	    if (pancake[i] != '+') {
		++total_flips;
		for (int j = 0; j < flip_size; ++j) {
		    pancake[i + j] = (pancake[i + j] == '+' ? '-' : '+');
		}
	    }
	}

	bool happy = true;
	for (int i = 0; i < SZ(pancake) && happy; ++i) {
	    if (pancake[i] != '+')
		happy = false;
	}

	cout << "Case #" << t << ": ";

	if (happy) {
	    cout << total_flips;
	} else {
	    cout << "IMPOSSIBLE";
	}
	cout << "\n";
    }
    return 0;
}
