#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 100;
char b[maxn][maxn];
int T, r, c, Case = 1;

int main()
{
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d:\n", Case++);
        scanf("%d%d", &r, &c);
        for(int i = 1; i <= r; i++)
            scanf("%s", b[i]+1);
        for(int i = 1; i <= r; i++) {
            for(int j = 1; j <= c; j++) if(b[i][j] != '?') {      
                int k, l, l2;
                for(k = 1; i - k >= 1 && b[i-k][j] == '?'; k++); k--;
                for(l = 1; j - l >= 1 && b[i][j-l] == '?'; l++); l--;
                for(l2 = 1; j + l2 <= c && b[i][j+l2] == '?'; l2++); l2--;
                for(int x = i-k; x <= i; x++)
                    for(int y = j-l; y <= j+l2; y++) b[x][y] = b[i][j];
                /*
                printf("%d %d %d %d %d\n", i, j, k, l, l2);
                for(int x = 1; x <= r; x++) {
                    printf("%s\n", b[x]+1);
                }
                printf("\n");
                */
            }
        }
        int x;
        for(x = r; x >= 1 && b[x][1] == '?'; x--);
        if(x != r)
            for(int i = x+1; i <= r; i++)
                memcpy(b[i], b[x], sizeof(b[0]));
        for(int i = 1; i <= r; i++)
            printf("%s\n", b[i]+1);
    }
    return 0;
}