#include <bits/stdc++.h>

#define F first
#define S second
#define x1 privet1
#define x2 privet2
#define y1 privet3
#define y2 privet4
#define left privet6

using namespace std;
typedef long long ll;

const long long max_n = 100011, log_n = 32, max_m = 111, mod = 1000000007, inf = 1011111111111111111LL, p = 1009, p2 = 997;

ll z, n;
vector<int> v;

void get_v() {
    ll nn = n;
    while (nn) {
        v.push_back(nn % 10);
        nn /= 10;
    }
    reverse(v.begin(), v.end());
}

void get_res() {
    int k = 0;
    for (int i = 1; i < v.size(); ++i) {
        if (v[i] < v[i - 1]) {
            k = i;
            break;
        }
    }
    if (k == 0) {
        for (int i = 0; i < v.size(); ++i) {
            cout << v[i];
        }
        return;
    }
    int cnt = 1;
    for (int i = k - 2; i >= 0 && v[i] == v[i + 1]; --i) {
        cnt++;
    }
    for (int i = 0; i < k - cnt; ++i) {
        cout << v[i];
    }
    if (k == cnt && v[0] == 1) {
        for (int i = 1; i < v.size(); ++i) {
            cout << "9";
        }
        return;
    }
    cout << v[k - 1] - 1;
    for (int i = k - cnt + 1; i < v.size(); ++i) {
        cout << "9";
    }
}

ll get_res1(ll a) {
    while (a) {
        int lst = 10;
        ll b = a;
        bool fl = 0;
        while (b) {
            if (lst < b % 10) {
                fl = 1;
                break;
            }
            lst = b % 10;
            b /= 10;
        }
        if (!fl) {
            return a;
        }
        a--;
    }
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> z;
    int zz = z;
    while (z--) {
        cin >> n;
        get_v();
        cout << "Case #" << zz - z << ": ";
        get_res();
        //cout << endl << "Case #" << zz - z << ": ";
        //cout << get_res1(n);
        cout << endl;
        v.clear();
    }
    return 0;
}
