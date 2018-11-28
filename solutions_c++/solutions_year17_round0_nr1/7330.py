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

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int x,y,z;
    string S;
    cin>>x;
    f(i,x){
        cin>>S>>y;
        z=0;
        f(j, S.size()){
            if((S.size()-j)<y && S[j]=='-'){
                z=-1;
                break;
            } else if(S[j]=='-'){
                z++;
                f(k,y){
                    if(S[j+k]=='-'){
                        S[j+k]='+';
                    } else {
                        S[j+k]='-';
                    }
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(z==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<z<<endl;
    }
    return 0;
}
