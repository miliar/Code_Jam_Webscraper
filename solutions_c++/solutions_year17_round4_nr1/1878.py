#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <list>

using namespace std;

int kol[7];

int dp[111][111][6];
int dp4[111][111][111][6];


int res3(int a1,int a2,int l)
{
    if (dp[a1][a2][l]!=-1){return dp[a1][a2][l];}
    if (a1==0&&a2==0){return 0;}
    if (a1==0){return (l==0)+res3(0,a2-1,(l+2)%3);}
    if (a2==0){return (l==0)+res3(a1-1,0,(l+1)%3);}
    dp[a1][a2][l]=(l==0)+max(res3(a1-1,a2,(l+1)%3),res3(a1,a2-1,(l+2)%3));
    //cout << a1 << ' ' << a2 << ' ' << l << ' ' << dp[a1][a2][l]<< endl;
    return dp[a1][a2][l];
}

int res4(int a,int b,int c,int d){return 0;}

int main()
{
    freopen("a","r",stdin);
    freopen("b","w",stdout);
    int t;
    cin >> t;
    int tre=1;
    while(t--)
    {
        cout << "Case #" << tre++ << ": ";
        int n,p;
        cin >> n >> p;
        kol[0]=kol[1]=kol[2]=kol[3]=0;
        for (int i=0;i<n;i++)
        {
            int g=0;
            cin >> g;
            kol[g%p]++;
        }
        int res=kol[0];
        for (int i=0;i<=106;i++)for (int j=0;j<=106;j++)for (int k=0;k<=5;k++){dp[i][j][k]=-1;}
        if (p==2)
        {
            int now=0;
            while(kol[1]){if (now){now=0;}else{res++;now++;}kol[1]--;}
            cout << res << endl;
        }
        else if (p==3){//cout << kol[1] << kol[2] << endl;
        cout << res+res3(kol[1],kol[2],0) << endl;}
        else if (p==4)
        cout << res+res4(kol[1],kol[2],kol[3],0) << endl;
    }
    return 0;
}
