#include <bits/stdc++.h>
#define max(a,b)   (((a)>(b))?(a):(b))
#define min(a,b)   (((a)>(b))?(b):(a))
#define ulli       unsigned long long int
#define lli        long long int
#define pb         push_back
#define mp         make_pair
#define fi         first
#define se         second
#define all(x)     x.begin(),x.end()
#define rall(x)    x.rbegin(),x.rend()
#define vi         vector<lli>
#define vii        vector<vi>
#define vs         vector<string>
#define pii        pair<lli,lli>
#define pis        pair<lli,string>
#define rep(i,lo,hi) for(lli i=lo;i<hi;i++)
#define MOD        1000000007
#define noof1(x)    __builtin_popcount(x)
#define sievesize  100000000
#define mt         make_tuple
#define eb         emplace_back
#define PI         3.141592653589793238
#define gcd        __gcd
#define digits(n)  (floor(log10(n))+1)
#define mini       INT_MIN
#define maxi       INT_MAX
#define minlli     LONG_LONG_MIN
#define maxlli     LONG_LONG_MAX
#define sz(a)      int((a).size())
#define ios        ios_base::sync_with_stdio(0);cin.tie(NULL)
using namespace std;
lli power(lli x, lli y)
{
    int res = 1;
    x = x %MOD;
    while (y > 0)
    {

        if (y & 1)
            res = (res*x) %MOD;


        y = y>>1;
        x = (x*x) %MOD;
    }
    return res;
}
int main() {
freopen("baths2.in","r",stdin);
freopen("baths2.out","w",stdout);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
   {
    lli n,n1,n2,k;
    cin>>n>>k;
    int flag=0;
    n1=n2=n;
    int temp=n;
    priority_queue<int> pq;
    pq.push(n);
    for(int j=1;j<=k;j++)
    {
    	temp=pq.top();
        n1=temp/2;
        n2=(temp-1)/2;
        pq.push(n1);
        pq.push(n2);
        pq.pop();

        }

    cout << "Case #" << i << ": " <<n1<<" "<<n2<<endl;

  }
  return 0;
}
