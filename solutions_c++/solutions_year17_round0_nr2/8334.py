#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pi acos(-1)
#define MOD 10000007
#define M 1000009
#define INF 1000000000000000001
#define inf 1000000001
#define mp make_pair
#define pb push_back
#define mem(a, b) memset(a, b, sizeof(a))
#define read(f) freopen(f, "r", stdin);
#define write(f) freopen(f, "w", stdout)

int dx8[] = {-1, 0, +1, -1, +1, -1, 0, +1};
int dy8[] = {+1, +1, +1, 0, 0, -1, -1, -1};
int dx4[] = { 0,-1,+1, 0};
int dy4[] = {+1,+1, 0,-1};
int dxkn[] = {1, -1, 1, -1, 2, -2, -2, 2};
int dykn[] = {2, 2, -2, -2, 1, 1, -1, -1};

ll bigmod(ll b, ll p, ll m) {
    if(p == 0) return 1%m;
    else if(p&1) return (((b%m)*bigmod(b, p - 1, m))%m);
    else {
        ll ret = bigmod(b, (p/2), m);
        return ret*ret;
    }
}

ll power(ll b, ll p) {
    if(p == 0) return 1;
    else if(p == 1) return b;
    else if(p&1) return b*power(b, p - 1);
    else {
        ll ret = power(b, (p/2));
        return ret*ret;
    }
}




int main() {
    //read("b.txt");
    //write("boutlarge.txt");
    vector <long long> a, b;
    long long t, tc, num, i, ans, n, d, sz, pos, flag, ss;
    scanf("%lld", &tc);
    for(t = 1; t <= tc; t++) {
        scanf("%lld", &n);
        ss = n;
        a.clear();
        while(n) {
            d = n%10;
            a.pb(d);
            n /= 10;
        }
        reverse(a.begin(), a.end());
        sz = a.size();
        for(int k = 1; k <= 20; k++) {
            for(i = 1, flag = 0; i < sz; i++) {
                if(a[i] < a[i - 1]) {
                    pos = i;
                    flag = 1;
                    break;
                }
            }

            if(flag) {
                for(i = pos; i < sz; i++) {
                    a[i] = 9;
                }
                if(a[pos - 1] == 1 && pos - 1 == 0) {
                    a[pos - 1] = -1;
                }
                else {
                    a[pos - 1]--;
                }
            }
            b.clear();
            for(i = 0; i < sz; i++) {
                if(a[i] >= 0) {
                    b.pb(a[i]);
                }
            }
            a.clear();
            sz = b.size();
            for(i = 0; i < sz; i++){
                a.pb(b[i]);
            }
        }

        printf("Case #%lld: ", t);
        if(ss == 0) printf("0");
        for(i = 0; i < sz; i++) {
            if(a[i] >= 0) {
                printf("%lld", a[i]);
            }
        }
        printf("\n");
    }
    return 0;
}


