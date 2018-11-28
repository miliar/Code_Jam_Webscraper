#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb(x) push_back(x);
#define p(x)    push(x);
#define mp(x, y) make_pair(x, y);
#define f(i,s,n)  for(ll i=s;i<n;++i);
typedef vector< vector<ll> > matrix;
#define inp(x)  scanf("%d",&x);
#define inp( n, x, y)  scanf("%d %d %d",&n, &x, &y);
/*vector <ll> newprime;
void sieve(ll n) {
    ll prime[n]={0};
    //memset(prime, 0, sizeof(prime[n]));
    prime[1] = 1;
    prime[0] = 1;
    for (ll i = 2; i <= n; i++) {
        if (prime[i] == 0) {
            for (ll j = i; i * j <= n; j++) prime[i * j] = 1;
        }
    }
    for (ll i = 2; i <= n; i++) {
        if (prime[i] == 0) {
            newprime.pb(i);
        }
    }
    //for (int i = 0; i < newprime.size(); i++) cout << newprime[i] << " ";
}*/
//xor!=0 first player win
//xor ==0 second player wins

int main() {
    int t,h=1;
    cin>>t;
    while(t--){
        cout<<"Case #"<<h<<": ";
        char s[1001];
        int n , ans=0, flag=0;
        cin>>s>>n;
        //cout<<strlen(s)-n;
        for(int i=0;i<=strlen(s)-n;++i){
            if(s[i]=='-'){
                for(int j=i;j<i+n;++j){
                    if(s[j]=='-')   s[j]='+';
                    else s[j]='-';
                }
               /* cout<<i<<endl;
                for(int j=i;j<i+n;++j)  cout<<s[j];
                cout<<endl;*/
                ++ans;
            }

        }
        for(int i=0;i<strlen(s);++i)    {
            //cout<<s[i];
            if(s[i]=='-')   {
                flag=1;
            }
        }
        if(flag==1) cout<<"IMPOSSIBLE\n" ;
        else cout<<ans<<endl;
        ++h;
    }
    return 0;
}
