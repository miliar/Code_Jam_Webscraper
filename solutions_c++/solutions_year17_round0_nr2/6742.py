#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

ull func(ull in) {
    if(in < 10) return in;
    ull tmp=10;
    while(tmp*10 < in) tmp *=10;
    int top = in/tmp;
    ull mod = in%tmp;
    ull d = func(mod);
    int dt = d/(tmp/10);
    if(top<=dt) return top * tmp + d;
    else return (top-1)*tmp + tmp-1;
}

int main()
{
    int T;
    cin >> T;

    rep(cnum, T) {
        ull in;
        cin >> in;
        ull ans = func(in);
        cout << "Case #" << cnum+1 << ": " << ans << endl;
    }
    return 0;
}
