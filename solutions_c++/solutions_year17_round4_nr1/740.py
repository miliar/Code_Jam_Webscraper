#include <bits/stdc++.h>
using namespace std;

int tot[10];
int add[100][4], totAdd;
int n, P, ans;
void dfs(vector<int> a, int idx, int ad) {
    //for(int i = 0; i < P; i++) {
    //    cout << a[i] << " ";
    //}
    //puts("");
    if(idx >= totAdd) {
        for(int i = 0; i < P; i++) {
            if(tot[i] - a[i]) {
                ad++;
                break;
            }
        }
        ans = max(ans, ad);
        return ;
    }
    int tt = 0;
    for(int i = 0; i < 4; i++) {
        tt += i * add[idx][i];
    }
    if(tt % P) {
        dfs(a, idx + 1, ad);
    } else {
        for(int i = 0; i <= 100; i++) {
            vector<int> b = a;
            bool judge = true;
            for(int j = 0; j < 4; j++) {
                b[j] += i * add[idx][j];
                if(b[j] > tot[j]) {
                    judge = false;
                    break;
                }
            }
            if(judge) {
                dfs(b, idx + 1, ad + i);
            } else {
                break;
            }
        }
    }
}

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                if(!(i + j + k)) continue;
                add[totAdd][1] = i;
                add[totAdd][2] = j;
                add[totAdd][3] = k;
                totAdd++;
            }
        }
    }

    int test;
    scanf("%d", &test);
    for(int _ = 1; _ <= test; _++) {
        std::cerr <<"_:" << _ << std::endl;

        scanf("%d%d", &n, &P);

        int ret = 0;
        memset(tot, 0, sizeof(tot));
        for(int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            if(0 == x % P)
                ret++;
            else{
                tot[x % P]++;
            }
        }

        ans = 0;
        vector<int> now(4, 0);
        dfs(now, 0, 0);

        printf("Case #%d: %d\n", _, ret + ans);
    }
    return 0;
}
