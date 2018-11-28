#include <bits/stdc++.h>
using namespace std;
string s[30];
struct node
{
        int v,l,r;
}q[55][55];
int a[55];
int N,Q;
int ans;
bool cmp(node a,node b)
{
    return a.v<b.v;
}
bool dfs(int x,int l ,int r)
{
    if (x==N+1) {ans = 1;return true;}
    for (int i = 1 ; i<=Q; i++)
    {
        if (q[x][i].v == -1) continue;
        int ll = max(l,q[x][i].l);
        int rr = min(r,q[x][i].r);
        if (ll<=rr)
        {
            q[x][i].v = -1;
            dfs(x+1,ll,rr);
            if (ans == 1) return true;
            q[x][i].v = 1;
        }
    }
    return false;
}
int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int T;
   cin >> T;

   for (int cas  = 1 ;  cas <= T ;cas++)
   {

       cin >> N  >> Q;
       for (int i = 1; i<= N; i++)
        cin >> a[i];
       for (int i = 1; i<=N;i++)
        {
            for (int j = 1; j<=Q; j++)
            {
                cin >> q[i][j].v;
                q[i][j].l = ceil(q[i][j].v/(1.1*a[i]));
                q[i][j].r =q[i][j].v *100/(90*a[i]);
                //cout<<q[i][j].l<<" "<<q[i][j].r <<endl;
            }
            sort(q[i]+1,q[i]+Q+1,cmp);
        } int anst = 0;
       for (int i = 1; i<=Q; i++)
       {
           ans = 0;
           if (dfs(1,1,1e6))  anst++;
       }
       printf("Case #%d: ",cas);
       cout << anst <<endl;
   }
}
