#include <bits/stdc++.h>

using namespace std;
vector<int> digits;
int N, test;
long long n, x[20], ans;

void Update(){
    long long temp = 0;
    for(int i = 1; i <= N; i++) temp = temp * 10 + x[i];
    ans = max(ans, temp);
}

void Back(int i, bool ok) {
    if (ok) {
        x[i] = 9;
        if (i == N) Update();
        else Back(i + 1, ok);
    }
    else {
        for(int j = x[i-1]; j <= digits[i-1]; j++) {
            x[i] = j;
            if (i == N) Update();
            else {
                if (j < digits[i-1]) Back(i+1, true);
                else Back(i + 1, false);
            }
        }
    }
}

void Solve(long long u) {
    digits.clear();
    long long res = 0;
    ans = 0;
    while (u) {
        digits.push_back(u % 10);
        u /= 10;
    }
    reverse(digits.begin(), digits.end());
    for(int i = 1; i < digits.size(); i++)
        res = res * 10 + 9;
    N = digits.size();
    Back(1, false);
    cout << max(ans, res);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    x[0] = 0;
    cin >> test;
    for(int i = 1; i <= test; i++) {
        cin >> n;
        cout << "Case #" << i <<": ";
        Solve(n);
        if (i != test) cout << endl;
    }
    fclose(stdin);
    fclose(stdout);
}
