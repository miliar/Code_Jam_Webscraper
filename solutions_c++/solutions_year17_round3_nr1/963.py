#include "bits/stdc++.h"
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RREP(i,n) for(int (i)=(int)(n)-1;i>=0;i--)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define MOD  1000000007
#define INF  0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
typedef long long ll;

int main() {
    
    ifstream ifs("/Users/kurodakousaku/GCJ/2017/R1C/A/Alargein.txt");
    int T; ifs >> T;
    
    REP(kai,T) {
        
        int K,N; ifs >> N >> K;
        vector<double> R(N),H(N);
        REP(i,N) ifs >> R[i] >> H[i];
        
        double ans = 0.0;
        vector< pair<double,double> > RH;
        REP(i,N) RH.push_back(make_pair(R[i],H[i]));
        sort(RH.begin(),RH.end());
        reverse(RH.begin(),RH.end());
        
        REP(i,N) {
            double r = RH[i].first;
            double anst = r * r * M_PI + r * RH[i].second * 2.0 * M_PI;
            vector<double> area;
            for(int j=i+1;j<N;j++) {
                area.push_back(RH[j].second * 2.0 * M_PI * RH[j].first);
            }
            sort(area.begin(),area.end());
            reverse(area.begin(),area.end());
            if(area.size() >= K-1) REP(j,K-1) anst += area[j];
            //if(area.size()>=1)cout << area[0] << endl;
            ans = max(ans,anst);
        }
        
        cout << "Case #" << kai + 1 << ": ";
        cout << fixed << setprecision(10) << ans << endl;
    }
    
    
    return 0;
}
