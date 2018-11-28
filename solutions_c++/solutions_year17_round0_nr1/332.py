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
    	string s;
    	int k;
    	cin >> s >> k;

    	vector <int> pans;
    	int n = (int) s.size();
    	for (int i = 0; i < n; i++) {
    		pans.pb(s[i] == '-');
    	}

    	bool flag = true;
    	int ans = 0;
    	for (int i = 0; i < n; i++) {
    		if (pans[i]) {
    			if (i + k > n) {
    				flag = false;
    				break;
    			}

    			ans++;
    			for (int j = 0; j < k; j++) {
    				pans[i + j] ^= 1;
    			} 	
    		}
    	}
    
    	cout << "Case #" << tnum + 1 << ": ";
    	if (!flag) {
    		cout << "IMPOSSIBLE" << endl;
    	} else {
    		cout << ans << endl;
    	}
    }



    return 0;
}