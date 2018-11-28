#include <bits/stdc++.h>
using namespace std;

#define fi          "input.txt"
#define fo          "output.txt"
#define fileopen    freopen(fi,"r",stdin);freopen(fo,"w",stdout)
#define FOR(i,l,r)  for(int i=(int)(l);i<=(int)(r);i++)
#define FORD(i,l,r) for(int i=(int)(l);i>=(int)(r);i--)
#define xy          pair<int64,int>
#define int64       long long
#define ld          long double
#define X           first
#define Y           second
#define pb          push_back
#define init(a,v)   memset(a,v,sizeof(a))
#define Sz(s)       (int)(s.size())
#define EL          cout<<endl
#define digit(x)    ('0'<=x&&x<='9')
#define forever     while (true)
#define ran(l,r)    ((1LL*rand()*rand())%((int)(r)-(int)(l)+1)+(int)(l))

const int OO = (int) 2e9+5;
const int MOD = (int) 1e9+7;
const long double Pi = 3.141592653589793238;
const int N = (int) 1e3+5;

map<pair<int64,int>,int64> mp;
int64 n,k;

void add(int64 len,int64 cnt) {
    mp[make_pair(len+len%2,-len%2)]+= cnt;
}

pair<int64,int64> pop() {
    pair<pair<int64,int>,int64> top = *(mp.rbegin());
    int64 len = top.X.X + top.X.Y;
    int64 cnt = top.Y;
    mp.erase(top.X);
    return make_pair(len,cnt);
}

pair<int64, int64> solve() {
    cin>>n>>k;
    mp.clear();
    add(n,1);
    int64 last_l = 0;
    while (k>0) {
        pair<int64,int64> get = pop();
        int64 len = get.X;
        int64 cnt = get.Y;
        if (k<=cnt) {
            last_l = len;
            break;
        } else {
            k-=cnt;
            if (len%2==0) {
                add(len/2-1,cnt);
                add(len/2,cnt);
            } else {
                add(len/2,2*cnt);
            }
        }
    }
    pair<int64,int64> res;
    res.X = last_l/2;
    res.Y = last_l-last_l/2-1;
    return res;
}

int main() {
    fileopen;
    int T;
    cin>>T;
    FOR(_,1,T) {
        pair<int64,int64> res = solve();
        cout<<"Case #"<<_<<": "<<res.X<<" "<<res.Y<<endl;
    }
}
