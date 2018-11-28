#include<bits/stdc++.h>
using namespace std;

char s[1002];
int N, M;

void main2(int tc) {
    scanf("%s %d", s, &M);
    N = 0;
    for(int i = 0; i < s[i]; i++) N++;
    int cnt = 0;
    for(int i = 0; i <= N - M; i++) {
        if(s[i] == '-') {
            cnt++;
            for(int j = i; j < i + M; j++) {
                s[j] = s[j] == '+'? '-' : '+';
            }
        }
    }
    printf("Case #%d: ", tc);
    for(int i = 0; i < N; i++) if(s[i] != '+') {
        printf("IMPOSSIBLE\n");
        return;
    }
    printf("%d\n", cnt);
}

int TC;
int main() {
    freopen("inputA.txt", "r", stdin);
    freopen("outputA.txt", "w", stdout);
    scanf("%d", &TC);
    for(int i = 1; i <= TC; i++) main2(i);
}
