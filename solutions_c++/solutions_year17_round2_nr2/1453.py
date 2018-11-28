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

char let[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int a[10];

bool check(string s) {
	for (int i = 0; i < (int)s.size(); i++) {
		if (s[i] == s[(i + 1) % (int)s.size()]) return false;
	}
	return true;
}

int main()
{
	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	
	int t;
	cin >> t;
	int initt = t;
	
	while (t--) {
		int n;
		
		cin >> n;
		for (int i = 0; i < 6; i++)
			cin >> a[i];
		
		int cur = 0;
		if (a[2] > a[0]) cur = 2;
		if (a[4] > a[cur]) cur = 4;
		
		string ans;
		bool f = 1;
		
		ans.pb(let[cur]);
		a[cur]--;
		
		for (int i = 0; i < n - 1; i++) {
			int next = -1;
			for (int j = 0; j < 6; j++) {
				if (j == cur) continue;
				if (a[j] == 0) continue;
				if (next == -1) {
					next = j;
				}
				else {
					if (a[j] > a[next]) next = j;
				}
			}
			
			if (next == -1) {
				f = 0;
				break;
			}
			
			ans.pb(let[next]);
			a[next]--;
			cur = next;
		}
		
		if (!f) {
			cout << "Case #" << initt - t << ": IMPOSSIBLE\n";
			continue;
		}
		
		if (!check(ans)) {
			swap(ans[n - 1], ans[n - 2]);
		}
		
		cout << "Case #" << initt - t << ": ";
		
		if (check(ans)) 
			cout << ans;
		else
			cout << "IMPOSSIBLE";
			
		cout << "\n"; 
	}	
    return 0;   
}


