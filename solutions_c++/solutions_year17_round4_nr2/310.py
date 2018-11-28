//
//  main.cpp
//  B
//
//  Created by Yuto Murashita on 13/05/2017.
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

#define FOR(i,m,M) for(int i=m; i<M; i++)
#define ALL(v) v.begin(),v.end()

typedef long long ll;

using namespace std;

int N, C, M;
vector<int> pos[1000];
vector<int> cust[1000];

void read(void){
//when using vectors or queues, do not forget to clear them!
    cin >> N >> C >> M;
    FOR(c,0,C) pos[c].clear();
    FOR(n,0,N) cust[n].clear();
    FOR(m,0,M){
        int P, B;
        cin >> P >> B;
        P--;B--;
        pos[B].push_back(P);
        cust[P].push_back(B);
    }
}

bool possible(int r){
    FOR(c,0,C){
        //cerr << c << ": " << pos[c].size() << endl;
        if(pos[c].size()>r) return false;
    }
    int sum=0;
    FOR(p,0,N){
        sum+=(int)cust[p].size();
        //cerr << p << ": " << sum << endl;
        if(sum>(p+1)*r) return false;
    }
    return true;
}

int findMinRides(void){
    int res=-1;
    FOR(r,1,1001){
        if(possible(r)){
            res=r;
            break;
        }
    }
    return res;
}

void solve(void){
    int min=findMinRides();
    cout << min << " ";
    int res=0;
    FOR(p,0,N){
        int tmp;
        tmp=(int)cust[p].size()-min;
        if(tmp>0) res+=tmp;
    }
    cout << res << endl;
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
