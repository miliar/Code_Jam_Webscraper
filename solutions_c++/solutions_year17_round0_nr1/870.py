#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

#define rep(i,n) for (int i=1;i<=(n);++i)
#define rep2(i,x,y) for (int i=(x);i<=(y);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;

string a;

int n,m;

bool b[10000];

void MAIN(){
    cin >> a >> m;
    n = a.size();
    rep2(i,0,n) b[i]=false;
    bool cur = false;
    bool ck = true;
    int cnt = 0;
    rep2(i,0,n-1){
        cur ^= b[i];
        if ((a[i]=='-') ^ cur) {
            if (i>n-m)
                ck = false;
            else{
                cnt += 1;
                cur ^= 1;
                b[i+m] = true;
            }
        }
    }
    if (ck){
        cout << cnt << endl;
    }else{
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    // freopen("d:\\oi\\gcjr3\\A-large (1).in","r",stdin);
    // freopen("d:\\oi\\gcjr3\\A-large (1).out","w",stdout);
    int tt;
    cin >> tt;
    rep(i,tt)
    {
        printf("Case #%d: ",i);
        MAIN();
    }    
    return 0;
}