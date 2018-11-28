#include<bits/stdc++.h>
using namespace std;
typedef long long lo;
typedef vector<string> vs;
typedef pair<lo,lo> ll;//pair
typedef vector<lo> vl;  //vector of long
typedef vector<ll > vll;   //vector of pair
typedef priority_queue<lo>p_q;
#define CHECK_BIT(var,pos) ((var) & (1<<(pos)))
#define mp(a,b) make_pair((a),(b))
#define REP(a,b) for(lo i=(a);i<(b);i++)//no need to declare variable i
#define REPE(a,b,c,d) REP(a,b)for(lo j=(c);j<(d);j++)//no need to declare vaiables i,j
#define REPV(a,b,c) for((a)=b;(a)<(c);(a)++)//a is the variable
#define IREP(a,b) for(lo i=(a);i>=(b);i--)
#define IREPV(a,b,c) for((a)=b;(a)>=(c);(a)--)
#define all(v) (v).begin(),(v).end()
#define TRvl(c) for (vl::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvll(c) for (vll::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvm(c) for (map<lo,lo>::iterator it=(c).begin(); it != (c).end(); it++)
#define INF 1200
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pb(a) push_back(a)
#define X first
#define Y second
#define MOD 1000000007
typedef vector<bool> vb;
int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("outputA.out","w",stdout);
    lo t,T;
    cin>>T;
    for(t=1;t<=T;t++){
        string a;
        cin>>a;
        lo k;
        cin>>k;
        lo index=0;
        lo ans=0;
        while(index+k-1<a.length()){
            while(a[index]=='+' and index<a.length())index++;
            if(a[index]=='-' and index+k-1<a.length()){
                    ans++;
                    REP(0,k){
                        if(a[index+i]=='+')a[index+i]='-';
                        else a[index+i]='+';
                    }
            }
        }
        REP(0,a.length())if(a[i]=='-')ans=-1;
        cout<<"Case #"<<t<<": ";
        if(ans==-1)cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}
