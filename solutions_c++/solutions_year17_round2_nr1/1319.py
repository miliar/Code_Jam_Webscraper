#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <iomanip>
#include <deque>
#include <stdio.h>
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define UNIQUE(Itr) sort((Itr).begin(),(Itr).end()); (Itr).erase(unique((Itr).begin(),(Itr).end()),(Itr).end())
#define LBOUND(Itr,val) lower_bound((Itr).begin(),(Itr).end(),(val))
#define UBOUND(Itr,val) upper_bound((Itr).begin(),(Itr).end(),(val))
#define MOD 1000000007
typedef long long ll;

double need_time(double D, double K, double S) {
    double diff = D - K;
    return diff / S;
}

int main() {
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/R1B/A/Alargein.txt");
    int T; ifs >> T;
    REP(kai,T) {
        double D;
        int N;
        ifs >> D >> N;
        vector<double> K(N),S(N);
        REP(i,N) ifs >> K[i] >> S[i];
        double need = 0.0;
        REP(i,N) need = max(need,need_time(D,K[i],S[i]));
        cout << fixed << setprecision(10) << "Case #" << kai + 1 << ": " << D / need << endl;
    }
    
    return 0;
}