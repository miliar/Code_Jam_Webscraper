#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#include <cassert>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define sz(x) ((int) x.size())
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define eps 1e-9
using namespace std;

typedef long long ll;

int main(void) {
    int n, k, m;
    int i, j, l;
    string s;
    cin >> n;
    fo(i,n) {
	cin >> s >> k;
	int m = s.size(), ans = 0;
	fo(j,(m-k+1)) {
	    if (s[j] == '-') {
		ans++;
		fo(l,k) {
		    if (s[j+l] == '-') s[j+l]='+';
		    else s[j+l] = '-';
		}
	    }
	}
	fo(j,k) {
	    if (s[m-1-j] == '-') {
		ans = -1;
	    }
	}
	cout << "Case #" << i+1 << ": ";
	if (ans == -1) {
	    cout << "IMPOSSIBLE" << endl;
	} else {
	    cout << ans << endl;
	}
    }
}
