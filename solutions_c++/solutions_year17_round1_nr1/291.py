#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iomanip>
#include <map>
#include <cmath>
#include <deque>
using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef pair<ll,ll> l4;
const int maxn = 50010;
const double eps = 1e-8;

int T,R,C;
char ch[30][30];

int main() {
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        printf("Case #%d:\n",tt);
        cin >> R >> C;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cin >> ch[i][j];
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (ch[i][j] != '?') {
                    int cur = j-1;
                    while (cur >= 0 && ch[i][cur] == '?') {
                        ch[i][cur] = ch[i][j];
                        cur--;
                    }
                    cur = j+1;
                    while (cur < C && ch[i][cur] == '?') {
                        ch[i][cur] = ch[i][j];
                        cur++;
                    }
                }
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (ch[i][j] != '?') {
                    int cur = i-1;
                    while (cur >= 0 && ch[cur][j] == '?') {
                        ch[cur][j] = ch[i][j];
                        cur--;
                    }
                    cur = i+1;
                    while (cur < R && ch[cur][j] == '?') {
                        ch[cur][j] = ch[i][j];
                        cur++;
                    }
                }
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cout << ch[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
