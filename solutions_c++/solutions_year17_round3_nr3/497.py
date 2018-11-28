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

ld a[105];
ld eps = 0.0000001;

int main()
{
	freopen("input33.txt", "r", stdin);
	freopen("output33.txt", "w", stdout);
	
	int t;
	cin >> t;
	int initt = t;
	
	while (t--) {
		int n, k;
		ld x;
		
		cin >> n >> k;
		cin >> x;
		
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}		
		
		sort(a, a + n);
		
		a[n] = 10000.0;
		
		while (x > eps) {
			int j = -1;
			for (int i = 1; i <= n; i++) {
				if (abs(a[i] - a[i - 1]) > eps) {
					j = i;
					break;
				}
			}
			
			ld h = a[j] - a[j - 1];
			
			if (h * j < x) {
				for (int i = 0; i < j; i++)
					a[i] = a[j];
				x -= h * j;
			} 
			else {
				for (int i = 0; i < j; i++)
					a[i] += x / j;
				x = 0;
			}
		}
		
		ld ans = 1;
		
		for (int i = 0; i < n; i++) {
			if (a[i] <= 1) ans *= a[i]; 
		}
		
		cout << "Case #" << initt - t << ": ";
		
		cout << fixed << setprecision(10) << ans;
		
		cout << "\n"; 
	}	
    return 0;   
}


