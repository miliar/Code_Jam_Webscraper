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
int dp[11000][110];

int buy[1001];
int sit[1001];


int n, c, m;

int check(int train) {
    int i, tmp(0);
    for (i = 1000; i > 0; i--) {
        tmp += sit[i]-train;
        if (tmp < 0) tmp = 0;
    }
    return tmp;
}

int promote(int train) {
    int i, tmp(0);
    for (i = 1000; i > 0 ; i--) {
        if (sit[i] > train) {
            tmp += sit[i] - train;
        }
    }
    return tmp;
}

void proc(int t) {
    int i;
    memset(buy, 0, sizeof(buy));
    memset(sit, 0, sizeof(sit));
    cin >> n >> c >> m;
    rep(i, m) {
        int per, pos;
        cin >> pos >> per;
        buy[per]++;
        sit[pos]++;
    }
    int train = 0;
    // rep(i, 1001) {
    //     if (sit[i] !=0 ) cout << sit[i] << endl;
    // }
    rep(i, 1001) {
        train = max(train, buy[i]);
    }
    train = max(train, sit[1]);
    // cout << train << endl;
    while(check(train)!=0) {
        train++;
        // cout << train << endl;
    }
    int pro = promote(train);
    cout << "Case #" << t << ": " << train << ' ' << pro << endl;
}

int main() {
    int t, tt;
    cin >> t;
    xrep(tt, 1, t+1) {
        proc(tt);
    }
}
