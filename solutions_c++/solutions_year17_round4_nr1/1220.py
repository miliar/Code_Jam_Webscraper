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
#define PI              acos(-1.0)
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
const int N = 100;
int ara[N+5];
int cnt[5];
int answer,id;
int dp[101][101][101];
int vis[101][101][101];
int n,p;

int call(int a,int b,int c)
{
    if(a==cnt[1] and b==cnt[2] and c==cnt[3])return 0;
    if(vis[a][b][c]==id)return dp[a][b][c];
    vis[a][b][c]=id;
    int cost = (a + 2*b + 3*c)%p;
    int add = (cost==0);

    int ret = 0;
    if(a<cnt[1])ret = max(ret,add+call(a+1,b,c));
    if(b<cnt[2])ret = max(ret,add+call(a,b+1,c));
    if(c<cnt[3])ret = max(ret,add+call(a,b,c+1));

    return dp[a][b][c]=ret;
}
int main()
{
    fRead("Alarge.in");
    fWrite("Aout.txt");
    int t,cases=0;
    cin >> t;
    while(t--)
    {
        MEM(cnt,0);
        id++;

        cin >> n >> p;
        REP(i,n)cin >> ara[i];
        REP(i,n){
            ara[i]%=p;
            cnt[ara[i]]++;
        }
        answer = cnt[0] + call(0,0,0);
        cout << "Case #" << ++cases  << ": " << answer << "\n";
    }

}
/*
1
50 3
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
*/
