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
#define traverse(a) for(auto i=a.begin();i!=a.end();i++)
#define INF 1200
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pb(a) push_back(a)
#define X first
#define Y second
#define MOD 10001000
typedef vector<bool> vb;
int main(){
    lo t,T;
    freopen("B-large.in","r",stdin);
    freopen("outputB.out","w",stdout);
    cin>>T;
    for(t=1;t<=T;t++){
        string a;
        cin>>a;
        lo start=a.length();
        REP(0,a.length()-1)if(a[i]>a[i+1]){
            start=i;
            break;
        }
        cout<<"Case #"<<t<<": ";
        if(start==a.length()){
            cout<<a<<endl;
            continue;
        }
        lo s=a.length();
        for(lo i=start;a[i]>a[i+1] and i>=0;i--){
            a[i]--;
            s=i;
        }
        REP(s+1,a.length())a[i]='9';
        if(a[0]=='0')cout<<a.substr(1,a.length()-1);
        else cout<<a;
        cout<<endl;
    }
    return 0;
}
