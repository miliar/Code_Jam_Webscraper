#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<map>
#include<queue>
#include<cstring>
#include<stack>
#include<set>
#include<vector>
#include<iostream>
#include<fstream>
#include<math.h>
#include<cmath>
#define mp(x,y) make_pair(x,y)
#define INF 1e9
#define EPS 1e-5
using namespace std;
int const sz=1e5+2;
int t;
map<string ,int > memo;
int n,k;
int solve (string inp,int idx){
    if(idx==n){
        for(int i=0;i<n;i++){
            if(inp[i]=='-')
                return INF;
    }
        return 0 ;

}
int ans=INF;
if(memo.count(inp))
    return memo[inp];
string a=inp;
for(int i=idx;i<idx+k&&idx+k-1<n;i++)
{
    if(a[i]=='+')
        a[i]='-';
    else
        a[i]='+';
}
ans=min(solve(inp,idx+1),solve(a,idx+1)+1);

return memo[inp]=ans;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.in","w",stdout);
    scanf("%d",&t);
    int cnt=1;
    while(t--){
        string mm;
        cin>>mm>>k;
        memo.clear();
        n=mm.size();
        int ans=solve(mm,0);
        if(ans==INF)
        {
        printf("Case #%d: IMPOSSIBLE\n",cnt++);

        }
        else
            printf("Case #%d: %d\n",cnt++,ans);


    }
return 0;
}
