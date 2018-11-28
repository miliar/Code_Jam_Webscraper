#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

using namespace std;

int n;
double dist[100];
double speed[100];
double l[100][100];
double lastHorseSpeed[100][100];
double lastHorseDist[100][100];
double time[100][100];

int main() {
    int TT, T;
    scanf("%d", &TT);
    
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        int q;
        scanf("%d%d", &n, &q);
        int i, j, k, k2;
        for (i = 0; i < n; i++)
            scanf("%lf%lf", &dist[i], &speed[i]);
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                scanf("%lf", &l[i][j]);
                if (l[i][j] == -1) {
                    time[i][j] = -1;
                } else {
                    if (l[i][j] > dist[i]) {
                        time[i][j] = -1;
                    } else {
                        time[i][j] = l[i][j] / speed[i];
                        lastHorseSpeed[i][j] = speed[i];
                        lastHorseDist[i][j] = dist[i] - l[i][j];
                    }
                }
                
            }
        }
        
        for (k = 0; k < n; k++) {
            for (i = 0; i < n; i++) {
                for (j = 0; j < n; j++) {
                    if (l[i][k] == -1 || l[k][j] == -1)
                        continue;
                    if (l[i][j] == -1 || l[i][k] + l[k][j] < l[i][j])
                        l[i][j] = l[i][k] + l[k][j];
                }    
            }
        }

        for (k2 = 0; k2 < n; k2++) {
            for (k = 0; k < n; k++) {
                for (i = 0; i < n; i++) {
                    for (j = 0; j < n; j++) {
                        int state = 0;
                        double time1 = time[i][k];
                        double time2 = time[k][j];
                        if (time1 == -1)
                            continue;
                        //can existing horse go the distance
                        if (time2 != -1 && (l[k][j] <= lastHorseDist[i][k])) {
                            if (l[k][j] / lastHorseSpeed[i][k] < time2) {
                                time2 = l[k][j] / lastHorseSpeed[i][k];
                                state = 1;
                            }
                        }
                        //what about switching horses?
                        if (l[k][j] <= dist[k]) {
                            if (l[k][j] / speed[k] < time2) {
                                time2 = l[k][j] / speed[k];
                                state = 2;
                            }
                        }
                        if (time2 == -1)
                            continue;
                        if (time[i][j] == -1 || time1 + time2 < time[i][j]) {
                            time[i][j] = time1 + time2;
                            if (state == 0) {
                                lastHorseDist[i][j] = lastHorseDist[k][j];
                                lastHorseSpeed[i][j] = lastHorseSpeed[k][j];
                            }
                            if (state == 1) {
                                lastHorseDist[i][j] = lastHorseDist[i][k] - l[k][j];
                                lastHorseSpeed[i][j] = lastHorseSpeed[i][k];
                            }
                            if (state == 2) {
                                lastHorseDist[i][j] = dist[k] - l[k][j];
                                lastHorseSpeed[i][j] = speed[k];
                            }
                        }
                        //if (k == 0 && j == 3)
                        //    fprintf(stderr, "Going to 4 through 1. state=%d, time1=%f, time2=%f\n", state, time1, time2);
                    }
                }
            }
        }
        
        /*for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            fprintf(stderr, "%4f ", l[i][j]);
        }
        fprintf(stderr, "\n");
        }
        
        for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            fprintf(stderr, "%4f ", time[i][j]);
        }
        fprintf(stderr, "\n");
        }*/
            
        
        for (i = 0; i < q; i++) {
            int s, e;
            scanf("%d%d", &s, &e);
            printf("%.8f ", time[s-1][e-1]);
        }
        printf("\n");
        

    }
}
        