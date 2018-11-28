#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int t;
ll n;
ll cnt[30][20];            // ile cyfr, jaka pierwsza

bool tidy(ll x) {
    vector<int> digits;
    while(x) {
        digits.push_back(x % 10);
        x /= 10;
    }

    for(int i = 0 ; i < int(digits.size()) - 1; i++)
        if(digits[i] < digits[i + 1])
            return false;

    return true;
}

ll ile_do2(ll x) {
    ll res = 0;
    for(ll i = 1 ; i <= x ; i++)
        if(tidy(i))
            res++;
    return res;
}

ll ile_do(ll x) {
    ll cp = x;
    stack<int> digits;
    while(x) {
        digits.push(x % 10);
        x /= 10;
    }

    int last = 0;
    ll c = 0;
    while(!digits.empty()) {
        int dig = digits.top();
        digits.pop();

        if(last > dig)
            break;

        for(int i = last ; i < dig ; i++)
            c += cnt[digits.size() + 1][i];

        last = dig;
    }

    if(tidy(cp))
        c++;

    return c;
}

int main() {
    for(int i = 1 ; i < 10 ; i++)
        cnt[1][i] = 1;

    for(int cyfr = 2 ; cyfr <= 19 ; cyfr++)
        for(int i = 0 ; i < 10 ; i++)
            for(int j = i ; j < 10 ; j++)
                cnt[cyfr][i] += cnt[cyfr - 1][j];

    int t;
    scanf("%d", &t);
    for(int c = 1 ; c <= t ; c++) {
        scanf("%lld", &n);

        ll pocz = 1, kon = n, mid;
        ll to_find = ile_do(n);

        while(pocz < kon) {
            mid = (pocz + kon) / 2;
            if(ile_do(mid) < to_find)
                pocz = mid + 1;
            else
                kon = mid;
        }

        printf("Case #%d: %lld\n", c, pocz);
    }

    return 0;
}
