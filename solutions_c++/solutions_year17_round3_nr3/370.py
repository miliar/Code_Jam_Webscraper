//
//  main.cpp
//  C
//
//  Created by Yuto Murashita on 30/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <math.h>
#include <sys/time.h>

#define INF ((int)1e9)
#define INFLL ((long long)1e18)
#define MOD (1000000007LL)
#define EPS ((double)1e-10)

#define FOR(i,m,M) for(int i=m; i<M; i++)
#define ALL(v) v.begin(),v.end()

typedef long long ll;

using namespace std;

int N, K;
double U;
vector<double> P;

void read(void){
//when using vectors or queues, do not forget to clear them!
    P.clear();
    cin >> N >> K;
    cin >> U;
    double p;
    FOR(n,0,N){
        cin >> p;
        P.push_back(p);
    }
    sort(ALL(P));
}

void solve(void){
    FOR(n,0,N){
        if(n==N-1){
            FOR(m,0,N){
                P[m] += U/N;
            }
            break;
        }
        if(U>(P[n+1]-P[0])*(n+1)){
            U -= (P[n+1]-P[0])*(n+1);
            FOR(m,0,n+1){
                P[m]=P[n+1];
            }
        }else{
            FOR(m,0,n+1){
                P[m] += U/(n+1);
            }
            break;
        }
    }
    double res=1.;
    FOR(n,0,N){
        res *= P[n];
    }
    printf("%.10f\n", res);
}

int main(int argc, const char * argv[]) {
    struct timeval start, end, tstart, tend;

    int T;
    cin >> T;

    gettimeofday(&tstart, NULL);

    for(int t=1; t<=T; t++){
    	gettimeofday(&start, NULL);

    	cout << "Case #" << t << ": ";
    	read();
    	solve();

    	gettimeofday(&end, NULL);	
    	cerr << "Case #" << t << ": " << (end.tv_sec-start.tv_sec)*1000+(end.tv_usec-start.tv_usec)/1000. << " ms" << endl;
    }

    gettimeofday(&tend, NULL);
    cerr << "*Total time: " << (tend.tv_sec-tstart.tv_sec)*1000+(tend.tv_usec-tstart.tv_usec)/1000. << " ms" << endl;

    return 0;
}
