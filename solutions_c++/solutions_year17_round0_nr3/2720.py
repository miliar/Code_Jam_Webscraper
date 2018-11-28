#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstdarg>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

#if __cplusplus > 199711L
    void read(){}
    template<typename... T>
    void read(int& head, T&... tail) {scanf("%d",&head); read(tail...);}

    #define DB(args...) { cerr << __LINE__<< ": "; vector<string> _v = split(#args, ','); err(_v.begin(), args); }
    vector<string> split(const string& s, char c) {
        vector<string> v;stringstream ss(s);string x;
        while (getline(ss, x, c)) v.push_back(x);
        return move(v);
    }
    void err(vector<string>::iterator it) {cerr<<endl;}
    template<typename T, typename... Args>
    void err(vector<string>::iterator it, T a, Args... args) {
        cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << "  "; err(++it, args...);
    }
#else
    #define DB(e) cerr << __LINE__ << ": " << #e << " = " << e << endl;
    void read(int& head) {scanf("%d",&head);}
#endif

#define ll long long int
#define pb push_back
#define fr(i,n)     for(int i=0;i<n;i++)
#define init(mem,v) memset(mem,v,sizeof(mem))
typedef pair <int,int> pii;
typedef pair <ll, ll> pll;

pll handle(ll n, ll k){
    map<ll,ll> pq;
    pq[n]=1;

    --k;
    while(k>0){
        auto nxt=pq.rbegin();
        ll c=nxt->first;
        ll w=nxt->second;
        ll sub=min(k,w);
        k-=sub;

        if(sub==w){
            pq.erase(c);
        }
        else{
            pq[c]=w-sub;
        }

        --c;
        pq[c/2]+=w;
        pq[(c+1)/2]+=w;
    }

    auto x=pq.rbegin();
    auto c=x->first;
    --c;

    return {(c+1)/2,c/2};
}

int main(){
    int t;
    read(t);

    fr(ii,t){
        ll n,k;
        scanf("%lld %lld",&n,&k);

        auto r = handle(n,k);
        printf("Case #%d: %lld %lld\n",ii+1,r.first, r.second);
    }
}
