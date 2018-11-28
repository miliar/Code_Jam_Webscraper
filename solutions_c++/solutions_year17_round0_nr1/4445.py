//JAI KALI MAA - (JKM)..-----THERE IS NO SECRET INGREDIENT.
//www.moovon.me
#include<bits/stdc++.h>
using namespace std;

//template jkm
#define ll   long long
#define jkm()int t; cin>>t; while(t--)
#define mp(a,b)  make_pair(a,b)
#define pb(a)push_back(a)
#define si(n)scanf("%d",&n)
#define ps   printf(" ")
#define pn   cout<<"\n";
#define pi(n)printf("%d\n", n)
#define all(v)   v.begin(),v.end()
#define l(a) a.length()
#define sz(a)a.size()
#define rep(i,n)  for(int i=0;i<n;i++)
#define debug(x) cout << '>' << #x << ':' << x << endl;
#define printarray(a,i,n)  for(int i=0; i<n; i++) cout<<a[i]<<" ";
#define ios {std::ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);}
#define inputarray()int n; cin>>n;int a[n]; rep(i,n) cin>>a[i];
 
 
template< class T > T gcd(T a, T b) {  while(b^=a^=b^=a%=b); return a; }  //gcd
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b);}  //lcm
template<class T> inline bool isPrimeNumber(T n) {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T multiplyMod(T a,T b,T m) {return (T)((((ll)(a)*(ll)(b)%(ll)(m))+(ll)(m))%(ll)(m));}
template<class T> inline T powerMod(T p,int e,T m) {if(e==0)return 1%m;else if(e%2==0){T t=powerMod(p,e/2,m);return multiplyMod(t,t,m);}else return multiplyMod(powerMod(p,e-1,m),p,m);}
char toLowerCase(char c){return (isupper(c))?(c+32):c;}
char toUpperCase(char c){return (islower(c))?(c-32):c;}
ll decimaltobinary(ll b) {ll p10 = 1, ret = 0;for(; b > 0; b >>= 1){ret += p10*(b&1);p10 *= 10;}return ret;}
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}
const double pi=acos(-1.0);
 
//freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
//----------------------------------------------CodeYard--------------------------------------------------// 


int main(){
freopen("jkma.in","r",stdin);freopen("snennya.out","w",stdout);
ll z=0;
jkm(){
string s;
cin>>s;
int n;
cin>>n;
int c=0;
int l=l(s);
for(int i=0;i<=l(s)-n;i++){
    if(s[i]=='-'){
        c++;
        for(int j=i;j<i+n;j++){
            if(s[j]=='-') s[j]='+';
            else s[j]='-';
        }
    }
    // debug(s);
}

cout<<"Case #"<<++z<<": ";
if(count(all(s),'-')!=0) cout<<"IMPOSSIBLE";
else cout<<c;
pn;
}
return 0;
} 