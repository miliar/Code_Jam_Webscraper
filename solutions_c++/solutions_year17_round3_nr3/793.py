#include "bits/stdc++.h"
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define MOD  1000000007
#define INF  0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
typedef long long ll;

int N,K;
double U;
vector<double> P;

bool judge(double x){
    
    double sum = 0.0;
    REP(i,P.size()) {
        if(P[i] < x)  sum += x - P[i];
    }
    
    if(sum <= U) return true;
    return false;
}

double BinarySearch(double low, double high){
    REP(i,1000){
        double mid=(low+high)/2;
        if(judge(mid))low = mid;
        else high = mid;
    }
    return low;
}


int main() {
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/R1C/C/Csmallin.txt");
    int T; ifs >> T;
    
    REP(kai,T) {
        
        ifs >> N >> K >> U;
        P.resize(N);
        REP(i,N) ifs >> P[i];
        
        double least = BinarySearch(0.0,1.0);
        REP(i,P.size()) if(P[i]<least) P[i] = least;
        
        double ans = 1.0;
        REP(i,P.size()) ans *= P[i];
        
        cout << "Case #" << kai + 1 << ": ";
        cout << fixed << setprecision(10) << ans << endl;
    }
    
    
    return 0;
}

