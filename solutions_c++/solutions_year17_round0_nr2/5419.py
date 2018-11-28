#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

typedef pair<int, int> ii;

#define pb push_back
#define fi first
#define se second
#define sqr(x) ((x) * (x))

const char* fin = "quali17b.inp";
const char* fon = "quali17b.out";

#define oo (int) (1e9+7)
#define maxn (int) ()

long long n;

bool checkTidy(int n) {
    int tmp = 10;
    while (n) {
        if (n % 10 > tmp) return false;
        tmp = n % 10;
        n /= 10;
    }
    return true;
}

void buff() {
    for(int i = (int)n; i > 0; --i) {
        if (checkTidy(i)) {
            cout << i;
            return;
        }
    }
}

string toStr(long long n) {
    string tmp;
    while (n) {
        tmp = (char)(n % 10 + 48) + tmp;
        n /= 10;
    }
    return tmp;
}

string backtrack(string s) {
    string s1;
    for(int i = 0; i < s.size(); ++i) {
        s1 += s[i];
        if (i < s.size() - 1)
        if (s[i] > s[i + 1]) {
            s1[i] = s[i] - 1;
            s1 = backtrack(s1);
            return s1;
        }
    }
    return s;
}

void sol() {
    string s = toStr(n), s1;
    for(int i = 0; i < s.size(); ++i) s1 += s[0];
    if (s1 > s) {
        char tmp = s[0] - 1;
        s1.clear();
        if (tmp != '0') s1 += tmp;
        for(int i = 1; i < s.size(); ++i) s1 += '9';
    } else {
        s1.clear();
        for(int i = 0; i < s.size(); ++i) {
            s1 += s[i];
            if (i < s.size() - 1)
            if (s[i] > s[i + 1]) {
                s1[i] = s[i] - 1;
                s1 = backtrack(s1);
                break;
            }
        }
        while (s1.size() < s.size()) s1 += '9';
    }
    if (s1[0] == '0') s1.erase(0, 1);
    cout << s1;
}

void inp() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        cin >> n;
        //if (n <= 1000) buff(); else
            sol();
        cout << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    freopen(fin, "r", stdin);freopen(fon, "w", stdout);
    inp();
    return 0;
}
