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

struct node {
	LL L, R;
	node(LL _begin, LL _end) : L(_begin), R(_end) {};
	bool operator < (const node y) const {
		LL n1 = R-L, n2 = y.R - y.L;
		if (n1 == n2) {
			return L < y.L;	
		}
		return n1 < n2;
	}
};

void solve(int kase){
	LL n, k;
	cin >> n >> k;
	priority_queue<node> s;
	s.push(node(1, n));
	for (LL i = 1; i <= k; i++) {
		node x = s.top();
		s.pop();
		LL M = x.L + (x.R - x.L) / 2;
		if (x.L <= M-1) {
			s.push(node(x.L, M-1));	
		}
		if (M+1 <= x.R) {
			s.push(node(M+1, x.R));	
		}
		if (i == k) {
			LL ls = M-x.L, rs = x.R-M;
			cout << "Case #" << kase << ": " << max(ls, rs) << " " << min(ls, rs) << endl;
		}
	}
}

int main(int argc, char *argv[]){
    ios::sync_with_stdio(false);
    std::cin.tie(0);
    if(argc >= 2) {
        freopen(argv[1], "r", stdin);
    }else{
        freopen("C.in", "r", stdin);    
    }
    int kase;
    cin >> kase;
    for(int i=1; i<=kase; i+=1){
        solve(i);    
    }
    return 0;
}
