#include <bits/stdc++.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()
#define pb push_back
#define MOD 1000000007

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;

ll pw(ll b,int p, int m){
    ll a=1;
    while(p){
        if(p&1)
            a=(a*b)%m;
        b=(b*b)%m;
        p>>=1;
    }
    return a;
}

ll gcd(ll a, ll b){
    if(a<b)
        swap(a,b);
    if(!b)
        return a;
    return gcd(b,a%b);
}

ull reduce(ull n){
    ull x=n;
    int size=0, a[20];
    while(x) {
        a[size++] = x%10;
        x /= 10;
    }
    for(int j=size-1;j>0;j--){
        if(a[j]>a[j-1]) {
            x = pow(10, j);
            return reduce((n/x)*x-1);
        }
    }
    return n;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int t,size;
    ull n,x;
    cin>>t;
    f(i,t){
        cout<<"Case #"<<i+1<<": ";
        cin>>n;
        cout<<reduce(n)<<endl;
    }
    return 0;
}
