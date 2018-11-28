#include <cstdio>
#include <cstring>

const int MAXN = 50;

char s[MAXN], buff[MAXN];
int T, n;
unsigned long long result;

void fill(char* buf, int l, int r) {
    for (int i = l; i < r; i++) {
        buf[i] = '9';
    }
}

void update(char* buf, int l, int r) {
    unsigned long long sum = 0ULL;
    for (int i = l; i < r; i++) {
        sum = sum * 10ULL + (buf[i]-'0');
    }
    //printf("UDP: %llu\n", sum);
    if (sum > result) result = sum;
}

void dfs(int pos) {
    if (pos >= n) {
        update(buff, 0, n);
        return;
    }

    buff[pos] = '\0';
    for (int x = 9; x >= 0; x--) {
        if (pos == 0 && x == 0) continue;

        if (pos && x < s[pos-1]-'0') continue;

        if (x > s[pos]-'0') {
            continue;
        }

        if (x == s[pos]-'0') {
            buff[pos] = s[pos];
            dfs(pos+1);
        } else {
            buff[pos] = x+'0';
            fill(buff, pos+1, n);
            update(buff, 0, n);
            break;
        }
    }
    buff[pos] = '\0';
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s", s);
        n = strlen(s);
        result = 0;
        fill(buff, 0, n-1);
        update(buff, 0, n-1);

        dfs(0);

        printf("Case #%d: %llu\n", t, result);

    }
    return 0;
}
