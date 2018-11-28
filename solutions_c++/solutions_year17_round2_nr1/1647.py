#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cctype>
#include <cstring>
#include <bitset>
#include <algorithm>
#include <iomanip>

#define ld long double
#define ll long long
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define y0 _y0
#define y1 _y1

using namespace std;

template < typename T > T abs(T x)
{
    return x > 0 ? x : -x;
}

template < typename T > T sqr(T x)
{
    return x * x;
}

int main()
{
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	
	int t;
	cin >> t;
	int initt = t;
	
	while (t--) {
		int n;
		ll d;
		
		cin >> d >> n;
		
		ld tm = 0;
		
		for (int i = 0; i < n; i++) {
			ll di, si;
			cin >> di >> si;
			
			tm = max(tm, (ld)(d - di) / (ld)si);
		}
		
		cout << "Case #" << initt - t << ": ";
		
		cout << fixed << setprecision(10) << (ld)d / tm;
		
		cout << "\n"; 
	}	
    return 0;   
}


