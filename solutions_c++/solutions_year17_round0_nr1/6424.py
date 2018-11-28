#include <bits/stdc++.h>
#define MAX(a,b)   (((a)>(b))?(a):(b))
#define MIN(a,b)   (((a)>(b))?(b):(a))
#define ABS(x)     ((x>0)?(x):(-(x)))
#define ulli       unsigned long long int
#define lli        long long int
#define pb         push_back
#define mp         make_pair
#define fi         first
#define se         second
#define all(x)     x.begin(),x.end()
#define rall(x)    x.rbegin(),x.rend()
#define vi         vector<lli>
#define pii        pair<lli,lli>
#define matrix     vector<vector<lli> >
#define rep(lo,hi) for(lli i=lo;i<hi;i++)
#define mem(a,val) memset(a,val,sizeof(a))
#define digits(n)  (floor(log10(n))+1)
#define bin_1(n)    __builtin_popcount(n)
#define ios        ios_base::sync_with_stdio(false);cin.tie(0)
#define out        cerr<<(float(clock())/CLOCKS_PER_SEC)<<endl
#define iss(s)     istringstream(s)
#define MOD        1000000007
#define eps        1e-9
#define whats(x) cerr << #x << " is " << x << endl
const lli oo = (lli)1e18+10;
const int inf = 0x3f3f3f3f;
const double PHI = ((sqrt(5)+1)/2);
const double PI = acos(-1.0);
using namespace std;
lli CEIL(lli,lli);
lli FLOOR(lli a,lli b) { if(b<0) return FLOOR(-a,-b); else if(a<0) return -1*CEIL(-a,b); else return a/b; }
lli CEIL(lli a,lli b) { if(b<0) return CEIL(-a,-b); else if(a<0) return -1*FLOOR(-a,b); else return (a+b-1)/b; }
lli gcd(lli a,lli b) { if(b==0) return a; return gcd(b,a%b); }
lli lcm(lli a,lli b) { return (a*b)/gcd(a,b); }
lli exgcd(lli a,lli b,lli &x,lli &y){ if(a==0) { x=0; y=1; return b; } lli xx,yy,g=exgcd(b%a,a,xx,yy); x=yy-(b/a)*xx; y=xx; return g; }
int bin1(lli x) { int r=0; while(x) { r++; x&=x-1; } return r; }
lli power(lli b,lli e) { if(e==0) return 1; if (e%2==0) return power(b*b,e/2); return b*power(b*b,e/2); }
double powerf(double b,int e) {if(e==0) return 1; if(e%2==0)return powerf(b*b,e/2); else{ if(e>0)return b*powerf(b*b,e/2); else return powerf(b*b,e/2)/b;}}
lli modpow(lli b,lli e,lli m) { lli r=1; b=b%m; while(e>0) { if(e%2==1) r=(r*b)%m; e/=2; b=(b*b)%m; } return r; }
lli modinverse(lli a,lli mod) { return modpow(a,mod-2,mod);    }
lli modinverse2(lli a,lli m) { lli x,y; exgcd(a,m,x,y);  while(x<0) x+=m; return x; }
lli nCrmod(lli n,lli r,lli m) {if(r>n) r=n-r; lli res=1; for(lli i=r;i>=1;i--) { res=(res*(n-i+1))%m; res=(res*modinverse(i,m)); } return res; }
lli nCr(lli n,lli r) {if(r>n) r=n-r; lli res=1; for(lli i=r;i>=1;i--) { res*=(n-i+1); res/=i; } return res; }
lli totient(lli n) { lli res=n,p; for(p=2;p*p<=n;p++){ if(n%p==0){ while(n%p==0) n/=p; res-=res/p; }} if(n>1) res-=res/n; return res; }
bool isprime(lli x) { if(x==1) return false; for(lli i=2;i*i<=x;i++) if(x%i==0) return false; return true; }
bool isvowel(char c) { if(isupper(c)) c=tolower(c); return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'; }
bool istriangle(lli a,lli b,lli c) { return (a+b>c)&&(a+c>b)&&(b+c>a); }
lli stringmod(string s,lli mod) { lli res=0; for(unsigned int i=0;i<s.size();i++) res=(res*10+s[i]-'0')%mod; return res; }
lli powinfact(lli n,lli p) { lli res=0,pw=p; while(n>=pw) { res+=(n/pw); pw*=p; } return res; }
matrix matrixmultiply(matrix A,matrix B,lli n) { matrix C(2,vector<lli>(n)); for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) C[i][j]=(C[i][j]+A[i][k]*B[k][j]); return C; }
matrix modmatrixmultiply(matrix A,matrix B,lli n,lli mod) { matrix C(2,vector<lli>(n)); for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) C[i][j]=(C[i][j]+A[i][k]*B[k][j])%mod; return C; }
matrix powermatrix(matrix A,lli exp,lli n) { if(exp==1) return A; if(exp%2) return matrixmultiply(A,powermatrix(A,exp-1,n),n); matrix X=powermatrix(A,exp/2,n); return matrixmultiply(X,X,n); }
matrix modpowmatrix(matrix A,lli exp,lli n,lli mod) { if(exp==1) return A; if(exp%2) return modmatrixmultiply(A,modpowmatrix(A,exp-1,n,mod),n,mod); matrix X=modpowmatrix(A,exp/2,n,mod); return modmatrixmultiply(X,X,n,mod); }
lli merge(lli a[],lli l,lli m,lli r) { lli i=l,j=m+1,k=0,inv_cnt=0,temp[r-l+1]; while(i<=m&&j<=r) { if(a[i]<=a[j]) temp[k++]=a[i++]; else { temp[k++]=a[j++]; inv_cnt+=(m-i+1); } } while(i<=m) temp[k++]=a[i++]; while(j<=r) temp[k++]=a[j++]; for(i=l;i<=r;i++) a[i]=temp[i-l]; return inv_cnt; }
lli mergesort(lli a[],lli l,lli r) { lli inv_count=0; if(l<r) { lli m=(l+r)/2; inv_count+=mergesort(a,l,m); inv_count+=mergesort(a,m+1,r); inv_count+=merge(a,l,m,r); } return inv_count; }
double dist(lli x1,lli y1,lli x2,lli y2) { return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)); }
#define N (int)1e6+10
void pre()
{
}
void gcj()
{   //freopen("C:\\Users\\atul5095\\Downloads\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\atul5095\\Downloads\\A-large.in","r",stdin);
    //freopen("C:\\Users\\atul5095\\Downloads\\input.in","r",stdin);
    freopen("F:\\Code\\TestC++\\output.txt","w",stdout);
    lli t; cin>>t;
    for(lli c=1;c<=t;c++)
    {   cout<<"Case #"<<c<<": ";
        string s;
        int k,n,ans=0;
        bool f=true;
        cin>>s>>k;
        n=s.size();
        for(int i=0;i<=n-k;i++)
        {   if(s[i]=='-')
            {   for(int j=i;j<i+k;j++)
                    s[j]=(s[j]=='-'?'+':'-');
                ans++;
            }
        }
        for(int i=0;i<n;i++) if(s[i]=='-') f=false;
        if(f) cout<<ans;
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
}
void judge()
{
}
int main()
{   ios;
    pre();
    lli tt=1;
    //cin>>tt;
    while(tt--)
    {   //judge();
		gcj();
    }
    return 0;
}
