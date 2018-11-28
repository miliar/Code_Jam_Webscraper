#include "bits/stdc++.h"
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define MOD  1000000007
#define INF  0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
typedef long long ll;

int dp[1500];

int main() {
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/R1C/B/Bsmallin.txt");
    int T; ifs >> T;
    
    REP(kai,T) {
        int ans = 0;
        int Ac,Aj; ifs >> Ac >> Aj;
        if(Ac==2 || Aj==2) {
            vector<int> a(4);
            REP(i,4) ifs >> a[i];
            sort(a.begin(),a.end());
            int diff1 = abs(a[2] - a[1]);
            if(diff1 == 0) {
                ans = 2;
            } else {
                int d1 = abs(a[3]-a[0]);
                int d2 = a[1] + (1440-a[2]);
                if(d1<=720||d2<=720){
                    ans = 2;
                } else {
                    ans = 4;
                }
            }
        } else if(Aj==1&&Ac==1){
            int t; REP(i,4) ifs >> t;
            ans = 2;
        } else {
            int t; REP(i,2) ifs >> t;
            ans = 2;
        }
        
        cout << "Case #" << kai + 1 << ": ";
        cout << fixed << setprecision(10) << ans << endl;
    }
    
    
    return 0;
}

