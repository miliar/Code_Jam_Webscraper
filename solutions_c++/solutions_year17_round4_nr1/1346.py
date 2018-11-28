#include <bits/stdc++.h>

using namespace std;

int t,n,p,a[5];
int DP[102][102][102];
int fx[102][102][102];
int ans,i,j,k,x;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>n>>p;
        a[1]=a[2]=a[3]=ans=0;
        for (i=1;i<=n;i++) {
            cin>>x;
            if (x % p == 0) ans++; else
                a[x%p]++;
        }
        for (i=0;i<=a[1];i++)
            for (j=0;j<=a[2];j++)
                for (k=0;k<=a[3];k++) {
                    int lef=(i+2*j+3*k)%p;
                    if (fx[i+1][j][k] != t1 || DP[i+1][j][k] < DP[i][j][k]+(lef == 0)) {
                        DP[i+1][j][k]=DP[i][j][k]+(lef == 0);
                        fx[i+1][j][k]=t1;
                    }
                    if (fx[i][j+1][k] != t1 || DP[i][j+1][k] < DP[i][j][k]+(lef == 0)) {
                        DP[i][j+1][k]=DP[i][j][k]+(lef == 0);
                        fx[i][j+1][k]=t1;
                    }
                    if (fx[i][j][k+1] != t1 || DP[i][j][k+1] < DP[i][j][k]+(lef == 0)) {
                        DP[i][j][k+1]=DP[i][j][k]+(lef == 0);
                        fx[i][j][k+1]=t1;
                    }
        }
        cout<<"Case #"<<t1<<": "<<ans+DP[a[1]][a[2]][a[3]]<<endl;
    }
}
