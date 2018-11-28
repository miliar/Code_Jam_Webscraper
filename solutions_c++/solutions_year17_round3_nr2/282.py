#include <bits/stdc++.h>
using namespace std;
typedef double LD;
const int LEN(1441);
int T,f[LEN][721][2],s[2][LEN];
bool a[2][LEN];
inline int sm(int f,int l,int r){
    return s[f][r]-(l<=0?0:s[f][l-1]);
}
int main(){
    freopen("B.in","r",stdin);
//    freopen("B.out","w",stdout);
    cin>>T;
    for(int ti=1;ti<=T;ti++){
        int n,m;
        cin>>n>>m;
        memset(a,0,sizeof(a));
        for(int i(1);i<=n;i++){
            int l,r;
            cin>>l>>r;
            for(int j(l);j<r;j++)
                a[0][j]=true;
        }
        for(int i(1);i<=m;i++){
            int l,r;
            cin>>l>>r;
            for(int j(l);j<r;j++)
                a[1][j]=true;
        }
        for(int j(0);j<2;j++)
            for(int i(0);i<LEN;i++)
                s[j][i]=(i==0?0:s[j][i-1])+a[j][i];
        memset(f,0x7f,sizeof(f));
        int mxx=f[0][0][0];
        f[0][0][0]=f[0][0][1]=0;
        for(int i(1);i<LEN;i++)
            for(int j(0);j<i;j++)
                for(int k(0);k<min(721,j+1);k++)
                    for(int t(0);t<2;t++)
                        if(f[j][k][t]!=mxx){
                            if(sm(0,j+1,i)==0)
                                f[i][k+i-j][0]=min(f[i][k+i-j][0],f[j][k][t]+bool(t==1));
                            if(sm(1,j+1,i)==0)
                                f[i][k][1]=min(f[i][k][1],f[j][k][t]+bool(t==0));
                        }
        printf("Case #%d: %d\n",ti,min(f[1439][720][0],f[1439][720][1]));
    }   
    return 0;
}