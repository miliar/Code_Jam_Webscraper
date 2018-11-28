#include <bits/stdc++.h>
using namespace std;

#define sc(a) scanf("%d",&a)
#define scm(a,b) scanf("%d%d",&a,&b)
#define fl(c,i,n) for(int i=c;i<n;i++)
#define f(i,n) for(int i=0;i<n;i++)
#define mem(a) memset(a,0,sizeof(a))
#define ll long long int
#define ull unsigned long long int
#define inf INT_MAX
#define linf LLONG_MAX
#define pb push_back
#define pp pop_back()
#define aov(a) a.begin(),a.end()
//#define mp make_pair
#define nl printf("\n")
#define PI 2.0*acos(0.0) //#define PI acos(-1.0)
#define xx first
#define yy second
#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))
#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())
#define to_c_string(a) a.c_str()
#define strtoint(c) atoi(&c[0])
#define pii pair<int,int>
#define MAXN 500005
#define MOD 1000000007

template <class T> inline T bigmod(T p,T e,T M){
    ll ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}
/*int fact[MAXN];
int invfact[MAXN];
int inv(int a, int b){
    if(b==0)
        return 1;
    if(b&1)
        return (long long)a*inv(a, b-1)%MOD;
    else{
        int res = inv(a, b>>1);
        return (long long)res*res%MOD;
    }
}
void init(){
    fact[0] = 1;
    for(int i=1;i<MAXN;i++){
        fact[i] = (long long)fact[i-1]*i%MOD;
    }
    invfact[MAXN-1] = inv(fact[MAXN-1], MOD-2);
    for(int i=MAXN-1;i>0;i--){
        invfact[i-1] = (long long)invfact[i]*i%MOD;
    }
}
int C(int n, int r){
    if(r>n || r<0)
        return 0;
    return (long long)((long long)fact[n]*invfact[r]%MOD)*invfact[n-r]%MOD;
}*/
int T, k;
string s;
void solve(){
    sc(T);
    for(int t=0;t<T;t++){
        int ans = 0;
        cin>>s>>k;
        string S = s;
        map<string, int> mp;
        mp[s] = 1;
        int l=s.length();
        for(int i=0;i+k-1<l;i++){
            if(s[i]=='-'){
                ans++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='+')   s[j] = '-';
                    else    s[j] = '+';
                }
            }
            //cout<<s<<"\n";
        }
        int flag = 0;
        for(int i=0;i<l;i++){
            if(s[i]=='-'){
                flag = 1;
                break;
            }
        }
        if(flag)    cout<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE\n";
        else    cout<<"Case #"<<(t+1)<<": "<<ans<<"\n";
    }
}
int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A1.out", "w", stdout);
	//init();
    solve();
    return 0;
}

