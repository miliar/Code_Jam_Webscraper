/***********************TUFAAN***********************/
#include<bits/stdc++.h>
#define pi acos(-1.0)
#define pb push_back
#define LL long long
#define LIM 100000
using namespace std;
int _I(){int x; scanf("%d",&x); return x;}
LL _L(){LL x; scanf("%lld",&x); return x;}
LL gcd(LL x,LL y){if(x%y==0) return y; else return gcd(y,x%y);}
LL lcm(LL x,LL y){x/=gcd(x,y); return x*y;}
int kdx[8]={-2,-2,-1,-1,1,1,2,2};
int kdy[8]={-1,1,-2,2,-2,2,-1,1};
bool prime[2];
vector<int> v;
map<int, int> mp;
void sieve(){
    int i,j; prime[1]=1; v.pb(2);
    for(i=4;i<=LIM;i+=2) prime[i]=1;
    for(i=3;i<=LIM;i+=2) if(!prime[i]){ v.pb(i); for(j=i+i+i;j<=LIM;j+=i+i) prime[j]=1;}
}
int cases;
void lipu_mira(){
        int i,j,k,l,ans = 0;
        string a;
        bool flag = 0;
        cin>>a;
        k = _I();
        l = a.size();
        int c = 0;
        while(c < l){
                if(a[c] == '-'){
                        ans++;
                        c++;
                        if((c-1 + k) > l){
                                flag = 1;
                                break;
                        }
                        for(i = c-1; i < k+c-1; i++){
                               if(a[i] == '-') a[i] = '+';
                               else a[i] = '-';
                        }
                }
                else {
                        c++;
                        continue;
                }
        }
        if(flag) printf("Case #%d: IMPOSSIBLE\n",++cases);
        else printf("Case #%d: %d\n",++cases,ans);
}
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.out", "w", stdout);
    //sieve();
    int t = _I();
    while(t--)
        lipu_mira();
    return 0;
}
