#include<bits/stdc++.h>

using namespace std;

#define fRead(x)        freopen(x,"r",stdin)
#define fWrite(x)       freopen (x,"w",stdout)

#define LL              long long
#define ULL             unsigned long long
#define ff              first
#define ss              second
#define pb              push_back
#define INF             2e16
#define mk              make_pair
#define pii             pair<int,int>
#define pll             pair<LL,LL>


#define min3(a,b,c)     min(a,min(b,c))
#define max3(a,b,c)     max(a,max(b,c))
#define min4(a,b,c,d)   min(a,min(b,min(c,d)))
#define max4(a,b,c,d)   max(a,max(b,max(c,d)))
#define SQR(a)          ((a)*(a))
#define FOR(i,a,b)      for(int i=a;i<=b;i++)
#define ROF(i,a,b)      for(int i=a;i>=b;i--)
#define REP(i,b)        for(int i=0;i<b;i++)
#define MEM(a,x)        memset(a,x,sizeof(a))
#define ABS(x)          ((x)<0?-(x):(x))

#define SORT(v)         sort(v.begin(),v.end())
#define REV(v)          reverse(v.begin(),v.end())


#define FastRead        ios_base::sync_with_stdio(0);cin.tie(nullptr);

int Ac,Aj;
const int n = 1440;
string str;
int dp[n+2][n+2][2][2];
int vis[n+2][n+2][2][2] , id;

int call(int a,int b,int pl,int st)
{
    int pos = a + b;
    if(pos==n){
        return pl!=st;
    }
    if(vis[a][b][pl][st]==id)return dp[a][b][pl][st];
    vis[a][b][pl][st]=id;

    int newst = st;
    int ret = 12345;

    if(pos==0){
        if(str[pos]=='0'){
            if(a<720)ret = call(a+1,b,0,0);
            if(b<720)ret = min(ret,call(a,b+1,1,1));
        }else if(str[pos]!='1'){
            if(a<720)ret = call(a+1,b,0,0);
        }else{
            if(b<720)ret = call(a,b+1,1,1);
        }
    }
    else{
        if(str[pos]=='0'){
            if(a<720)ret = (pl!=0) + call(a+1,b,0,st);
            if(b<720)ret = min(ret,(pl!=1) + call(a,b+1,1,st));
        }else if(str[pos]!='1'){
            if(a<720)ret = (pl!=0) + call(a+1,b,0,st);
        }else{
            if(b<720)ret = (pl!=1) + call(a,b+1,1,st);
        }
    }
    return dp[a][b][pl][st] = ret;
}
int main()
{
    freopen("Blarge.in","r",stdin);
    freopen("Bout.txt","w",stdout);

    int t,cases=0;
    cin >> t;
    while(t--)
    {
        str.clear();
        id++;
        cin >> Ac >> Aj;
        REP(i,n)str+="0";

        int l,r;
        REP(i,Ac){
            cin >> l >> r;
            for(int j = l;j<r;j++)str[j]='1';
        }
        REP(i,Aj){
            cin >> l >> r;
            for(int j = l;j<r;j++)str[j]='2';
        }
        int a = call(0,0,0,0);
        int b = call(0,0,1,0);
        cout << "Case #" << ++cases << ": " << min(a,b) << "\n";
    }
}
