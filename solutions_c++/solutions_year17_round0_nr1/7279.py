#include<bits/stdc++.h>
using namespace std;
typedef long long lo;
typedef vector<string> vs;
typedef pair<lo,lo> ll;//pair
typedef vector<lo> vl;  //vector of long
typedef vector<ll > vll;   //vector of pair
typedef priority_queue<lo>p_q;
#define CHECK_BIT(var,pos) ((var) & (1<<(pos)))
#define X first
#define Y second
#define mp(a,b) make_pair((a),(b))
#define REP(a,b) for(lo i=(a);i<(b);i++)//no need to declare variable i
#define REPE(a,b,c,d) REP(a,b)for(lo j=(c);j<(d);j++)//no need to declare vaiables i,j
#define REPV(a,b,c) for((a)=b;(a)<(c);(a)++)//a is the variable
#define IREP(a,b) for(lo i=(a);i>=(b);i--)
#define IREPV(a,b,c) for((a)=b;(a)>=(c);(a)--)
#define all(v) (v).begin(),(v).end()
#define TRvl(c) for (vl::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvll(c) for (vll::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pb(a) push_back((a))
#define mod 1000000007

int main(){
    lo i,j,k,l,m,n,te,_,ans,t;
    string s;
    ifstream fin ("A-large.in");
    ofstream fout("bans.out");
    fin>>t;
    bool flag;
    for(n=1;n<=t;n++){
        fin>>s>>k;
        ans=0;
        l = s.length();
        REP(0,s.length()){
            if(s[i]=='-' && i+k-1<l){
                REPV(j,i,k+i){if(j==l)break;if(s[j]=='-')s[j]='+';else if(s[j]=='+')s[j]='-';}ans++;
            }
            //cout<<s<<endl;
        }
        flag=true;
        REP(0,s.length())if(s[i]=='-'){flag=false;break;}
        fout<<"Case #"<<n<<": ";
        if(flag)fout<<ans<<endl;
        else fout<<"IMPOSSIBLE"<<endl;
    }
}
