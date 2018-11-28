#include<bits/stdc++.h>

using namespace std;

#define fRead(x)  freopen(x,"r",stdin)
#define fWrite(x) freopen (x,"w",stdout)

#define LL long long
#define ULL unsigned long long
#define ff first
#define ss second
#define pb push_back
#define INF 2e16
#define PI acos(-1.0)
#define mk make_pair
#define pii pair<int,int>
#define pll pair<LL,LL>


#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(a,min(b,min(c,d)))
#define max4(a,b,c,d) max(a,max(b,max(c,d)))
#define SQR(a) ((a)*(a))
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define ROF(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,b) for(int i=0;i<b;i++)
#define MEM(a,x) memset(a,x,sizeof(a))
#define ABS(x) ((x)<0?-(x):(x))

#define scanI(a) scanf("%d",&a)
#define scanI2(a,b) scanI(a) , scanI(b)
#define scanI3(a,b,c) scanI(a), scanI(b), scanI(c)
#define scanI4(a,b,c,d) scanI(a), scanI(b), scanI(c), scanI(d)

#define scanL(a) scanf("%I64d",&a)
#define scanL2(a,b) scanL(a) , scanL(b)
#define scanL3(a,b,c) scanL(a), scanL(b), scanL(c)
#define scanL4(a,b,c,d) scanL(a), scanL(b), scanL(c), scanL(d)

#define SORT(v) sort(v.begin(),v.end())
#define REV(v) reverse(v.begin(),v.end())


#define FastRead ios_base::sync_with_stdio(0);cin.tie(nullptr);

string str;
int dp[31][31][2];
int call(int pos,int pre,int tight)
{
    if(pos==str.size()){
        return 1;
    }
    if(dp[pos][pre][tight]!=-1)return dp[pos][pre][tight];
    int ret = 0;
    int d = str[pos] - '0';
    int st = 9;
    if(tight)st = d;
    for(int i = st;i>=pre;i--){
        int newtight = tight;
        if(i!=st)newtight = 0;
        ret = ret | call(pos+1,i,newtight);
    }
    return dp[pos][pre][tight] = ret;
}
int found;
void dfs(int pos,int pre,int tight,string &s)
{
    if(found)return;
    if(pos==str.size()){
        found = 1;
        return;
    }
    int d = str[pos] - '0';
    int st = 9;
    if(tight)st = d;
    for(int i = st;i>=pre;i--){
        int newtight = tight;
        if(i!=st)newtight = 0;
        if(call(pos+1,i,newtight)==1){
            s+= char(i + '0');
            dfs(pos+1,i,newtight,s);
            break;
        }
    }
    return;
}
int main()
{
    freopen("Blarge.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    int cases = 0;
    while(t--){
        MEM(dp,-1);
        found =  0;
        cin >> str;
        string s;
        dfs(0,0,1,s);
        while(s[0]=='0'){
            s.erase(s.begin());
        }
        cout << "Case #" << ++cases << ": " << s << "\n";
    }
}
