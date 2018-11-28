#include<iostream>
#include<sstream>
#include<fstream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<functional>
#include<climits>
#include<utility>
#include <iomanip>
#include<map>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define REP(i,x) FOR(i,0,x)
#define CLR(a) memset((a), 0 ,sizeof(a))


const int MOD = 1e+9+7;
const double PI  = acos(-1.0);

int main(){
    int T;
    cin>>T;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";
        int n,q;
        cin>>n>>q;
        int e[n],s[n];
        REP(i,n) cin>>e[i]>>s[i];
        int d[n][n];
        REP(i,n) REP(j,n) cin>>d[i][j];
        int u,v;
        REP(i,q){
            cin>>u>>v;
            double dp[n];
            REP(i,n) dp[i]=1.0e+32;
            dp[0]=0.0;
            REP(i,n-1){
                int tdist=0;
                int curr=i;
                while(curr<n-1){
                    tdist+=d[curr][curr+1];
                    if(tdist>e[i]) break;
                    dp[curr+1]=min(dp[curr+1], dp[i]+(double)tdist/(double)s[i]);
                    curr+=1;
                }
            }
            cout<<fixed<<setprecision(7)<<dp[n-1]<<"\n";
        }
    }
}
