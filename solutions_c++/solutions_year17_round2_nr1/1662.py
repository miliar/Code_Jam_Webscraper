//
//  main.cpp
//  A
//
//  Created by Yuto Murashita on 23/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <sys/time.h>

#define INF ((int)1e9)
#define FOR(i,i_m,i_M) for(int i=i_m; i<i_M; i++)

typedef long long ll;

using namespace std;

int D, N;
ll K[1000], S[1000];
double mintime;

void read(void){
    cin >> D >> N;
    mintime = 0.;
    for(int n=0; n<N; n++){
        cin >> K[n] >> S[n];
        mintime = max(mintime, (double)(D-K[n])/S[n]);
    }
}

void solve(void){
    printf("%.6f\n", D/mintime);
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
