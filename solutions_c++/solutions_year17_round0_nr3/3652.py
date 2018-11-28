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
struct node{
  int up,low,val;
   bool operator < (const node & p) const
    {
        if(val==p.val)return low>=p.low;
        return val<=p.val;
    }

};
int main()
{
     freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int test,casio=1;
    scanf("%d",&test);
    while(test--){
    priority_queue<node>q;
    while(!q.empty())q.pop();
    int i,j,k,l,m,n,ans1,ans2,s,t;
    node gr,pr;
   scanf("%d%d",&n,&k);
   gr.up=n;
   gr.low=1;
   gr.val=(n-1+1);
   q.push(gr);
   while(k){
    gr=q.top();
    q.pop();
        l=(gr.low+gr.up)/2;
        pr.low=gr.low;
        pr.up=l-1;
        pr.val=pr.up-pr.low+1;
        s=pr.val;
        if(pr.val){
            q.push(pr);
        }
        pr.low=l+1;
        pr.up=gr.up;
        pr.val=pr.up-pr.low+1;
        t=pr.val;
        if(pr.val){
            q.push(pr);
        }
        ans1=max(s,t);
        ans2=min(t,s);
    k--;
   }
    printf("Case #%d: %d %d\n",casio++,ans1,ans2);
}

}
