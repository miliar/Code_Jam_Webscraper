//
//  main.cpp
//  B
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

int AC, AJ;
vector<pair<int,int>> Cint, Jint;
int Ctime, Jtime;

void read(void){
//when using vectors or queues, do not forget to clear them!
    Cint.clear(); Jint.clear();
    cin >> AC >> AJ;
    Ctime=720; Jtime=720;
    int C, D;
    FOR(a,0,AC){
        cin >> C >> D;
        Cint.push_back({C,D});
        Ctime -= (D-C);
    }
    FOR(a,0,AJ){
        cin >> C >> D;
        Jint.push_back({C,D});
        Jtime -= (D-C);
    }
    sort(ALL(Cint));
    sort(ALL(Jint));
}

bool overlapWithJ(int begin, int end){
    if(end<begin) return overlapWithJ(begin,1440) || overlapWithJ(0,end);
    FOR(i,0,Jint.size()){
        int b=Jint[i].first, e=Jint[i].second;
        if(e>b){if(b<end && e>begin) return true;}
        else if(end>b || begin<e) return true;
    }
    return false;
}

bool overlapWithC(int begin, int end){
    if(end<begin) return overlapWithC(begin,1440) || overlapWithC(0,end);
    FOR(i,0,Cint.size()){
        int b=Cint[i].first, e=Cint[i].second;
        if(e>b){if(b<end && e>begin) return true;}
        else if(end>b || begin<e) return true;
    }
    return false;
}

void solve(void){
    while(1){
        int min_gap=INF;
        int ind=-1, tmp;
        FOR(i,0,Cint.size()){
            tmp = Cint[(i+1)%(Cint.size())].first-Cint[i].second;
            if(tmp<0) tmp += 1440;
            if(tmp<=Ctime && min_gap>tmp && !overlapWithJ(Cint[i].second, Cint[(i+1)%(Cint.size())].first)){
                min_gap=tmp; ind=i;
            }
        }
        if(min_gap==INF) break;
        Cint[ind].second = Cint[(ind+1)%Cint.size()].second;
        Cint.erase(Cint.begin()+(ind+1)%Cint.size());
        Ctime-=min_gap;
    }
    while(1){
        int min_gap=INF;
        int ind=-1, tmp;
        FOR(i,0,Jint.size()){
            tmp = Jint[(i+1)%(Jint.size())].first-Jint[i].second;
            if(tmp<0) tmp += 1440;
            if(tmp<=Jtime && min_gap>tmp && !overlapWithC(Jint[i].second, Jint[(i+1)%(Jint.size())].first)){
                min_gap=tmp; ind=i;
            }
        }
        if(min_gap==INF) break;
        Jint[ind].second = Jint[(ind+1)%Jint.size()].second;
        Jint.erase(Jint.begin()+(ind+1)%Jint.size());
        Jtime-=min_gap;
    }

    FOR(i,0,Cint.size()){
        cerr << Cint[i].first << " " << Cint[i].second << endl;
    }
    FOR(i,0,Jint.size()){
        cerr << Jint[i].first << " " << Jint[i].second << endl;
    }
    cout << max(Cint.size(),Jint.size())*2 << endl;
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
