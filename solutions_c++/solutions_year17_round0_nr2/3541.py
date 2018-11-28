#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cmath>
#include<string>
#include<map>
#include<list>
#include<queue>
#include<utility>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<math.h>
#include<set>
#include<stack>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<iterator>
using namespace std;
#define pb push_back
#define ll long long
vector<int>vc;
ll sum=0;
int dp[20][3][12];
int dp_func(int pos,int ck,int last)
{
    if(pos==0)return dp[pos][ck][last]=1;
    int lim=vc[pos];;
    if(ck==1)lim=9;
    if(dp[pos][ck][last]!=-1)return dp[pos][ck][last];
    int ret=0;
    for(int i=lim;i>=last;i--){
        ret=ret||dp_func(pos-1,ck||i<lim,i);
   // cout<<i<<" "<<ret<<endl;
    }
    return dp[pos][ck][last]=ret;
}
void print(int pos,int ck,int last)
{
    if(pos==0)return ;
    int lim=vc[pos];
    if(ck)lim=9;
    for(int i=lim;i>=last;i--){
        if(dp[pos-1][ck||i<lim][i]){
            sum=sum*10+i;
            print(pos-1,ck||i<lim,i);
            return ;
        }

    }
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
int test,casio=1;
scanf("%d",&test);
while(test--){
        vc.clear();
    vc.pb(0);
sum=0;
    memset(dp,-1,sizeof dp);
    ll n;
    scanf("%lld",&n);
    while(n!=0){
        vc.pb(n%10);
        n=n/10;
    }
    int l=dp_func(vc.size()-1,0,0);
     print(vc.size()-1,0,0);
    printf("Case #%d: %lld\n",casio++,sum);
}
}
