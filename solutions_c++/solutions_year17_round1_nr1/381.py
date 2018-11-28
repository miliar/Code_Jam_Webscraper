#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(__typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))
#define SIZE(x) (int)(x).size()

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int R, C;
char s[50][50];

void Solve() {
    cin >> R >> C;
    REP(i, R) {
        scanf("%s", s[i]);
    }
    REP(i, R) {
        REP(j, C) {
            char ch = s[i][j];
            if (ch != '?') {
                for (int k = i; k < R; ++k) {
                    if (s[k][j] == '?' || s[k][j] == ch) {
                        s[k][j] = ch;
                    } else {
                        break;
                    }
                }
                for (int k = i - 1; k >= 0; --k) {
                    if (s[k][j] == '?' || s[k][j] == ch) {
                        s[k][j] = ch;
                    } else {
                        break;
                    }
                }
            }
        }
    }
    REP(i, C - 1) {
        if (s[0][i] != '?' && s[0][i + 1] == '?') {
            REP(j, R) {
                s[j][i + 1] = s[j][i];
            }
        }
    }
    for (int i = C - 1; i > 0; --i) {
        if (s[0][i] != '?' && s[0][i - 1] == '?') {
            REP(j, R) {
                s[j][i - 1] = s[j][i];
            }
        }
    }
    puts("");
    REP(i, R) {
        puts(s[i]);
    }
}

int main() {
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
        cerr << "Case #" << T << ": done!" << endl;
    }
    return 0;
}

