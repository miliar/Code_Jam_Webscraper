#define _ijps 01
#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment(linker, "/STACK:667772160")
#include <iostream>
#include <cmath>
#include <vector>
#include <time.h>
#include <map>
#include <set>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <algorithm>
#include <string>
#include <fstream>
#include <assert.h> 
#include <list>
#include <cstring>
#include <queue>
using namespace std;

#define name ""
#define times clock() * 1.0 / CLOCKS_PER_SEC

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;


struct __isoff {
	__isoff() {
		if (_ijps)
			freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);//, freopen("test.txt", "w", stderr);
			//else freopen(name".in", "r", stdin), freopen(name".out", "w", stdout);
			//ios_bsume::sync_with_stdio(0);
			//srand(time(0));
		srand('C' + 'T' + 'A' + 'C' + 'Y' + 'M' + 'B' + 'A');
	}
	~__isoff() {
		//if(_ijps) cout<<times<<'\n';
	}
} __osafwf;
const ull p1 = 131;
const ull p2 = 129;
const double eps = 1e-8;
const double pi = acos(-1.0);

const int infi = 1e9 + 7;
const ll inf = 1e18 + 7;
const ll dd = 2e5 + 7;

bool ok(string t) {
    for(int i = 1; i < t.size(); i++) {
        if(t[i - 1] > t[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    int test;
    cin >> test;
    for(int ii = 1; ii <= test; ii++) {
        string s, res;
        cin >> s;
        string t = s;
        if(ok(t)) {
            res = t;
        }
        for(int i = (int)s.size() - 1; i >= 0; i--) {
            if(t[i] > '0' && !(i == 0 && t[i] == '1')) {
                t[i]--;
                if(ok(t) && res.empty()) {
                    res = t;
                }
            }
            t[i] = '9';
        }
        if(res.empty()) {
            res = string(s.size() - 1, '9');
        }
        printf("Case #%d: %s\n", ii, res.c_str());
    }

}