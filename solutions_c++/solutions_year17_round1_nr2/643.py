#include <bits/stdc++.h>
using namespace std;
bool used[1000][1000];

bool Fits(double a, double b, double c, double d) {
    int f1 = a/b;
    int f2 = c/d+1;
    if(f1 > f2)swap(f1, f2);
    for(int i = f1; i <= f2; i++) {
        int f = i;
        if(0.9 *(double)f * b - a <= 0.1 and 1.1 *(double)f * b - a >= -0.1) {
            if(0.9 *(double)f * d  - c <=  0.1 and 1.1 *(double)f * d - c >= -0.1) { return true; }
        }
    }
    return false;
}
int ing[1000];
int pack[1000][1000];
void Solve(int testNum) {
    int n, p;
    scanf("%d %d", &n, &p);
    for(int i = 0; i < n; i++) scanf("%d", &ing[i]);
    for(int i = 0; i < n; i++)
        for(int j = 0; j < p; j++) scanf("%d", &pack[i][j]), used[i][j] = false;
    for(int i = 0; i < n; i++) sort(pack[i], pack[i]+p);

    int ans = 0;
    for(int j = 0; j < p; j++) {
        vector< pair<int, int> > cur;
        cur.push_back(make_pair(0, j));
        for(int i = 1; i < n; i++)
            for(int q = 0; q < p; q++) {
                if(Fits(pack[0][j] , ing[0], pack[i][q] ,ing[i]) and !used[i][q]) { cur.push_back(make_pair(i, q)); break;}
        }
        if(cur.size() == n) {
            for(int i = 0; i < n; i++) used[cur[i].first][cur[i].second] = true;
            ans++;
        }
    }
    if(n == 1) {
        ans = 0;


        for(int i = 0; i < p; i++)
            if(Fits(pack[0][i] , ing[0], pack[0][i] ,ing[0])) ans++;
    }
    printf("Case #%d: %d\n", testNum, ans);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) Solve(i+1);
}
