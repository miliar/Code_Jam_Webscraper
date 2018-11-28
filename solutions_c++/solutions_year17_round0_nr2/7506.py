#include<cstdio>
#include<algorithm>

using namespace std;
#define N 20

int tc;
int data[N];
int main() {
    int i,j,k;
    long long n;
    scanf("%d", &tc);
    for (int tcc = 1; tcc <= tc; tcc++) {
        scanf("%lld", &n);
        int len = 0;
        while(n != 0) {
            data[len++] = n % 10;
            n /= 10;
        }
        for (i = 0; i < len -1; i++) {
            if (data[i] < data[i+1]) {
                data[i+1]--;
                for (j = 0; j <= i; j++)
                    data[j]=9;
            }
        }
        printf("Case #%d: ", tcc);
        for (i = len - 1; i >= 0; i--) {
            if (i == len - 1 && data[i] ==0)
                continue;
            printf("%d", data[i]);
        }
        printf("\n");
    }
    return 0;
}
