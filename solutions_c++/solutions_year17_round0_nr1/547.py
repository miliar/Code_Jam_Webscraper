#include <bits/stdc++.h>
#define FO(i,a,b) for (int i = a; i < b; i++)
#define sz(v) int(v.size())

using namespace std;

string s;
int k;

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        printf("Case #%d: ", Z);
        cin >> s >> k;
        int res = 0;
        FO(i,0,sz(s)-k+1) {
            if (s[i] == '-') {
                FO(j,0,k) s[i+j] = '+'+'-'-s[i+j];
                res++;
            }
        }
        FO(i,0,sz(s)) if (s[i] != '+') {
            res = 1e9;
        }
        if (res < 1e8) printf("%d\n", res);
        else printf("IMPOSSIBLE\n");
    }
}
