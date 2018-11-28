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
using namespace std;

typedef vector<int> vi;

int main(void){
    freopen("C:/Users/Rideasnail/Downloads/B-small-attempt1.in","r",stdin);
    freopen("C:/Users/Rideasnail/Downloads/out.txt","w",stdout);

    int tc;
    sci(tc);

    FOR(x,tc)
    {
        int R,O,Y,G,B,V,N;
        int color[6];
        string baseColor = "ROYGBV";
        cin >> N;
        for(int i=0;i<6;i++){
            cin >> color[i];
        }
        string answer = "";

        if(color[0]*2>N || color[2]*2>N || color[4]*2>N){
            answer = "IMPOSSIBLE";
        } else {
            int col1 = 0;
            for(int i=0;i<6;i++){
                if(color[i] > color[col1]) {
                    col1 = i;
                }
            }

            while(true){
                if(color[col1]==0){
                    for(int i=0;i<6;i++){
                        if(color[i] > color[col1]) {
                            col1 = i;
                        }
                    }
                }
                int col2 = 0;
                int sum = 0;
                if(col1==0){
                    col2 = 2;
                }
                for(int i=0;i<6;i++){
                    if(i!=col1 && color[i] > color[col2]) {
                        col2 = i;
                    }
                    sum+=color[i];
                }
                if(sum==0){
                    break;
                }
                if(sum==1){
                    answer+=baseColor[col1];
                    color[col1]--;
                    break;
                }

                answer+=baseColor[col1];
                answer+=baseColor[col2];
                color[col1]--;
                color[col2]--;
            }
        }

        cout << "Case #" << x+1 << ": " << answer << endl;
    }


    return 0;
}
