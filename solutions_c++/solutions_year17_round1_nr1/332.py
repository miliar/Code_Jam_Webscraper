#include <bits/stdc++.h>
using namespace std;

int t,i,j,lstx,lsty,n,m;
char a[55][55];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>n>>m;
        for (i=1;i<=n;i++)
            for (j=1;j<=m;j++)
                cin>>a[i][j];
        cout<<"Case #"<<t1<<":"<<endl;
        lsty=m+1;
        for (j=m;j>=1;j--) {
            lstx=0;
            for (i=1;i<=n;i++)
                if (a[i][j] != '?') {
                    for (int i1=lstx+1;i1<=i;i1++)
                        for (int j1=j;j1<lsty;j1++)
                            a[i1][j1]=a[i][j];
                lstx=i;
            }
            if (lstx) {
                for (int i1=lstx+1;i1<=n;i1++)
                    for (int j1=j;j1<lsty;j1++)
                        a[i1][j1]=a[lstx][j];
                lsty=j;
            }
        }
        for (j=lsty-1;j>=1;j--)
            for (i=1;i<=n;i++)
                a[i][j]=a[i][j+1];
        for (i=1;i<=n;i++) {
            for (j=1;j<=m;j++)
                cout<<a[i][j];
            cout<<endl;
        }
    }
}
