#include<cstdio>
#include<cstring>
#define MAX 36

using namespace std;

int solve(char* s, int pos, int len) {
    int prev;
    int r;

    if(pos == 0) {
        prev = 0;
    } else {
        prev = s[pos-1] - '0';
    }

    int now = s[pos] - '0';

    if(now < prev) {
        return -1;
    }

    if(pos == len-1) {
        return 1;
    }

    r = solve(s, pos+1, len);

    if(r == 1) {
        return 1;
    }

    if(r == -1) {
        if(now-1 >= prev) {
            s[pos] = '0' + now - 1;
            for(int i = pos+1; i < len; ++i) {
                s[i] = '9';
            }
            return 1;
        }
        return -1;
    }
    return -1;

}

int main() {
    int T;
    scanf("%d", &T);
    int cnt = 0;

    char s[MAX];

    while(cnt < T) {

        scanf("%s", s);
        int len = strlen(s);

        cnt++;
        printf("Case #%d: ", cnt);

        if(len == 1) {
            printf("%s\n", s);
            continue;
        }

        solve(s, 0, len);
        int i = 0;
        while(i < len && s[i] == '0') i++;
        while(i < len) {
            printf("%c", s[i]);
            i++;
        }
        printf("\n");
    }

}
