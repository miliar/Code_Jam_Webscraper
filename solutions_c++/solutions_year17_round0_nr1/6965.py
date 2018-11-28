#define problem "A-large"
#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen(problem".in", "r", stdin);
    freopen(problem".out", "w", stdout);
    int test;
    cin >> test;
    for(int test_case = 1; test_case <= test; test_case++) {
        string S;
        int K;
        cin >> S >> K;
        int ans = 0;
        for(int i = 0; i < (int)S.size() - K + 1; i++) if(S[i] == '-'){
            for(int j = i; j < i + K; j++) S[j] = S[j] == '+' ? '-' : '+';
            ans++;
        }
        printf("Case #%d: ", test_case);
        for(int i = 0; i < (int)S.size(); i++) if(S[i] == '-'){
            ans = -1;
            break;
        }
        if(ans == -1) puts("IMPOSSIBLE"); else printf("%d\n", ans);
    }
}
