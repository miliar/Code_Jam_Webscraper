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
#define repr(i,x,y) for (int i=(y);i>=(x);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;

string a, b;

void MAIN(){
    cin >> a;
    int n = a.size();
    bool ck = false;
    rep2(i, 0, n-1){
        b=a;
        rep2(j, i+1, n-1) b[j] = a[i];
        if (b>a){
            ck = true;
            rep2(j, 0, i-1) cout << a[j];
            if (i>0 || a[i] > '1') cout << a[i] - '0' - 1;
            rep2(j, i+1, n-1) cout << '9';
            cout << endl;
            break;
        }
    }
    if (!ck){
        cout << a << endl;
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