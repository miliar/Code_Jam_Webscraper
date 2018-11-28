/*************************************
**----------------------------------**
*|**********************************|*
*|*  CODE By : Mohd. Ausaf Jafri   *|*
*|*     ECE, MNNIT , Allahabad     *|*
*|*                                *|*
*|*      ausafjafri@gmail.com      *|*
*|*   "Think Twice, Code Once"     *|*
*|**********************************|*
**----------------------------------**
**************************************/

/******** HEADER FILES ****************/

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp> 
using namespace std;
using namespace __gnu_pbds;

/******* STL & LOOPS ************************/

#define TESTCASE int tt; ind(tt) while(tt--)
#define upto(i,n) for(int i=0;i<n;i++)
#define from(i,a,b) for(int i=a;i<=b;i++)
#define rev(i,a,b) for(int i=a;i>=b;i--)
#define mp make_pair
#define pb push_back
#define fi first
#define se second

/************* CONSTANTS ********************/

const long long int inf = 1e17 + 110;
const int mod = 1e9 + 7;
const int MAX = 1e6 + 3;

/******* INPUTS-ALL KIND ********************/

#define inc(c) scanf("%c",&c);
#define ins(s) scanf("%s",s);
#define ind(n) scanf("%d",&n);
#define inlld(n) scanf("%lld",&n);
#define ind2(n,m) scanf("%d%d",&n,&m);
#define inlld2(n,m) scanf("%lld%lld",&n,&m);

/******* OUTPUTS-ALL KIND *********************/
    
#define opc(c) printf("%c\n",c);
#define ops(s) printf("%s\n",s);
#define opd(n) printf("%d\n",n);
#define oplld(n) printf("%lld\n",n);
#define opd2(n,m) printf("%d %d\n",n,m);
#define oplld2(n,m) printf("%lld %lld\n",n,m);

/******* ALIASING ***********************/
    
typedef long long ll;
typedef vector<int> vi;
typedef set<int> si;
typedef vector<ll> vll;    
typedef pair<int, int> ii; //pair
typedef vector<ii> vii;   //vector of pair
typedef vector< pair<int, ii> > edgelist; //maintain edge list

/********** USER DEFINED FUNCTIONS *******/

int isprime(int N){
    if(N<2 || (!(N&1) && N!=2))
        return 0;
    for(int i=3; i*i<=N; i+=2){
        if(!(N%i))
            return 0;
    }
    return 1;
}

ll power(ll a,ll b)
{
    ll res=1;
    a=a%mod;
    while(b>0)
    {
        if(b&1)
            res=(res*a)%mod;
        b=b>>1;
        a=(a*a)%mod;
    }
    return res;
}

ll inv[55];
void pre() {
      for (int i = 1; i <= 50; i++) {
            inv[i] = power(i, mod - 2);
      }
}

ll nCr(ll n, ll r) {
      pre();
      if (r > n) return 0;
      if (n - r < r) r = n - r;
      n %= mod;
      ll ans = 1;
      upto(i, r) {
            ans = (ans * (n - i)) % mod;
            ans = (ans * inv[i + 1]) % mod;
      }
      return ans;
}

int gcd(int a,int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
/********** LOGIC STARTS HERE ************/
    
int main()
{
   int k=1;
   TESTCASE
   {
   	ll n;
   	inlld(n)
   	if(n<10)
   		{printf("Case #%d: %lld\n",k,n);
   	     k++;
   		continue;
   	    }
   	ll temp=n;
   	stack<int>s;
   	while(temp)
   	{
   		s.push(temp%10);
   		temp=temp/10;
   	}
   	vi arr;
   	while(!s.empty())
   	{
   		int val=s.top();
   		s.pop();
        arr.pb(val);
   	}
    int i,j;
    for(i=0;i<arr.size()-1;i++)
    {
        if(arr[i]>arr[i+1])
        {
        	arr[i]--;
        	for(j=i;j>=1;j--)
        	{
        		if(arr[j-1]>arr[j])
        			arr[j-1]--;
        		else
        			break;
        	}
        	int k=j+1;
        	for(;k<arr.size();k++)
        		arr[k]=9;
        }
    }
   
   	printf("Case #%d: ",k);
   	upto(i,arr.size())
   	{
   		if(arr[i]!=0)
   			cout<<arr[i];
   	}
   	cout<<endl;
   	k++;
   }   
}