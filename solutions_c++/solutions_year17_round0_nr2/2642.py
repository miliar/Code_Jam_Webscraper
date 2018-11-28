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
typedef pair<int,int> pii;

ll last_tidy(ll n);

void test(){
    for(int i=1;i<10;i++) assert(last_tidy(i)==i);

    assert(last_tidy(10) == 9);
    assert(last_tidy(21) == 19);
    assert(last_tidy(1000000000000000000LL) == 999999999999999999LL);
    assert(last_tidy(1002222200777700111LL) == 999999999999999999LL);
    assert(last_tidy(2233322999) == 2229999999);
}

ll last_tidy(ll n){
    char d[20];
    sprintf(d,"%lld",n);

    int l=strlen(d);

    int bp=-1;
    fr(i,l-1){
        if(d[i]>d[i+1]){
            bp=i;
            break;
        }
    }
    if(bp>=0){
        while(bp>0 and d[bp-1]==d[bp]) bp--;
        d[bp]--;
        bp++;
        while(1){
            d[bp]='9';
            bp++;
            if(bp>=l) break;
        }
    }

    ll m=0;
    fr(i,l) m=10*m+(d[i]-'0');
    return m;
}

int main(){
    int t;
    ll n;
    read(t);
    fr(ii,t){
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",ii+1,last_tidy(n));
    }
}
