#include<bits/stdc++.h>
using namespace std;
const long long INF=1e9+7;
const double INFL=1e15;
long long d[105][105];
int e[105],s[105];
double c[105];
set<pair<double,int> > st;
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cout<<fixed<<setprecision(9);
    int i,j,k,l,n,q,t;
    cin>>t;
    for(l=1;l<=t;++l){
        cin>>n>>q;
        for(i=1;i<=n;++i)
            cin>>e[i]>>s[i];
        for(i=1;i<=n;++i)
            for(j=1;j<=n;++j){
                cin>>d[i][j];
                if(d[i][j]==-1) d[i][j]=INF;
            }
        for(k=1;k<=n;++k)
            for(i=1;i<=n;++i)
                for(j=1;j<=n;++j)
                    if(d[i][k]!=-1&&d[k][j]!=-1)
                        d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
        cout<<"Case #"<<l<<":";
        while(q--){
            for(i=1;i<=n;++i) c[i]=INFL;
            st.clear();
            cin>>j>>k;
            c[j]=0.0;
            st.insert(make_pair(c[j],j));
            while(!st.empty()){
                j=st.begin()->second;
                if(j==k) break;
                st.erase(st.begin());
                for(i=1;i<=n;++i)
                    if(d[j][i]<=e[j]&&c[i]>c[j]+1.0*d[j][i]/s[j]){
                        st.erase(make_pair(c[i],i));
                        c[i]=c[j]+1.0*d[j][i]/s[j];
                        st.insert(make_pair(c[i],i));
                    }
            }
            cout<<" "<<c[k];
        }
        cout<<"\n";
    }
}
