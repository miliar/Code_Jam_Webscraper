
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
    double k=0;
    double s=0;
};

class greaterVV {
public:
    bool operator()(const VV& riLeft, const VV& riRight) const {
        //第2条件
        if((riLeft.k) == (riRight.k)){
            return riLeft.k > riRight.s;//<:昇順(小さいものから順番)、>:降順(大きいものから順番)
        }
        //第1条件
        return (riLeft.k) > (riRight.k);
    }
};


VV v[1000];
double solve(double D, int N){
    sort(v,v+N,greaterVV());
    
    int index=0;
    vector<int> ans;
    ans.clear();
    
    double max=0;
    for(int i=0;i<N;i++){
        double tmp=(D-v[i].k)/v[i].s;
        if(max<tmp){
            max=tmp;
            index=i;
        }
    }
    ans.push_back(index);
    
    int f=0;
    while(f==0){
        f=1;
        max=0;
        for(int i=index+1;i<N;i++){
            double tmp=((D-v[index].k)-v[i].k)/(v[i].s);
            if(max<tmp){
                max=tmp;
                index=i;
                ans.push_back(index);
                f=0;
            }
        }
    }
    double tmpp=(D-v[ans[0]].k)/v[ans[0]].s;
    double min=D/tmpp;
    for(int i=1;i<ans.size();i++){
        tmpp=(v[ans[i-1]].k-v[ans[i]].k)/v[ans[i]].s;
        if(min>v[ans[i-1]].k/tmpp){
            min=v[ans[i-1]].k/tmpp;
        }
    }
    
    return min;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        
        double D;
        int N;
        ifs >> D >> N;
        
        for(int i=0;i<N;i++){
            ifs >> v[i].k >> v[i].s;
        }
        double d=solve(D,N);
        cout << "Case #" << t << ": ";
        printf("%.6f\n",d);
        t++;
    }
    return 0;
}
