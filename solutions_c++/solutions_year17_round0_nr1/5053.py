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

using namespace std;
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

const LL mod=1000000007;
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head

string s;
int k;

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
int T, cas = 0;scanf("%d",&T);while(T--){
    cas++;
    cin>>s>>k;int ans = 0;bool flag = true;
    int l = s.length();
    rep(i,0,l-k+1){
        if(s[i] == '-'){
            //cout<<"!!!"<<i<<endl;
            ans++;
            rep(j,i,i+k){
                if(s[j] == '+')s[j] = '-';
                else s[j] = '+';
            }
        }
    }
    rep(i,0,l)if(s[i] == '-')flag = false;
    cout<<"Case #"<<cas<<": ";
    if(flag){
        cout<<ans<<endl;
    }else{
        cout<<"IMPOSSIBLE"<<endl;
    }
}
	return 0;
}
