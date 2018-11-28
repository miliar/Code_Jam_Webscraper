#include <bits/stdc++.h>
using namespace std;

int t,n,p,i,j,ans,l,r,res;
int now[55][55];
int a[55],st[55],kmi[55];
int b[55][55];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>n>>p;
        for (i=1;i<=n;i++)
            cin>>a[i];
        for (i=1;i<=n;i++) {
            for (j=1;j<=p;j++)
                cin>>b[i][j];
            sort(b[i]+1,b[i]+p+1);
        }
        cout<<"Case #"<<t1<<": ";
        res=0;
        for (i=1;i<=n;i++)
            st[i]=1;
        for (ans=1;ans<=1000000;ans++) {
            bool f1=true,f2=true;
            for (i=1;i<=n;i++) {
                kmi[i]=(a[i]*ans*9+9)/10;
                while (st[i] <= p && b[i][st[i]] < kmi[i])
                    st[i]++;
                if (st[i] <= p) {
                    kmi[i]=(a[i]*ans*11)/10;
                    if (b[i][st[i]] > kmi[i]) { f2=false; }
                } else f1=false;
            }
            if (!f1) break;
            if (!f2) continue;
            res++;
            for (i=1;i<=n;i++)
                st[i]++;
            ans--;
        }
        cout<<res<<endl;
    }
}
