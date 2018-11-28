
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <queue>
using namespace std;

long max(long a,long b){
    return a < b ? b : a;
}
long min(long a,long b){
    return a > b ? b : a;
}

struct VV{
    double r=0;
    double h=0;
    double soku=0;
};

class greaterVV {
public:
    bool operator()(const VV& riLeft, const VV& riRight) const {
        //第2条件
        if((riLeft.r) == (riRight.r)){
            return riLeft.h > riRight.h;//<:昇順(小さいものから順番)、>:降順(大きいものから順番)
        }
        //第1条件
        return (riLeft.r) > (riRight.r);
    }
};


class hterVV {
public:
    bool operator()(const VV& riLeft, const VV& riRight) const {
        //第2条件
        if((riLeft.r) == (riRight.r)){
            return riLeft.r > riRight.r;//<:昇順(小さいものから順番)、>:降順(大きいものから順番)
        }
        //第1条件
        return (riLeft.soku) > (riRight.soku);
    }
};

VV p[1000000];

double solve(int N,int K){
    
    sort(p,p+N,greaterVV());
    double maru_r=p[0].r;
    double maru_h=p[0].h;
    double maru_soku=p[0].soku;
    
    sort(p,p+N,hterVV());
    double ans=0;
    double maxr=0;

    for(int i=0;i<K;i++){
        ans+=p[i].soku;
        if(maxr<p[i].r){
            maxr=p[i].r;
        }
    }
    double tmpans=ans+maxr*maxr*M_PI;
    ans=ans-p[K-1].soku+maru_soku+maru_r*maru_r*M_PI;
    if(tmpans>ans){
        ans=tmpans;
    }
    
    return ans;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        int N,K;
        ifs >> N >> K;
        
        for(int i=0;i<N;i++){
            ifs >> p[i].r >> p[i].h;
            p[i].soku=2*M_PI*p[i].r*p[i].h;
        }
        double ans=solve(N,K);
        cout << "Case #" << t << ": ";
        printf("%.9f\n",ans);
        t++;
    }
    return 0;
}
