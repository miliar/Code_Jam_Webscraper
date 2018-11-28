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
#define inf -1e13;
#define pb push_back
#define pi 3.1415926535897932384626433832795
struct node{
    double x,y,sur,pase;
    bool operator < (const node & p) const
    {
    if(x==p.x)return y>p.y;
        return x>p.x;
    }
};
int casio=1,vis[1200][1200];
double dp[1200][1200];
vector<node>vc;
double dp_func(int pos,int koyta)
{
    if(pos==vc.size()){
        if(koyta==0)return 0.0;
        return inf;
    }
    if(koyta==0)return 0;
    if(vis[pos][koyta]==casio)return dp[pos][koyta];
    vis[pos][koyta]=casio;
    double ret;
    ret=dp_func(pos+1,koyta-1)+vc[pos].pase;
    ret=max(ret,dp_func(pos+1,koyta));
    return dp[pos][koyta]=ret;


}
int main()
{
   freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    double a,b,c,d,e,f,g,h,t=2;
    int i,j,k,l,m,n,test;
    scanf("%d",&test);
    while(test--){
    double sum=0,now;
    double ma=0;
    scanf("%d%d",&n,&k);
    node gr;
    vc.clear();
    for(i=1;i<=n;i++){
        scanf("%lf%lf",&a,&b);
        gr.x=a;
        gr.y=b;
        gr.sur=pi*a*a;
      //  if(i==1)cout<<a<<" "<<pi*a*a<<" "<<gr.sur<<endl;
        gr.pase=pi*t*a*b;
        vc.pb(gr);
    }
    sort(vc.begin(),vc.end());
   for(i=0;i<vc.size();i++){
    d=vc[i].sur+vc[i].pase;
    e=dp_func(i+1,k-1);
    //if(i==1)cout<<vc[i].x<<" "<<gr.sur<<" "<<gr.pase<<endl;
    d=d+e;
 //
    ma=max(ma,d);
 //  }
}
printf("Case #%d: %.10f\n",casio++,ma);
}


}
