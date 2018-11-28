#include <bits/stdc++.h>
#include <tr1/unordered_map>
typedef long long ll;
typedef unsigned long long ull;
#define clr(ma) memset(ma,-1,sizeof ma)
#define inf 1000000000
#define vi vector<int>
#define pi pair<int  ,int >
#define mk make_pair
#define getBit(m,i) ((m&(1<<i))==(1<<i))
#define setBit(m,i) (m|(1<<i))
#define setBit2(m,i) (m|(1ull<<i))
#define cont(i,ma) ((ma.find(i))!=(ma.end()))
#define in(i) scanf("%d",&i)
#define in2(i,j) scanf("%d%d",&i,&j)
#define in3(i,j,k) scanf("%d%d%d",&i,&j,&k)
#define in4(i,j,k,l) scanf("%d%d%d%d",&i,&j,&k,&l)
#define il(i) scanf("%I64d",&i)
#define itr map<ll,ll>::iterator
#define itr2 map<ll,map<ll,ll> >::iterator
#define id(k) scanf("%9lf",&k)
#define fi(ss) freopen (ss,"r",stdin)
#define fo(ss) freopen (ss,"w",stdout)
#define clean(vis)  memset(vis,0,sizeof vis)
#define mo(x) ((x)<P?(x):(x)-P)
#define mo2(x) ((x)>=0?(x):(x)+P)
#define fast ios_base::sync_with_stdio(0);cin.tie(0);
#define sc(s)  scanf("%s",s)
using namespace std;
string s ;
const int N=21;
int dp [10][2][N];
int solve (int last,int g, int pos){
    if (pos==N)return 1;
    int &res=dp[last][g][pos];
    if (res!=-1)return res;
    res=0;
    for (int i=9;i>=last;i--){
        if (g==0 && s[pos]-'0'<i)continue;
        res|=solve(i,(s[pos]-'0'>i)?1:g,pos+1);
    }
    return res;
}
ll  trace(int last,int g, int pos,ll res=0){
    if (pos==N)return res;
    for (int i=9;i>=last;i--){
        if (g==0 && s[pos]-'0'<i)continue;
        if (solve(i,(s[pos]-'0'>i)?1:g,pos+1)){
           return trace(i,(s[pos]-'0'>i)?1:g,pos+1,res*10ll+i);

        }
    }
    return 0;
}
int main(){
    fi("/home/mohamedatef/ClionProjects/untitled1/input.txt");
    fo("/home/mohamedatef/ClionProjects/untitled1/out.txt");
    int t;
    in(t);
    for (int c=1;c<=t;c++){
        clr(dp);
        ll num;cin>>num;
      string g=to_string(num);
        s="";
        while (s.length()+g.length()<N)s+="0";
        s+=g;
        solve(0,0,0);
        ll res=trace(0,0,0);
        printf("Case #%d: %lld\n",c,res);
    }
}