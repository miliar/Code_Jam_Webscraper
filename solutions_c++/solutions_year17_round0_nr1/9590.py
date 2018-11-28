#include <cstdio>
#include <vector>

using namespace std;

void solve(int t) {
    char ch;
    vector<int> v;

    do {
        scanf("%c", &ch);

        if (ch == '+')
            v.push_back(1);
        else if (ch == '-')
            v.push_back(-1);
    } while (ch != ' ');

    int k;
    scanf("%d", &k);

    int ans = 0;
    for (int i = 0; i < v.size() - k + 1; i++) {
        if (v[i] == -1) {
            ans++;
            for (int j = i; j < i + k; j++)
                v[j] *= -1;
        }
    }

    bool ok = true;
    for (int i = v.size() - k + 1; i < v.size(); i++) {
        if (v[i] < 1) {
            ok = false;
            break;
        }
    }

    if (ok) {
        printf("Case #%d: %d\n", t, ans);
    } else {
        printf("Case #%d: IMPOSSIBLE\n", t);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int it = 0; it < T; it++) {
        solve(it+1);
    }
    return 0;
}
