#include <bits/stdc++.h>
 using namespace std;

#define pb push_back
#define m_p make_pair
#define F first
#define S second
#define For(i,a,b) for(int i=a;i<b;i++)
#define Fore(i,a,b) for(int i=a;i<=b;i++)
#define rFor(i,a,b) for(int i=a;i>b;i--)
#define rFore(i,a,b) for(int i=a;i>=b;i--)
#define tr(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define all(a) a.begin(),a.end()
#define mem(a,b) memset(a,b,sizeof(a))
typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<int,pii> pi3;
typedef pair<pii,pii> pi4;
typedef vector<int> vi;
typedef vector<pii> vpii;
void sc(int& a){scanf("%d",&a);}
void sc(lli& a){scanf("%lld",&a);}
void sc(int& a,int& b){sc(a);sc(b);}
void sc(lli& a,lli& b){sc(a);sc(b);}
void sc(int& a,int& b,int& c){sc(a,b);sc(c);}
void sc(lli& a,lli& b,lli& c){sc(a,b);sc(c);}
void prl(int a){printf("%d\n",a);}
void prl(lli a){printf("%lld\n",a);}
void prl(){printf("\n");}
void prs(int a){printf("%d ",a);}
void prs(lli a){printf("%lld ",a);}
void prl(lli a, lli b){cout<<a<<" "<<b<<" "<<endl;}
void prl(lli a, lli b, lli c){cout<<a<<" "<<b<<" "<<c<<" "<<endl;}
void prl(lli a, lli b, lli c, lli d){cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;}
void prl(lli a, lli b, lli c, lli d, lli e){cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<endl;}
void prl(lli a, lli b, lli c, lli d, lli e, lli f){cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<endl;}
lli mod = 1000000007;
lli pmod=40000;
lli modpow(lli a, lli b, lli mod){lli res=1;while(b>0){if(b&1)res=(res*a)%mod;a=(a*a)%mod;b=b/2;}return res%mod;}
lli pow(lli a, lli b){lli res=1;while(b>0){if(b&1)res=(res*a);a=(a*a);b=b/2;}return res;}
lli modulo(lli a,lli b){
  lli c = a%b;
  return c;
}
lli modInverse(lli a, lli m)
{
    lli  m0 = m, t, q;
    lli x0 = 0, x1 = 1;
 
    if (m == 1)
      return 0;
 
    while (a > 1)
    {
        // q is quotient
        q = a / m;
 
        t = m;
 
        // m is remainder now, process same as
        // Euclid's algo
        m = a % m, a = t;
 
        t = x0;
 
        x0 = x1 - q * x0;
 
        x1 = t;
    }
 
    // Make x1 positive
    if (x1 < 0)
       x1 += m0;
 
    return x1;
}
int modI[100000];

 
#define inf INT_MAX
#define linf LLONG_MAX
const lli MAX = 10000005;
#define N 100000+5
const int M = 100000+5;
#define BLOCK_SIZE 320
lli max(lli a, lli b) { return (a > b)? a : b; }
typedef pair<lli, lli> Key;
lli
gcd ( lli a, lli b )
{
  lli c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

/* Recursive Standard C Function: Greatest Common Divisor */
lli 
gcdr ( lli a, lli b )
{
  if ( a==0 ) return b;
  return gcdr ( b%a, a );
}

int phi(int n)
{    
    int result = n;   // Initialize result as n
 
    // Consider all prime factors of n and subtract their
    // multiples from result
    for (int p=2; p*p<=n; ++p)
    {
        // Check if p is a prime factor.
        if (n % p == 0)
        {
            // If yes, then update n and result 
            while (n % p == 0)
                n /= p;
            result -= result / p;
        }
    }
 
    // If n has a prime factor greater than sqrt(n)
    // (There can be at-most one such prime factor)
    if (n > 1)
        result -= result / n;
    return result;
}

bool v[MAX];
int len, sp[MAX];

void Sieve(){
  for (int i = 2; i < MAX; i += 2)  sp[i] = 2;//even numbers have smallest prime factor 2
  for (lli i = 3; i < MAX; i += 2){
    if (!v[i]){
      sp[i] = i;
      for (lli j = i; (j*i) < MAX; j += 2){
        if (!v[j*i])  v[j*i] = true, sp[j*i] = i;
      }
    }
  }
}

#include <stdio.h>
 
void multiply(lli F[2][2], lli M[2][2]);
 
void power(lli F[2][2],lli n);
 
/* function that returns nth Fibonacci number */
lli fib(lli n)
{
  lli F[2][2] = {{1,1},{1,0}};
  if (n == 0)
    return 0;
  power(F, n-1);
  return F[0][0];
}
 
/* Optimized version of power() in method 4 */
void power(lli F[2][2], lli n)
{
  if( n == 0 || n == 1)
      return;
  lli M[2][2] = {{1,1},{1,0}};
 
  power(F, n/2);
  multiply(F, F);
 
  if (n%2 != 0)
     multiply(F, M);
}
 
void multiply(lli F[2][2], lli M[2][2])
{
  lli x =  ((F[0][0]*M[0][0])%mod + (F[0][1]*M[1][0])%mod)%mod;
  lli y =  ((F[0][0]*M[0][1])%mod + (F[0][1]*M[1][1])%mod)%mod;
  lli z =  ((F[1][0]*M[0][0])%mod + (F[1][1]*M[1][0])%mod)%mod;
  lli w =  ((F[1][0]*M[0][1])%mod + (F[1][1]*M[1][1])%mod)%mod;
 
  F[0][0] = x;
  F[0][1] = y;
  F[1][0] = z;
  F[1][1] = w;
}
string s;

double A[100005],B[100005];

int main()
{
  // Create a graph given in the above diagram
  int t;
  int p=0;
  int n;
  double d,k;
  cin>>t;

  double ans=inf;
  while(t--){

    p++;
    cin>>d>>n;
    ans=inf;
    For(i,0,n)
      cin>>A[i]>>B[i];

      k=0;
    For(i,0,n){
      k=max(k,(d-A[i])/B[i]);
    }

    ans=d/k;


    printf("Case #%d: %lf\n",p,ans);  
    }


}


 



