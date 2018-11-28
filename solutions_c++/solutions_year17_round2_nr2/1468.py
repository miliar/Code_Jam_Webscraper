//
//  main.cpp
//  B
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

int N,R,O,Y,G,B,V;

void read(void){
    cin >> N >> R >> O >> Y >> G >> B >> V;
}

void solve(void){
    string s(N, 'X');
    char max_c, mid_c, min_c; int max_n, mid_n, min_n;
    if(R>=Y && R>=B){
        max_c = 'R'; max_n = R;
        if(Y>=B){mid_c = 'Y'; mid_n = Y; min_c = 'B'; min_n = B;}
        else{mid_c = 'B'; mid_n = B; min_c = 'Y'; min_n = Y;}
    }else if(R<Y && R>=B){
        max_c = 'Y'; max_n =Y; mid_c = 'R'; mid_n = R; min_c = 'B'; min_n=B;
    }else if(R>=Y && R<B){
        max_c = 'B'; max_n = B; mid_c = 'R'; mid_n = R; min_c = 'Y'; min_n=Y;
    }else{
        min_c = 'R'; min_n = R;
        if(Y>=B){max_c='Y'; max_n=Y; mid_c='B'; mid_n=B;}
        else{max_c='B'; max_n=B; mid_c='Y'; mid_n = Y;}
    }
    
    if(max_n>N/2){
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    else{
        for(int n=0; n<max_n; n++){
            s[2*n] = max_c;
        }
        for(int n=max_n; n<(N+1)/2; n++){
            s[2*n] = mid_c;
        }
        for(int n=0; n<mid_n-((N+1)/2-max_n); n++){
            s[2*n+1] = mid_c;
        }
        for(int n=mid_n-((N+1)/2-max_n); n<N/2; n++){
            s[2*n+1] = min_c;
        }
    }
    for(int n=0; n<N; n++){
        cout << s[n];
    }
    cout << endl;
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
