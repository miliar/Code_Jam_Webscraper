#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <queue>
#include <iomanip>

using namespace std;
#define eps 1e-7
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define ft first
#define sd second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef queue<int> QI;
typedef pair<long double,long double>PDD;

const LL mod=1000000007;
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head

int n,k;
PDD a[2333];
long double f[2333][2333];

bool cmp(PDD x,PDD y){
    return x.ft * x.sd > y.ft * y.sd;
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int cas = 1;
int T;cin>>T;while(T--){
    cin>>n>>k;
    rep(i,0,n+2)rep(j,0,n+2)f[i][j] = 0.0;
    rep(i,0,n)cin>>a[i].ft>>a[i].sd;
    sort(a,a+n,cmp);
    long double ans = 0.0;

    rep(i,0,n){
        int num = 1;
        long double cur = a[i].ft * a[i].ft + 2 * a[i].ft * a[i].sd;
        rep(j,0,n){
            if(j == i)continue;
            if(num == k)break;
            if(a[j].ft<=a[i].ft){
                num ++;
                cur += 2 * a[j].sd * a[j].ft;
            }
        }
        if (num!=k)continue;
        ans = max(ans,cur);
    }
    ans = ans * acos(-1.0);
    cout<<"Case #"<<cas++<<": ";
    printf("%.8lf",ans);
    cout<<endl;
}
	return 0;
}
