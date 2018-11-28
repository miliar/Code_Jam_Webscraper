#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <map>
#include <functional>
#include <cassert>
#include <ctime>
#include <chrono>
using namespace std;
typedef long long ll;
typedef pair<int,int> pr;
#define REP(i,m,n) for (int i=(m); i<(n); ++i)
#define RREP(i,m,n) for (int i=(m)-1; i>=n; --i)

int main()
{
#ifdef MICRO_LOCAL
    freopen("in.put", "r", stdin);
    chrono::time_point<chrono::high_resolution_clock> timer_start, timer_end;
    timer_start = chrono::high_resolution_clock::now();
#endif
/*----------------------------------------------------------------------------*/
    int T, TT; scanf("%d", &T);
    TT = T;
    while (T--) {
        int r, c; scanf("%d%d", &r, &c);
        char cake[30][30] = {"", };
        int minx[26], miny[26];
        int maxx[26], maxy[26];
        fill(minx, minx+26, 30);
        fill(miny, miny+26, 30);
        fill(maxx, maxx+26, -1);
        fill(maxy, maxy+26, -1);
        REP(i,0,r) scanf("%s", cake[i]);
        REP(i,0,r) {
            REP(j,0,c) {
                if (cake[i][j] != '?') {
                    miny[cake[i][j] - 'A'] = min(miny[cake[i][j] - 'A'], i);
                    minx[cake[i][j] - 'A'] = min(minx[cake[i][j] - 'A'], j);
                    maxy[cake[i][j] - 'A'] = max(maxy[cake[i][j] - 'A'], i);
                    maxx[cake[i][j] - 'A'] = max(maxx[cake[i][j] - 'A'], j);
                }
            }
        }

        REP(i,0,26) {
            if (minx[i] != 30) {
                REP(j,miny[i],maxy[i]) {
                    REP(k,minx[i],maxx[i]) {
                        cake[j][k] = i + 'A';
                    }
                }
            }
        }

        REP(i,0,r) {
            REP(j,0,c) {
                if (cake[i][j] != '?') {
                    RREP(k,j,0) {
                        if (cake[i][k] == '?') {
                            cake[i][k] = cake[i][j];
                        } else {
                            break;
                        }
                    }
                    REP(k,j+1,c) {
                        if (cake[i][k] == '?') {
                            cake[i][k] = cake[i][j];
                        } else {
                            break;
                        }
                    }
                }
            }
        }
        REP(j,0,c) {
            REP(i,0,r) {
                if (cake[i][j] != '?') {
                    RREP(k,i,0) {
                        if (cake[k][j] == '?') {
                            cake[k][j] = cake[i][j];
                        } else {
                            break;
                        }
                    }
                    REP(k,i+1,r) {
                        if (cake[k][j] == '?') {
                            cake[k][j] = cake[i][j];
                        } else {
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d:\n", TT-T);
        REP(i,0,r) {
            printf("%s\n", cake[i]);
        }
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
