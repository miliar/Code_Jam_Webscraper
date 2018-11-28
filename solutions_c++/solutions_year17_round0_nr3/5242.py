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

map<LL,int> m;
priority_queue<LL>v;
LL n,k,num;
int main(){

    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;scanf("%d",&T);int cas = 0;
while(T--){cas ++;
    while(!v.empty())v.pop();
    m.clear();
    LL now = 0;
    num = 0;
    cin>>n>>k;
    v.push(n);
    m[n] = 1;
    while(!v.empty()){
        now = v.top();
        num+=m[now];
        if(num>=k){now = v.top();break;}
        if(now%2){
            if(now!=1){
                if(m.find((now-1)/2)==m.end()){
                    v.push((now-1)/2);
                    m[(now-1)/2] = 0;
                }
                m[(now-1)/2]+=2*m[now];
            }
        }else{
            if(m.find((now)/2)==m.end()){
                    v.push((now)/2);
                    m[(now)/2] = 0;
                }
            if(m.find((now)/2 -1)==m.end() && now!=2){
                    v.push((now)/2 -1);
                    m[(now)/2 -1] = 0;
                }
            m[now/2] += m[now];
            if(now!=2)m[now/2-1] += m[now];
        }
        v.pop();
    }
    cout<<"Case #"<<cas<<": ";
    if(now%2 == 0){
        cout<<now/2<<' '<<now/2-1<<endl;
    }else{
        now-=1;
        cout<<now/2<<' '<<now/2<<endl;
    }
}
	return 0;
}
