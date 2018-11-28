#include <bits/stdc++.h>
using namespace std;

const int MAX = 25;

char N[MAX];

int main() {
    freopen("B-output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase) {
        scanf("%s", N); 
        int len = strlen(N);
        for (int i = 0; i < len - 1; ++i) {
            if (N[i] > N[i + 1]) {
                int j = i;
                while (j - 1 >= 0 && N[j] == N[j - 1]) --j;
                --N[j];
                ++j;
                while (j < len) N[j++] = '9';
                break;
            }
        }
        int k = 0;
        while (k < len && N[k] == '0') ++k;
        printf("Case #%d: ", testcase);
        while (k < len) printf("%c", N[k++]);
        printf("\n");
    }
}
