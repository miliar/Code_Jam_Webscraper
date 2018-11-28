
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
    int u=0;
    int v=0;
    int cost=0;
};
class greaterVV {
public:
    bool operator()(const VV& riLeft, const VV& riRight) const {
        //第2条件
        if((riLeft.cost) == (riRight.cost)){
            return riLeft.u < riRight.u;//<:昇順(小さいものから順番)、>:降順(大きいものから順番)
        }
        //第1条件
        return (riLeft.cost) < (riRight.cost);
    }
};


int solve(string N, int K){
    int ret=0;
    int sgn=0;
    bool gen[2000];
    //bool gen[20];
    for(int i=0;i<N.size();i++){
        gen[i]=false;
    }
    for(int i=0;i<N.size();i++){
        if(gen[i]){
            sgn--;
        }
        if(((N.substr(i,1)=="+" && sgn%2==1) || (N.substr(i,1)=="-" && sgn%2==0))){
            if(i+K>N.size()){
                return -1;
            }
            ret++;
            sgn++;
            gen[i+K]=true;
        }
    }

    return ret;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        string S;
        int K;
        ifs >> S >> K;
        
        int ret = solve(S,K);
        if(ret==-1){
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << t << ": " << ret << endl;
        }
        //printf("%.6f\n",ans);
        t++;
    }
    return 0;
}
