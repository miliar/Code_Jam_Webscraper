#include <bits/stdc++.h>

using namespace std;

const int N = 20;

int a[N];
long long pw[N];
int ok[N][11][2];
int cant[N][N][N];
long long f[N][11][2];

long long calc(int i, int last, int fine){
    if(i > 18){
        return 0;
    }
    if(ok[i][last][fine] == 1){
        return f[i][last][fine];
    }
    int able = 9;
    if(fine == 1){
        able = a[i];
    }
    f[i][last][fine] = -1000000000000000000;
    for(int x = last; x <= able; ++x){
        f[i][last][fine] = max(f[i][last][fine], 1LL * x * pw[18 - i] + calc(i + 1, x, fine && (x == able)));
    }
    return f[i][last][fine];
}

int main(){
    freopen("1.inp", "r", stdin);
    freopen("1.out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    pw[0] = 1;
    for(int i = 1; i <= 18; ++i){
        pw[i] = pw[i - 1] * 10;
    }
    for(int iTest = 1; iTest <= tt; ++iTest){
        string x;
        cin >> x;
        reverse(x.begin(), x.end());
        memset(a, 0, sizeof a);
        for(int i = 0; i < x.size(); ++i){
            a[18 - i] = x[i] - '0';
        }
        memset(ok, 0, sizeof ok);
        cout << "Case #" << iTest << ": " << calc(1, 0, 1) << endl;
    }
    return 0;
}
