#include<bits/stdc++.h>
using namespace std;
int rr[55][55];
int ll[55][55];
int r[55];
int x[55];
int pt[55];
int solve()
{
    int n,p;
    cin>>n>>p;
    for(int i=1;i<=n;i++){
        cin>>r[i];
        pt[i]=1;
    }
    for(int i=1;i<=n;i++){
        for(int j=1;j<=p;j++){
            cin>>x[j];
        }
        sort(x+1,x+1+p);
        for(int j=1;j<=p;j++){
            rr[i][j]=floor((1.0*x[j]/9*10)/r[i]);
            ll[i][j]=ceil((1.0*x[j]/11*10)/r[i]);
            //printf("%d %d %d %d\n",i,j,ll[i][j],rr[i][j]);
        }
    }
    int ans=0;
    for(int i=1;i<=1e6;i++)
    {
        for(int j=1;j<=n;j++){
            if(ll[j][pt[j]]>i) break;
            while(rr[j][pt[j]]<i){
                pt[j]++;
                if(pt[j]>p) return ans;
            }
            if(ll[j][pt[j]]>i) break;
            if(j==n) ans++;
            if(j==n)
            for(int k=1;k<=n;k++) {pt[k]++; if(pt[k]>p) return ans; i--;}
        }
    }
    return ans;
}
int main()
{
    int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin>>t;
    for(int i=1;i<=t;i++){
        cout<<"CASE #"<<i<<": ";
        cout<<solve()<<'\n';
    }
}
