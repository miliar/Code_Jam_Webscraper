//
//  main.cpp
//  A
//
//  Created by Yuto Murashita on 13/05/2017.
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

#define FOR(i,m,M) for(int i=m; i<M; i++)
#define ALL(v) v.begin(),v.end()

typedef long long ll;

using namespace std;

int N, P;
int C[4];

void read(void){
//when using vectors or queues, do not forget to clear them!
    cin >> N >> P;
    FOR(i,0,4) C[i]=0;
    FOR(n,0,N){
        int tmp;
        cin >> tmp;
        C[tmp%P]++;
    }
}

void solve(void){
    if(P==2){
        cout << C[0] + (C[1]+1)/2 << endl;;
    }else if(P==3){
        int min, max;
        if(C[1]<C[2]){min=C[1];max=C[2];}
        else{min=C[2];max=C[1];}
        cout << C[0] + min + (max-min + 2)/3 << endl;
    }else if(P==4){
        int min, max;
        if(C[1]<C[3]){min=C[1];max=C[3];}
        else{min=C[3];max=C[1];}
        if(C[2]%2==0) cout << C[0] + C[2]/2 + min + (max-min+3)/4 << endl;
        else cout << C[0] + C[2]/2 + min + 1 + (max-min+1)/4 << endl;
    }else exit(1);
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
