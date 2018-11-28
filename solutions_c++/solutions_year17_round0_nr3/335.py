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

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;

    for (int tnum = 0; tnum < tc; tnum++) {
    	long long n, k;
    	cin >> n >> k;

    	map <long long, long long> cnt;
    	cnt[n] = 1;

    	long long amin = -1, amax = -1;
    	while (true) {
    		long long len = cnt.rbegin()->fs;
    		long long c = cnt.rbegin()->sc;
    		assert(len > 0);

    		cnt.erase(--cnt.end());

    		long long lenleft = (len - 1) / 2;
    		long long lenright = len - 1 - lenleft;
    		if (c >= k) {
    			amin = lenleft;
    			amax = lenright;
    			
    			break;
    		}

    		k -= c;
    		cnt[lenleft] += c;
    		cnt[lenright] += c;
    	}

    	cout << "Case #" << tnum + 1 << ": " << amax << ' ' << amin << endl;
    }

    return 0;
}