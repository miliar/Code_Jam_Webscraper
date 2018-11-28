#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <random>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define tget(X,id) get<id>(X)

#define MAXN 105

string FILE_IN, FILE_OUT;
int N, Q;
ll D[MAXN][MAXN];
double T[MAXN][MAXN];
int TP[MAXN][MAXN];
int E[MAXN], S[MAXN];

// int VIS[MAXN];
void ride(int s){
    // memset(VIS,0,sizeof VIS);
    // priority_queue<pair<double, int> > pq;
    // pq.push(mp(0, s));
    // VIS[s] = 1;
    T[s][s] = 0;
    for (int i = 0; i < N; i++)
        if (D[s][i] <= E[s]){
            T[s][i] = D[s][i]/double(S[s]);
            // pq.push(mp(-T[s][i], i));
        }
    // while (!pq.empty()){
    //     auto x = pq.top(); pq.pop();
    //     if (-x.ff > T[s][x.ss]+0.00001) continue;
    //     for (int i = 0; i < N; i++)
    //         if (D[s][i] <= E[s] && T[s][x.ss]+D[x.ss][i]/double(S[s]) < T[s][i]){
    //             T[s][i] = T[s][x.ss]+D[x.ss][i]/double(S[s]);
    //             pq.push(mp(-T[s][i], i));
    //         }
    // }
}
double DIS[MAXN];
int main(int argc, char *argv[]){
    if (argc == 1){
        cerr<<"No input specified, using C.in"<<endl;
        FILE_IN = "C.in";
        FILE_OUT = "C.out";
    } else {
        FILE_IN = string(argv[1]);
        FILE_OUT = FILE_IN + ".out";
    }
    freopen(FILE_IN.c_str(),"r",stdin);
    freopen(FILE_OUT.c_str(),"w",stdout);
    
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++){
        scanf("%d%d", &N, &Q);
        for (int i = 0; i < N; i++)
            scanf("%d%d", &E[i], &S[i]);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++){
                scanf("%lld", &D[i][j]), T[i][j] = 1e60;
                if (i == j) D[i][j] = 0;
                if (D[i][j] == -1) D[i][j] = 1LL<<60;
            }
        for (int k = 0; k < N; k++)
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    D[i][j] = min(D[i][j], D[i][k]+D[k][j]);

        // for (int i = 0; i < N; i++, cout<<endl)
        //     for (int j = 0; j < N; j++)
        //         cout<<D[i][j]<<"\t";

        for (int i = 0; i < N; i++)
            ride(i);
        // for (int k = 0; k < N; k++)
        //     for (int i = 0; i < N; i++)
        //         for (int j = 0; j < N; j++)
        //             T[i][j] = min(T[i][j], T[i][k]+T[k][j]);
        
        // for (int i = 0; i < N; i++, cout<<endl)
        //     for (int j = 0; j < N; j++)
        //         cout<<T[i][j]<<"\t";

        printf("Case #%d:", _t);
        int PP[MAXN];
        int U, V;
        for (int i = 0; i < Q; i++){
            scanf("%d%d", &U, &V);
            U--, V--;
            for (int i = 0; i < N; i++) DIS[i] = 1e60;

            priority_queue<pair<double, int> > pq;
            pq.push(mp(0, U));
            DIS[U] = 0;
            // PP[U] = -1;
            while (!pq.empty()){
                auto x = pq.top(); pq.pop();
                x.ff = -x.ff;
                if (x.ss == V) break;
                if (x.ff > DIS[x.ss]+0.00001) continue;
                for (int i = 0; i < N; i++)
                    if (DIS[i] > DIS[x.ss] + T[x.ss][i]){
                        DIS[i] = DIS[x.ss]+T[x.ss][i];
                        // PP[i] = x.ss;
                        pq.push(mp(-DIS[i], i));
                    }

            }
            // int a = V;
            // while (a != -1){
            //     cout<<a<<",";
            //     a = PP[a];
            // }
            printf(" %lf", DIS[V]);
            // cout<<endl;
        }
        printf("\n");
    }
    return 0;
}
