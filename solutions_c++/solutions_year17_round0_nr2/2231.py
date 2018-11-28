#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int LEN = 20;
const bool BRUTE = false;

char num[LEN + 5];
long long n;

bool isTidy(long long n) {
    int last = 9;
    while (n) {
        if (n % 10 > last) return false;
        last = n % 10;
        n /= 10;
    }
    return true;
}

int firstLocalMax() {
    for (int i = 0; num[i]; i++)
        if (num[i] > num[i + 1]) return i;
    return 42;
}

void continueNines(int i) {
    for (; num[i]; i++)
        num[i] = '9';
}

int findDrop(int i) {
    for (; i > 0; i--) {
        if (num[i] > num[i - 1]) return i;
    }
    return 0;
}

int main() {
    freopen("tidy.in","r",stdin);
    freopen("tidy.out","w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
        scanf("%lld",&n);
        sprintf(num, "%lld", n);
        if (BRUTE) {
            long long ret;
            for (ret = n ; !isTidy(ret) ; ret--);
            printf("Case #%d: %lld\n",test,ret);
        } else {
            printf("Case #%d: ",test);
            int i = firstLocalMax();
            if (!num[i + 1]) {
                printf("%s\n",num);
            } else {
                i = findDrop(i);
                num[i]--;
                continueNines(i + 1);
                if (num[0] == '0') printf("%s\n",num + 1);
                else printf("%s\n",num);
            }
        }
    }
    
    return 0;
}
