
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

struct PP{
    long long rmax;
    long long rmin;
};

PP solve(long long N, long long K){
    int index=0;
    long long tmp=1;
    while(tmp<=K){
        tmp*=2;
        index++;
    }

    PP ans;
    ans.rmax=0;
    ans.rmin=1000;

    vector<long long>a[1000];
    for(int i=0;i<1000;i++){
        a[i].clear();
    }
    a[0].push_back(N);
    for(int i=0;i<index-1;i++){
        for(int j=0;j<a[i].size();j++){
            if(a[i][j]%2==0){
                a[i+1].push_back(a[i][j]/2-1);
                a[i+1].push_back(a[i][j]/2);
            }else{
                a[i+1].push_back(a[i][j]/2);
                a[i+1].push_back(a[i][j]/2);
            }
        }
    }
    
    sort(a[index-1].begin(),a[index-1].end(),greater<long long>());
    int i=pow(2,index-1);
    int j=0;
    while(i!=K){
        if(a[index-1][j]%2==0){
            a[index].push_back(a[index-1][j]/2);
            a[index].push_back(a[index-1][j]/2-1);
        }else{
            a[index].push_back(a[index-1][j]/2);
            a[index].push_back(a[index-1][j]/2);
        }
        j++;
        i++;
    }
    if(a[index-1][j]%2==0){
        ans.rmin=a[index-1][j]/2-1;
        ans.rmax=a[index-1][j]/2;
    }else{
        ans.rmin=a[index-1][j]/2;
        ans.rmax=a[index-1][j]/2;
    }
    
    
//    for(int i=0;i<a[index].size();i++){
//        if(ans.rmin>a[index][i]){
//            ans.rmin=a[index][i];
//        }
//        if(ans.rmax<a[index][i]){
//            ans.rmax=a[index][i];
//        }
//    }
    //cout << a[0][0] << endl;
    return ans;
}


int main(int argc, const char * argv[])
{
    
    ifstream ifs( "a.txt" );
    int T;
    ifs >> T;
    int t=1;
    
    while(t<=T){
        long long N,K;
        ifs >> N >> K;
        PP p=solve(N,K);
        cout << "Case #" << t << ": " << p.rmax << " " << p.rmin << endl;

        //printf("%.6f\n",ans);
        t++;
    }
    return 0;
}
