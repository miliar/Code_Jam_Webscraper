//
//  main.cpp
//  A
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

#define FOR(i,m,M) for(int i=m; i<M; i++)
#define ALL(v) v.begin(),v.end()

typedef long long ll;

using namespace std;

int N, K;
ll R[1000], H[1000];
pair<ll,ll> cakes[1000];

void read(void){
//when using vectors or queues, do not forget to clear them!
    cin >> N >> K;
    FOR(n,0,N){
        cin >> R[n] >> H[n];
        cakes[n] = {R[n],H[n]};
    }
    sort(cakes, cakes+N, greater<pair<ll,ll>>());
}

ll max(int i){
    ll maxR = cakes[i].first, maxL = cakes[i].second;
    ll ret = maxR*maxR + 2*maxR*maxL;
    priority_queue<ll> pq;
    FOR(j,i+1,N){
        ll r=cakes[j].first, h=cakes[j].second;
        pq.push(2*r*h);
    }
    FOR(k,0,K-1){
        ret += pq.top(); pq.pop();
    }
    return ret;
}

void solve(void){
    ll res = 0;
    FOR(n,0,N-K+1){
        ll tmp;
        if(res<(tmp=max(n))) res=tmp;
    }
    printf("%.10Lf\n", res*3.1415926535897932384626433832795029L);
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
