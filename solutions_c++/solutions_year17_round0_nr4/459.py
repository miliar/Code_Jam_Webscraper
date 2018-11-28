#include<bits/stdc++.h>
using namespace std;
int X[200][200];
int r[200];
int c[200];
typedef pair<int,int> ii;
set<ii> save;
map<int,int> d1,d2;
void solve()
{
    memset(X,0,sizeof X);
    memset(r,0,sizeof r);
    memset(c,0,sizeof c);
    d1.clear(); d2.clear();
    int n,k,x,y,ans=0;
    char C;
    cin>>n>>k;
    for(int i=1;i<=k;i++){
        cin>>C>>x>>y;
        if(C=='x'){
            r[x]=true;
            c[y]=true;
            X[x][y]+=1;
                ans++;
        }
        else if(C=='+'){
            d1[x+y]=true;
            d2[x-y]=true;
            X[x][y]+=2;
                ans++;
        }
        else {
            d1[x+y]=true;
            d2[x-y]=true;
            r[x]=true;
            c[y]=true;
            X[x][y]+=3;
                ans++;
                ans++;
        }
    }
    for(int i=1;i<=n;i++){
        if(!r[i])
        for(int j=1;j<=n;j++){
            if(!c[j]){
                r[i]=c[j]=true;
                X[i][j]+=1;
                save.insert(ii(i,j));
                ans++;
                break;
            }
        }
    }
    for(int i=1-n;i<=0;i++){
        int dis=i-(1-n);
        if(!d2[i])
        for(int j=1;j<=2*n;j++){
            if(!d1[j] && dis>=(abs(j-(n+1)))){
                d2[i]=d1[j]=true;
                X[(i+j)/2][(j-i)/2]+=2;
                ans++;
                save.insert(ii((i+j)/2,(j-i)/2));
                break;
            }
        }
        if(!d2[-i])
        for(int j=1;j<=2*n;j++){
            if(!d1[j] && dis>=(abs(j-(n+1)))){
                d2[-i]=d1[j]=true;
                X[(-i+j)/2][(j+i)/2]+=2;
                save.insert(ii((-i+j)/2,(j+i)/2));
                ans++;
                break;
            }
        }
    }
    cout<<ans<<" "<<save.size()<<'\n';
    {
        while(save.size()){
            x=save.begin()->first;
            y=save.begin()->second;
            cout<<((X[x][y]==1)?'x':((X[x][y]==2)?'+':'o'))<<" "<<x<<" "<<y<<'\n';
            save.erase(save.begin());
        }
    }
}
int main()
{
    int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
