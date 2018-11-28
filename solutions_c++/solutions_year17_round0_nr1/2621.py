#include<cstdio>
#include<cstring>
#define MAX 1024

using namespace std;

void flip(char* s, int pos, int k) {
    for(int i = 0; i < k; ++i) {
        int index = pos + i;
        if(s[index] == '+') {
            s[index] = '-';
        } else {
            s[index] = '+';
        }
    }
}

int solve(char* s, int pos, int len, int k) {
    if(pos == len-k+1) {
        for(int i = pos; i < len; ++i) {
            if(s[i] == '-') {
                return -1;
            }
        }
        return 0;
    }

    bool fliped = false;
    if(s[pos] == '-') {
        flip(s, pos, k);
        fliped = true;
    }

    int r = solve(s, pos+1, len, k);

    if(r < 0) {
        return r;
    }

    if(fliped) {
        r++;
    }
    return r;
}

int main() {
    int T;
    int K;

    scanf("%d", &T);
    char s[MAX];

    int cnt = 0;
    while(cnt < T) {

        scanf("%s", s);
        scanf("%d", &K);

        int len = strlen(s);
        int r = solve(s, 0, len, K);

        cnt++;
        printf("Case #%d: ", cnt);
        if(r < 0) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", r);
        }
    }
    return 0;
}

