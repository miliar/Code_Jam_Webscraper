#include <stdio.h>
#include <string.h>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <utility>
#include <queue>
#include <climits>
using namespace std;

#define endl '\n'
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define FORE(i, a, b) for(int i=(a); i<=(b); i++)
typedef pair<int, int> ii;
typedef long long LL;
typedef long double LD;

void filp(string& s, int k, int start) {
	int n = s.size();
	for (int i = start; i < start+k; i++) {
		if (s[i] == '-') {
			s[i] = '+';
		} else {
			s[i] = '-';	
		}
	}
}

void solve(int kase){
	string s;
	int k;
	cin >> s >> k;
	int n = s.size(), res = 0;
	for (int i = 0; i <= n-k; i++) {
		if (s[i] == '-') {
			filp(s, k, i);
			res += 1;
		}
		// cerr << s << endl;
	}
	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			cout << "Case #" << kase << ": " << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << "Case #" << kase << ": " << res << endl;
}

int main(int argc, char *argv[]){
    ios::sync_with_stdio(false);
    std::cin.tie(0);
    if(argc >= 2) {
        freopen(argv[1], "r", stdin);
    }else{
        // freopen("A.in", "r", stdin);    
    }
    int kase;
    cin >> kase;
    for(int i=1; i<=kase; i+=1){
        solve(i); 
    }
    return 0;
}
