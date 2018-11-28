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
#define vp(i,a) for(int i=0;i<a.size();++i)
using namespace std;
typedef long long ll;

static int Q[110][110];
int N,P;
static int R[110];
int v_in(int i,int j){
    int t=(i-1)*P+j-1;
    t*=2;
    return t;
}
int v_out(int i,int j){
    int t=(i-1)*P+j-1;
    t*=2;
    return t+1;
}
int v_src(){
    return 2*N*P;
}
int v_snk(){
    return 2*N*P+1;
}
int getbg2(int i,int j){
   if(Q[i][j]*10%(11*R[i])==0)
       return Q[i][j]*10/(11*R[i]);
   else
       return Q[i][j]*10/(11*R[i])+1;
}
int getbg(int i,int j){
    if(getbg2(i,j)<1){
        return 1;
    }
    return getbg2(i,j);
}

int geted(int i,int j){
   if(Q[i][j]*10%(9*R[i])==0)
       return Q[i][j]*10/(9*R[i]);
   else
       return Q[i][j]*10/(9*R[i]);
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;scanf("%d",&T);
    for(int I=1;I<=T;++I){

        cin>>N>>P;

        for(int i=1;i<=N;++i)
            cin>>R[i];
        for(int i=1;i<=N;++i){
            for(int j=1;j<=P;++j){
                cin>>Q[i][j];
            }
        }
        if(N==1){
            int ans=0;
            for(int j=1;j<=P;++j)
                if(getbg(1,j)<=geted(1,j))
                    ++ans;
            cout<<"Case #"<<I<<": ";
            cout<<ans<<endl;
        }else{
            int ans=0;
            static int mh[110];
            for(int j=1;j<=P;++j)
                mh[j]=j;
            do{
               int tans=0;
               for(int j=1;j<=P;++j){
                   //cout<<1<<" "<<j<<" "<<getbg(1,j)<<endl;
                   //cout<<1<<" "<<j<<" "<<geted(1,j)<<endl;
                   //cout<<2<<" "<<mh[j]<<" "<<getbg(2,mh[j])<<endl;
                   //cout<<2<<" "<<mh[j]<<" "<<geted(2,mh[j])<<endl;
                   if(getbg(1,j)>geted(1,j))
                       continue;
                   if(getbg(2,mh[j])>geted(2,mh[j]))
                       continue;
                   if(getbg(1,j)>geted(2,mh[j]))
                       continue;
                   if(getbg(2,mh[j])>geted(1,j))
                       continue;
                   ++tans;
               }
               ans=max(ans,tans);
            }while( next_permutation(mh+1,mh+P+1));
            cout<<"Case #"<<I<<": ";
            cout<<ans<<endl;
        }
    }
    return 0;
}
/*
1
2 2
50 100
450 449
1100 1101

*/
