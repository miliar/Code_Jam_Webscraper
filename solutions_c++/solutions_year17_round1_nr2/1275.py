/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Aditya Agarwal
 * IT, MNNIT-ALLAHABAD 
 * aditya.mnnit15@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include<bits/stdc++.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second

 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)


//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;

int dp[10][(1<<9)+5];
int n,m;
int qua[3],mat[10][10];

int func(int x,int mask){
    if(x==m)
        return 0;
    else if(dp[x][mask]!=-1)
        return dp[x][mask];
    int ans=0;
    rep(i,m){
        if((mask&(1<<i))==0){
            int a=mat[0][x],b=mat[1][i];
            int flag=0,k=1;
            //cout<<a<<" "<<(0.9*qua[0])<<endl;
            int mx=max((a*10)/(9*qua[0]),(b*10)/(9*qua[1]));   
            int mn=min((a*10)/(11*qua[0]),(b*10)/(11*qua[1]));
            //cout<<mn<<" "<<mx<<endl;  
            for(int j=mn;j<=mx;j++){
                if(qua[0]*j*9<=10*a && qua[0]*j*11>=10*a && qua[1]*j*9<=10*b && qua[1]*j*11>=10*b)
                    ans=max(ans,1+func(x+1,(mask|(1<<i))));
            }
        }
    }
    ans=max(ans,func(x+1,mask));
    return dp[x][mask]=ans;
}
int main(){
    int t;
    inp(t);
    int p=1;
    while(t--){
        inp2(n,m);
        rep(i,n)
            cin>>qua[i];
        rep(i,n)
            rep(j,m){
                cin>>mat[i][j];
            }
        memset(dp,-1,sizeof(dp));
        int ans=0;
        if(n>1)
            ans=func(0,0);
        else {
            ans=0;
            rep(i,m){
                int mx=(mat[0][i]*10)/(9*qua[0]);
                int mn=(mat[0][i]*10)/(11*qua[0]);
                //cout<<i<<" "<<v<<endl;
                for(int j=mn;j<=mx;j++){
                    if(mat[0][i]*10>=9*j*qua[0] && mat[0][i]*10<=11*j*qua[0]){
                    //cout<<i<<endl;
                    ans++;
                    break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",p++,ans);
    }

    return 0;
}
