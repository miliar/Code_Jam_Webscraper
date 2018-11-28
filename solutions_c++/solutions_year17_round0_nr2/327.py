#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

long long go(long long n, long long cur, int lst) {
	if (cur > n)
		return 1;
	if (n / 10 < cur)
		return cur;
	
	long long ans = 1;
	for (int i = lst; i < 10; i++) {
		ans = max(ans, go(n, cur * 10 + i, i));
	}

	return ans;
}

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	long long n;
    	cin >> n;
    	
    	cout << "Case #" << tnum + 1 << ": " << go(n, 0, 1) << endl;
    }

    return 0;
}