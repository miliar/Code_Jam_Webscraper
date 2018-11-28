#include<bits/stdc++.h>
using namespace std;

const int maxn = 1e5+5;
int T,cs,m,n,res,a[55];
vector<int> v[55];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.ou","w",stdout);
    scanf("%d",&T);
    while(T--){
        res=0;
        for(int i=1; i<=n; ++i)v[i].clear();
        scanf("%d%d",&n,&m);
        for(int i=1; i<=n; ++i)scanf("%d",&a[i]);
        for(int i=1; i<=n; ++i){
            for(int j=1,x; j<=m; ++j){
                scanf("%d",&x);
                v[i].push_back(x);
            }
            sort(v[i].begin(),v[i].end(),greater<int>());
        }
        bool br=0,ctn;
        for(int k=1; ;){
            ctn=0;
            for(int i=1; i<=n; ++i){
                while(!v[i].empty() && v[i].back()*10<9*a[i]*k)v[i].pop_back();
                if(v[i].empty()){
                    br=1;
                    break;
                }
                if(v[i].back()*10>11*a[i]*k){
                    ctn=1;
                    break;
                }
            }
            if(br)break;
            if(ctn){
                ++k;
                continue;
            }
            for(int i=1; i<=n; ++i)v[i].pop_back();
            ++res;
        }
        printf("Case #%d: %d\n",++cs,res);
    }
}
