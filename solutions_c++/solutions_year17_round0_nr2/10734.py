/**********************************************************/
/**            Bismillahir-rahmanir-rahim                **/
/**  In the name of Allah, the Beneficent, the Merciful. **/
/**********************************************************/
/*author: Sayed Sohan, CSE 13th batch(2016), MBSTU*/
/**status : */

#include <bits/stdc++.h>
using namespace std;
typedef long long  ll;
typedef unsigned long long ull;
#define FOR(i,x,n) for(i=(x);i<(n);i++)
#define IFOR(i,n,x) for(i=(n-1);i>=(x);i--)
#define clr(arr,value) memset(arr,value,sizeof(arr))
#define MOD 1000000007
#define MAX 100000/** can increase another 0 */
#define PI acos(-1)
#define DIF if(0)

bool func(ll n)
{
    ll x = 10;
    while(n!=0){
       ll z = n%10;
       if(z<=x){
         x = z;
         n/=10;
       }
       else return false;
    }
    return true;
}

int main()
{
    ll i,j,k,arr[MAX],l,m,n,x,coun,sum,ans,T,check;
    char str[MAX];
    string s;
    vector<ll> v;
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    cin>>T;
    ll c = 1;
    while(T--){
        cin>>n;
        while(n){
            bool xx = func(n);
            if(xx==true){
                printf("Case #%lld: %lld\n",c++,n);
                break;
            }
            //cout<<n<<endl;
            n--;
        }
    }

    return 0;
}
