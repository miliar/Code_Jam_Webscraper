/**

**/
#include <bits/stdc++.h>
using namespace std;

#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test;
int R, O, Y, G, B, V, N, kq;
string ans;
bool check(string s) {
    int n = s.size() - 1;
    if (s[0] == 'Y')
        if (s[n] == 'Y' || s[n] == 'O' || s[n] == 'G') return false;
    if (s[0] == 'R')
        if (s[n] == 'R' || s[n] == 'O' || s[n] == 'V') return false;
    if (s[0] == 'B')
        if (s[n] == 'B' || s[n] == 'G' || s[n] == 'V') return false;
    if (s[0] == 'O')
        if (s[n] == 'O' || s[n] == 'R' || s[n] == 'Y') return false;
    if (s[0] == 'G')
        if (s[n] == 'G' || s[n] == 'Y' || s[n] == 'B') return false;
    if (s[0] == 'V')
        if (s[n] == 'V' || s[n] == 'R' || s[n] == 'B') return false;
    return true;
}
int duyet(string s, int i) {
    if (kq > 0) return 0;
    if (i == N - 1) {
        if (!check(s)) return 0;
        kq = 1;
        ans = s;
        return 0;
    }
    if (s[i] == 'R') {
        R--;
        if (G > 0) duyet(s + "G", i + 1);
        else if (B > Y && B > 0) duyet(s + "B", i + 1);
        else if (Y > 0) duyet(s + "Y", i + 1);
        R++;
    }
    if (s[i] == 'Y') {
        Y--;
        if (V > 0) duyet(s + "V", i + 1);
        else if (R > B && R > 0) duyet(s + "R", i + 1);
        else if (R > 0) duyet(s + "B", i + 1);
        Y++;
    }
    if (s[i] == 'B') {
        B--;
        if (O > 0) duyet(s + "O", i + 1);
        else if (R > Y && R > 0) duyet(s + "R", i + 1);
        else if (Y > 0) duyet(s + "Y", i + 1);
        B++;
    }
    if (s[i] == 'O') {
        O--;
        if (B > 0) duyet(s + "B", i + 1);
        O++;
    }
    if (s[i] == 'G') {
        G--;
        if (R > 0) duyet(s + "R", i + 1);
        G++;
    }
    if (s[i]== 'V') {
        V--;
        if (Y > 0) duyet(s + "Y", i + 1);
        V++;
    }
}
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        kq = -1;
        if (G > 0) duyet("G", 0);
        if (O > 0) duyet("O", 0);
        if (R > 0) duyet("R", 0);
        if (Y > 0) duyet("Y", 0);
        if (B > 0) duyet("B", 0);
        if (V > 0) duyet("V", 0);
        if (kq == -1) cout << "Case #" << te << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << te << ": " << ans << endl;
    }
}
int main() {
    freopen("main.in", "r", stdin);
    //freopen("main.in", "w", stdout);
    freopen("main.out", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
