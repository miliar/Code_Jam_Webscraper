#include<iostream>
#include<iomanip>
#include<algorithm>
#include<queue>
#include<set>
#include<cstdio>
#include<map>
#include<limits>
#include<cstring>
#include<string>
#include<sstream>
#include<utility>
using namespace std;
typedef long long ll;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int I=1;I<=T;++I){
        int R,C;
        cin>>R>>C;
        static string rows[110];
        for(int i=1;i<=R;++i)
            cin>>rows[i];
        for(int i=1;i<=R;++i){
            int j=i;
            while(rows[j]==string(C,'?'))
                ++j;
            int k=j+1;
            while(rows[k]==string(C,'?')&&k<=R)
                ++k;
            for(int u=0;u<C;++u){
                char last;
                if(rows[j][u]!='?'){
                    last=rows[j][u];
                    for(int v=0;v<=u;++v){
                        if(rows[j][v]=='?'||v==u){
                            rows[j][v]=rows[j][u];
                            for(int jj=i;jj<=j;++jj)
                                rows[jj][v]=rows[j][u];
                            if(k==R+1){
                                for(int jj=j+1;jj<=R;++jj)
                                    rows[jj][v]=rows[j][u];
                            }
                        }
                    }
                }
                if(u==C-1&&rows[j][u]=='?'){
                    for(int v=0;v<=u;++v){
                        if(rows[j][v]=='?'){
                            rows[j][v]=last;
                            for(int jj=i;jj<=j;++jj)
                                rows[jj][v]=last;
                            if(k==R+1){
                                for(int jj=j+1;jj<=R;++jj)
                                    rows[jj][v]=last;
                            }
                        }
                    }
                }
            }
            i=j;
            if(k==R+1)
                break;
        }
        cout<<"Case #"<<I<<":\n";
        for(int i=1;i<=R;++i)
            cout<<rows[i]<<endl;
    }
    return 0;
}
