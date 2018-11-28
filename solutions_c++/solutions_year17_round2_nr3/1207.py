#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int n,q;
int e[105],s[105];
int d[105][105];
void read(){
    cin>>n>>q;
    for(int i=1;i<=n;i++){
        cin>>e[i]>>s[i];
    }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            cin>>d[i][j];
    int x;
    cin>>x>>x;
}
double mns[105];
void solve1(){
    for(int i=1;i<=n;i++)
        mns[i]=-1;
    mns[1]=0;
    double smd;
    for(int i=1;i<=n;i++){
        smd=d[i][i+1];
        for(int j=i+1;j<=n && smd<=e[i];j++){
            if(mns[j]<0 || mns[j]>mns[i]+smd/s[i]){
                mns[j]=mns[i]+smd/s[i];
            }
            smd+=d[j][j+1];
        }
    }
    printf("%.9llf\n",mns[n]);
}
int main(){
    int t;
    freopen("Cs.in","r",stdin);
    freopen("Cs.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        read();
        cout<<"Case #"<<i<<": ";
        solve1();
    }
}
