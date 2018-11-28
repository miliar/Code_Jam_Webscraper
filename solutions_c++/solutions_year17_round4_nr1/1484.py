#include <bits/stdc++.h>

using namespace std;
map<pair<pair<int,int>,pair<int,int> >,int > M;
int main(){
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int t;cin >> t;
    int index=1;
    while(t--){
        int n,p;cin >> n >> p;
        int zero=0;int one=0;int two=0;int three=0;

        int g[105];
            for(int i=1;i<=n;++i){
                cin >> g[i];
                g[i]%=p;
                if(g[i]==0) ++zero;
                if(g[i]==1) ++one;
                if(g[i]==2) ++two;
                if(g[i]==3) ++three;
            }
        if(p==2){
            int ans=(one)/2;int ans2=0;int l=0;
            for(int i=1;i<=one;++i){
                if(l!=0) ++ans2;
                l=(l+1)%p;
            }
            cout << "Case #" << index++  << ": " <<  n-ans2 <<  endl;
        }
        if(p==3){
            int coun=max(one,two);
            int coun2=min(one,two);
            coun-=coun2;
           int  ans=coun-(coun/3)+coun2;int ans2=coun2;
           int l=0;
           int u=0;for(int i=1;i<=coun;++i){
                if(l!=0) ++ans2;
                l=(l+1)%p;
           }
             cout << "Case #" << index++ << ": " << n-ans2 << endl;
        }
        if(p==4){
            M.clear();
            M[make_pair(make_pair(0,0),make_pair(0,0))]=0;
            M[make_pair(make_pair(0,0),make_pair(0,1))]=0;
            M[make_pair(make_pair(0,0),make_pair(0,2))]=0;
            M[make_pair(make_pair(0,0),make_pair(0,3))]=0;
            for(int i=0;i<=one;++i){
                for(int j=0;j<=two;++j){
                    for(int k=0;k<=three;++k){
                        for(int l=0;l<4;++l){
                            if(i==0 && j==0 && k==0) continue;
                            if(M.find(make_pair(make_pair(i,j),make_pair(k,l)))==M.end()) M[make_pair(make_pair(i,j),make_pair(k,l))]=1000;
                            int u=M[make_pair(make_pair(i,j),make_pair(k,l))];
                            int kr;
                            if(l)
                                kr=1;
                            else
                                kr=0;

                            if(i) u=min(u,kr+M[make_pair(make_pair(i-1,j),make_pair(k,(l+1)%p))]);
                            if(j) u=min(u,kr + M[make_pair(make_pair(i,j-1),make_pair(k,(l+2)%p))]);
                            if(k) u=min(u,kr + M[make_pair(make_pair(i,j),make_pair(k-1,(l+3)%p))]);
                           // cout << i << " " << j << " " << k << " " << l << " " <<  u << endl;
                            M[make_pair(make_pair(i,j),make_pair(k,l))]=u;
                         }

                    }
                }
            }
            cout << "Case #" << index++ << ": " << n-M[make_pair(make_pair(one,two),make_pair(three,0))] << endl;

        }
    }
    return 0;
}
