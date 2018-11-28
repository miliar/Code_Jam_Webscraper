
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


string solve(string N){
    
    int f=1;
    while(f){
        string s=N.substr(0,1);
        string ret="";
        string hiku="1";
        for(int i=0;i<N.size();i++){
            if(atoi(s.c_str())<=atoi(N.substr(i,1).c_str()) && hiku.size()==1){
                ret+=N.substr(i,1);
                s=N.substr(i,1);
            }else{
                hiku+="0";
                ret+="9";
            }
        }
        
        stringstream ss;
        long long h;
        ss << hiku;
        ss >> h;
        if(h==1){
            h=0;
            f=0;
        }
        
        stringstream sss;
        long long r;
        sss << ret;
        sss >> r;
        
        stringstream ssss;
        ssss << r-h;
        N=ssss.str();
    }
    
    return N;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        string N;
        ifs >> N;
        
        string ret = solve(N);
        
        cout << "Case #" << t << ": " << ret << endl;
        //printf("%.6f\n",ans);
        t++;
    }
    return 0;
}
