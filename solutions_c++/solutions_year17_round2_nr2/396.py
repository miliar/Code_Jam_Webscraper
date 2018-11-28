#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int n;
int v[7];
char pr[7] = {'X', 'R', 'Y', 'O', 'B', 'V', 'G'};

void small() {
    vector<int> p = {1,2,4};
    sort(p.begin(), p.end(), [](int a, int b){return v[a] > v[b];});

    if (v[p[0]] > v[p[1]] + v[p[2]]) {
        printf("IMPOSSIBLE\n");
        return;
    }

    while (v[p[1]] > v[p[2]]) {
        printf("%c%c", pr[p[0]], pr[p[1]]);
        v[p[0]]--; v[p[1]]--;
    }

    while (v[p[0]] > v[p[1]]) {
        printf("%c%c%c%c", pr[p[0]], pr[p[1]], pr[p[0]], pr[p[2]]);
        v[p[0]]-=2; v[p[1]]--; v[p[2]]--;
    }

    while (v[p[0]] > 0) {
        printf("%c%c%c", pr[p[0]], pr[p[1]], pr[p[2]]);
        v[p[0]]--; v[p[1]]--; v[p[2]]--;
    }

    while (v[p[1]] > 0) {
        printf("%c%c", pr[p[1]], pr[p[2]]);
        v[p[1]]--; v[p[2]]--;
    }

    printf("\n");
}

int main()
{
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        memset(v, 0, sizeof(v));
        printf("Case #%d: ", t);

        scanf("%d", &n);
        scanf("%d %d %d %d %d %d", v+1, v+3, v+2, v+6, v+4, v+5);

        small();
    }
}
