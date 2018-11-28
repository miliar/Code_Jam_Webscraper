#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef pair<int,int> pii;
typedef vector<vector<int> > graph;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

const int MAXN = 25;

char s[MAXN];

void solve() {
    int n = strlen(s);
    for(int i = 0; i+1 < n; i++) {
        if(s[i]>s[i+1]) {
            int j = i;
            while(j > 0 && s[j-1]==s[i]) {
                j--;
            }
            s[j]--;
            for(int k = j+1; k < n; k++) {
                s[k] = '9';
            }
            break;
        }
    }
    printf("%s\n", s+(s[0]=='0'));
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T; scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
        printf("Case #%d: ", C);

        scanf("%s", s);
        solve();
	}
}
