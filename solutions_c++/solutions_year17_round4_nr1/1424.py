#include <bits/stdc++.h>
const long long mod = 1e9+7;
const double ex = 1e-10;
#define inf 0x3f3f3f3f
using namespace std;
int a[200];
int dp[200][200][200];
int dfs(int a,int b, int c)
{
    if (a<0||b<0||c<0) return -1;
    if (dp[a][b][c]!=-1) return dp[a][b][c];
    int ans = 0;
    //1111
    if (a==0&&b==0&&c==0) return 0;
    if (a==4&&b==0&&c==0) return 1;
    if (a==3&&b==0&&c==0) return 1;
    if (a==2&&b==0&&c==0) return 1;
    if (a==1&&b==0&&c==0) return 1;
    //22
    if (a==0&&b==2&&c==0) return 1;
    if (a==0&&b==1&&c==0) return 1;
    //3333
    if (a==0&&b==0&&c==4) return 1;
    if (a==0&&b==0&&c==3) return 1;
    if (a==0&&b==0&&c==2) return 1;
    if (a==0&&b==0&&c==1) return 1;
    //233
    if (a==0&&b==1&&c==2) return 1;
    if (a==0&&b==1&&c==1) return 1;
    //211
    if (a==1&&b==1&&c==0) return 1;
    if (a==2&&b==1&&c==0) return 1;
    //13
    if (a==1&&b==0&&c==1) return 1;
    ans = max(ans,dfs(a,b,c-4)+1);
    ans = max(ans,dfs(a-4,b,c)+1);
    ans = max(ans,dfs(a,b-2,c)+1);
    ans = max(ans,dfs(a-1,b,c-1)+1);
    ans = max(ans,dfs(a,b-1,c-2)+1);
    ans = max(ans,dfs(a-2,b-1,c)+1);
    return dp[a][b][c] = ans;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    int cas = 1;
    while (T--)
    {
        int N,P;
        cin >> N >>P;
        printf("Case #%d: ",cas++);
        for (int i = 1;i<=N;i++)
            cin >>a[i];
        if (P==2)
        {
            int c1 =0,c2 =0;
            for (int i = 1;i<=N;i++)
                if (a[i]%2==0) c2++;
            else c1++;
            int ans = c2+(c1+1)/2;
            cout << ans <<endl;
        }
        if (P==3)
        {
            int c1 = 0,c2=0,c3 =0 ;
            for (int i = 1; i<=N;i++)
                if (a[i]%3==0) c3++;
            else if (a[i]%3==1) c1++;
            else if (a[i]%3==2) c2++;
            int ans = c3+min(c1,c2) + (max(c1,c2) - min(c1,c2) + 2 )/3;
            cout <<ans <<endl;
        }
        if (P==4)
        {
            int c1 = 0,c2 = 0,c3 = 0,c4 =0;
            for (int i = 1; i<=N;i++)
            if (a[i]%4==0) c4++;
            else if (a[i]%4==1) c1++;
            else if (a[i]%4==2) c2++;
            else c3++;
            int ans = c4;
            memset(dp,-1,sizeof(dp));
            ans += dfs(c1,c2,c3);
            cout << ans <<endl;
        }
    }
}
