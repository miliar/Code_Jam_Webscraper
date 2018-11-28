#include<bits/stdc++.h>
using namespace std;
int N;
double st[1001];
double sp[1001];
double dist[101][101];
double dp[101][101];
bool pos;
double recurse (int i,int j ){
if(i==N-1){
return 0;
pos=true;
}
double ans =(double)LONG_LONG_MAX;

double prev=0.0;
if(dp[i][j]!=-1.0){

    return dp[i][j];
}

double req=dist[i][i+1];
if(st[j]>=req){
prev=st[j];
st[j]-=req;
ans= min(ans,recurse(i+1,j)+(req/sp[j]));
st[j]=prev;
}
if(st[i]>=req){
prev=st[i];
st[i]-=req;
ans=min(ans,(recurse(i+1,i)+(req/sp[i])));
st[i]=prev;

}
return dp[i][j]=ans;
}




int main(){
  freopen("C:\\Users\\Chandan\\Desktop\\input.txt", "r", stdin);
freopen("C:\\Users\\Chandan\\Desktop\\gcj1.txt", "w", stdout);

int q;
double D,x,y;
int t,i,j;
cin>>t;
int lc=1;
while(t--){
        pos=false;
        cout<<"Case #"<<lc<<": ";
        lc++;
        cin>>N>>q;;
        for(i=0;i<N;i++){
        cin>>st[i]>>sp[i];
        }
for(i=0;i<N;i++){

for(j=0;j<N;j++){
cin>>dist[i][j];
dp[i][j]=-1.0;
}

}
int st,en;
cin>>st>>en;

double ans = recurse(0,0);


    printf("%.7lf\n",ans);

}
return 0;
}
