#include<cstdio>
#include<algorithm>

using namespace std;
#define N 1005

int tc,n;
char data[N];
int main() {
    int i,j,k;
    scanf("%d", &tc);
    for (int tcc = 1; tcc <= tc; tcc++) {
        scanf("%s %d", data, &n);
        int len = strlen(data);
        int ans = 0;
        for (i = 0; i < len - n + 1; i++) {
            if (data[i] == '-') {
                for (j = i; j < i + n; j++)
                    data[j] = '+' + '-' - data[j];
                ans++;
            }
        }
        for (i = len - n + 1; i < len; i++)
            if (data[i] == '-')
                ans = -1;
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", tcc);
        else
            printf("Case #%d: %d\n", tcc, ans);
    }
    return 0;
}
