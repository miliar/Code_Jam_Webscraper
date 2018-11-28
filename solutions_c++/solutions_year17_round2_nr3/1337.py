#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sci(x) scanf("%d",&x)
#define scs(x) scanf("%s",&x)

#include <algorithm>
#include <bitset>
#include <cstdio>
#include <vector>
#include <queue>
#include <iomanip>
using namespace std;

typedef vector<int> vi;

int main(void){
    freopen("C:/Users/Rideasnail/Downloads/C-small-attempt1.in","r",stdin);
    freopen("C:/Users/Rideasnail/Downloads/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(x,tc)
    {
        int N, Q;
        int temp;
        cin >> N;
        cin >> Q;

        int energy[N];
        int speed[N];
        int dist[N][N];

        double dp_time[N][N];
        int dp_energy[N][N];

        for(int i=0;i<N;i++){
            cin >> energy[i];
            cin >> speed[i];
        }

        for(int i=0;i<N;i++)
            for(int ii=0;ii<N;ii++){
                cin >> dist[i][ii];
                dp_time[i][ii] = -1;
                dp_energy[i][ii] = -1;
            }

        cin >> temp;
        cin >> temp;

        dp_time[0][0] = 0;
        dp_energy[0][0] = energy[0];
        double answer;
        for(int i=0;i<N-1;i++){
            int myDist = dist[i][i+1];
            double bestTime = -1;
            for(int ii=0;ii<N;ii++){
                if(dp_energy[i][ii]>=0){

                    if(dp_energy[i][ii]>=myDist) {
                        double tm = dp_time[i][ii] + (myDist*1.0/speed[ii]);
                        if(dp_time[i+1][ii] < 0 || dp_time[i+1][ii] > tm) {
                            dp_time[i+1][ii] = tm;
                            dp_energy[i+1][ii] = dp_energy[i][ii] - myDist;
                        }
                        if(bestTime < 0 || bestTime > tm) {
                            bestTime = tm;
                        }
                    }

                    if(energy[i]>=myDist) {
                        double tm = dp_time[i][ii] + (myDist*1.0/speed[i]);
                        if(dp_time[i+1][i] < 0 || dp_time[i+1][i] > tm) {
                            dp_time[i+1][i] = tm;
                            dp_energy[i+1][i] = energy[i] - myDist;
                        }
                        if(bestTime < 0 || bestTime > tm) {
                            bestTime = tm;
                        }
                    }
                }
            }
            answer = bestTime;
        }

        cout << "Case #" << x+1 << ": " << setprecision(10) << answer << endl;
    }


    return 0;
}
