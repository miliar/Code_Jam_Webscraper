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


int main() {
    int test;
    cin >> test;
    for(int ii = 0; ii < test; ii++) {
        string s;
        int n;
        cin >> s >> n;
        bool ok = true;
        int res = 0;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '-') {
                res++;
                for(int j = 0; j < n; j++) {
                    if(i + j >= s.size()) {
                        ok = false;
                        break;
                    }
                    s[i + j] = s[i + j] == '+' ? '-' : '+';
                }
            }
        }
        if(ok) {
            printf("Case #%d: %d\n", ii + 1, res);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", ii + 1);
        }
    }

}