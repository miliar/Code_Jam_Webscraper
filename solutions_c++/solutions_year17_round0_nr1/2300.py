#include<bits/stdc++.h>
#define two(a) (1<<(a))
#define LINF (1ll<<61)
#define EPS (1e-14)
#define Lshift(a,b) (a<<b)
#define Rshift(a,b) (a>>b)
#define rep(a,b) for(a=0 ; a<b ; a++)
#define xrep(a,b,c) for(a=b ; a<c ; a++)
#define INF (1<<29)
#define swap(a,b) ( (a^=b) , (b^=a) , (a^=b) )
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5]|=1<<(x&31))
#define maxL (10000000>>5)+1
#define mod 1000000007
typedef long long ll;
using namespace std;

void proc(int t) {
    char line[2000];
    int result = 0;
    int n, i, j;
    scanf("%s%d",line, & n);
    rep(i, strlen(line)-n+1) {
        if (line[i] == '-') {
            result += 1;
            rep(j, n) {
                int k = i+j;
                if (line[k] == '-') line[k] = '+';
                else line[k] = '-';
            }
        }
    }
    cout << "Case #" << t << ": ";
    rep(i, strlen(line)) {
        if (line[i] != '+') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << result << endl;
}


int main() {
    int T, t;
    scanf("%d", &T);
    xrep(t, 1, T+1) {
        proc(t);
    }
}
