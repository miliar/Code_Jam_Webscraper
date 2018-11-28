#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair< int, int > pii;
typedef pair< ll, ll > pll;

#define ALL(x) (x).begin(), (x).end()
#define vec vector

int const inf = 1000 * 1000 * 1000;
ll const inf64 = 1ll * inf * inf;

int f(vec< int > a) {
    int res = 0;
    int cur = 0;
    for(int x : a) {
        if(cur == 0) {
            res++;
        }
        cur = (cur + x) % 4;
    }
    return res;
}

int get(int cnt3) {
    int res = 0;
    for(int x = 0;x <= cnt3;x++) {
        vec< int > arr;
        for(int i = 0;i < x;i++) arr.push_back(3);
        arr.push_back(2);
        for(int i = 0;i < cnt3 - x;i++) arr.push_back(3);
        res = max(res, f(arr));
    }
    return res;
}

int simple(int p, vec< int > arr) {
    sort(ALL(arr));
    int res = 0;
    do{
        int tmp = 0;
        int cur = 0;
        for(int x : arr) {
            if(cur == 0) {
                tmp++;
            }
            cur = (cur + x) % p;
        }
        res = max(res, tmp);
    }while(next_permutation(ALL(arr)));
    return res;
}

int fast(int p, vec< int > arr) {
    vec< int > cnt(p);
    for(int x : arr) {
        cnt[x % p]++;
    }
    int res;
    if(p == 2) {
        res = cnt[0] + (cnt[1] + 1) / 2;
    }else if(p == 3) {
        res = cnt[0];
        int mn = min(cnt[1], cnt[2]);
        res += mn;
        cnt[1] -= mn;
        cnt[2] -= mn;
        if(cnt[1] > 0) {
            res += (cnt[1] + 2) / 3;
        }else if(cnt[2] > 0) {
            int cur = 0;
            while(cnt[2] > 0) {
                if(cur == 0) {
                    res++;
                }
                cnt[2]--;
                cur = (cur + 1) % 3;
            }
        }
    }else { // p == 4
        res = cnt[0];
        res += cnt[2] / 2;
        cnt[2] %= 2;
        int mn = min(cnt[1], cnt[3]);
        res += mn;
        cnt[1] -= mn;
        cnt[3] -= mn;
        if(cnt[2] == 0) {
            if(cnt[1] > 0) {
                res += (cnt[1] + 3) / 4;
            }else if(cnt[3] > 0) {
                int cur = 0;
                while(cnt[3] > 0) {
                    if(cur == 0) {
                        res++;
                    }
                    cnt[3]--;
                    cur = (cur + 1) % 4;
                }
            }
        }else {
            if(cnt[1] > 0) {
                if(cnt[1] == 1) {
                    res++;
                }else if(cnt[1] == 2) {
                    res++;
                }else {
                    res++;
                    cnt[1] -= 2;
                    res += (cnt[1] + 3) / 4;
                }
            }else if(cnt[3] > 0) {
                res += get(cnt[3]);
            }else {
                res++;
            }
        }
    }
    return res;
}

void solve() {
    int n, p;
    cin >> n >> p;
    vec< int > arr(n);
    for(int i = 0;i < n;i++) {
        cin >> arr[i];
    }
    cout << fast(p, arr) << "\n";
}

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testNumber;

    scanf("%d", &testNumber);

    for(int test = 1;test <= testNumber;test++) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
