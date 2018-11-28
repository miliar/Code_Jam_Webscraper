#include<bits/stdc++.h>
using namespace std;
//custom
#define endl ('\n')
#define space (" ")
#define __ ios_base::sync_with_stdio(false);cin.tie(0);
//utils
#define SET(a,b) (memset(a,b,sizeof(a)))
//for vectors
#define pb push_back
#define mp make_pair
typedef vector<int> vi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
//data types
typedef long long ll;
typedef long long LL;
//loops
#define REP(i,a,b) \
    for(int i = int(a);i <= int(b);i++)
#define MEMSET_INF 127 //2bill
#define MEMSET_HALF_INF 63 //1bill

#ifdef DEBUG
    #define debug(args...) {dbg,args; cerr<<endl;}
    #define _
#else
    #define debug(args...)  // Just strip off all debug tokens
    #define _ ios_base::sync_with_stdio(false);cin.tie(0);
#endif 
struct debugger
{
    template<typename T> debugger& operator , (const T& v)
    {    
        cerr<<v<<" ";    
        return *this;    
    }
} dbg;

const int mod = 1000000007;
inline void add(int &x, int y){x+=y; if(x>=mod)x-=mod; if(x<0)x+=mod;}
inline int mul(int x, int y){ return ((LL)x * y)%mod;}
int gcd(int a, int b){ if(b)return gcd(b,a%b); return a;}
int power(int a ,int p){int ret = 1; while(p){if(p&1)ret=mul(ret,a); a=mul(a,a); p/=2;}return ret;}
int phi(int n){ int ret=n; int i = 2; 
    if(n%i==0){ ret-=ret/i; while(n%i==0)n/=i;}
    for(i=3; i*i<=n; i++)if(n%i==0){ ret-=ret/i; while(n%i==0)n/=i;}
    if(n>1)ret-=ret/n;return ret;
}

int main(){
    _
    int t;
    cin>>t;
    REP(t1, 1, t){
        string s;
        int k;
        cin>>s>>k;
        int n = s.length();
        int flips = 0;
        REP(i, 0, n-1){
            if(i + k > n)break;
            if(s[i] == '-'){
                // flip k elements including i;
                REP(j, i, i+k-1){
                    if(s[j] == '-')s[j] = '+';
                    else s[j] = '-';
                }
                flips++;
            }
            // cout << s << endl;
        }
        bool flag = true;
        REP(i, 0, n-1)
            if(s[i] == '-')
                flag = false;

        debug(s);
        cout << "Case #" << t1 << ": ";
        if(flag)
            cout << flips << endl;
        else
            cout << "IMPOSSIBLE\n";
    }
    return 0;
}
