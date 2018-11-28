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

void solve(int kase){
	string s;
	cin >> s;
	int n = s.size();
	for (int i = n-1; i >= 1; i--) {
		if (s[i-1] > s[i]) {
			s[i-1] -= 1;
			for(int j = i; j < n; j++) {
				s[j] = '9';
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (s[i] != '0') {
			s = s.substr(i);
			break;
		}
	}
	if (s == "") s = "0";
    cout << "Case #" << kase << ": " << s << endl;
}

int main(int argc, char *argv[]){
    ios::sync_with_stdio(false);
    std::cin.tie(0);
    if(argc >= 2) {
        freopen(argv[1], "r", stdin);
    }else{
        freopen("B.in", "r", stdin);    
    }
    int kase;
    cin >> kase;
    for(int i=1; i<=kase; i+=1){
        solve(i);    
    }
    return 0;
}
