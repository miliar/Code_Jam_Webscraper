#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

using namespace std;

double shortest_time(int src, int dest, int* D, int* e, int* s, int N){
    int i, j;
    long long this_dist;
    double* shorts; /* Minimal time from src to dest if new horse at i */
    long long* dist_to_end; /* Cumulative distance from i to N-1 */

    if (src != 0 || dest != N-1)
        fprintf(stderr, "src,dest ERROR!\n");

    /* Allocate arrays */
    shorts = (double*) malloc(N * sizeof(double));
    dist_to_end = (long long*) malloc(N * sizeof(long long));
    shorts[N - 1] = 0;
    dist_to_end[N - 1] = 0;

    /* Calculate total distance from city i to end */
    for (i = N - 2; i >= 0; --i){
        if (D[i*N + i + 1] <= 0)
            fprintf(stderr, "D[][] ERROR!\n");
        dist_to_end[i] = D[i*N + i + 1] + dist_to_end[i + 1];
    }

    /* Dynamic! */
    for (i = N-2; i >= 0; --i){
        shorts[i] = -1; /* Default value */
        for (j = N-1; j > i; --j){
            this_dist = dist_to_end[i] - dist_to_end[j];
            if ((e[i] >= this_dist) &&                                     /* If horse is capable to go i, j */
                ((shorts[i] < 0) ||                                        /* And there is no current path to end */
                 (((this_dist / (double) s[i]) + shorts[j]) < shorts[i]))) /* Or i->j, j->dest is better than previous */
                shorts[i] = this_dist / ((double) s[i]) + shorts[j];
        }
    }

    return shorts[0];
}

void solve(){
    int N, Q, i, j;
    int* endurances;
    int* speeds;
    int* distances;
    int* sources;
    int* dests;

    cin >> N;
    cin >> Q;

    /* MALLOC! */
    endurances = (int*) malloc(  N * sizeof(int));
    speeds     = (int*) malloc(  N * sizeof(int));
    distances  = (int*) malloc(N*N * sizeof(int));
    sources    = (int*) malloc(  N * sizeof(int));
    dests      = (int*) malloc(  N * sizeof(int));

    /* Scan speeds and endurances */
    for (i = 0; i < N; ++i){
        scanf(" %d %d", endurances + i, speeds + i);
    }

    /* Scan in distance matrix */
    for (i = 0; i < N; ++i){
        for (j = 0; j < N; ++j){
            scanf(" %d", distances + i*N + j);
        }
    }

    /* Scan in ideal pairs */
    for (i = 0; i < Q; ++i){
        scanf(" %d %d", sources + i, dests + i);
        printf("%.7lf", shortest_time(sources[i]-1, dests[i]-1, distances, endurances, speeds, N));
    }

    free(endurances);
    free(speeds);
    free(distances);
    free(sources);
    free(dests);
}

int main(int argc, char** argv){
    int T, t;

    cin >> T;

    for (t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
