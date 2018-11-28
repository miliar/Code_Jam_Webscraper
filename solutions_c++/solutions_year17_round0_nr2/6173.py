#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

bool check(char str[], int n) {
    for (int i = 0; i < n-1; i++) {
        if (str[i] > str[i+1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T;
    scanf("%d", &T);

    char in[20];
    for (int times = 0; times < T; times++) {
        scanf("%s", in);
        int len = strlen(in);

        if (check(in, len) == true) {
            printf("Case #%d: %s\n", times+1, in);
        } else {
            long long mmax = 0;
            for (int i = 0; i < len; i++) {
                if (in[i] == '0') {
                    continue;
                } else {
                    char tmp[20];
                    strcpy(tmp, in);
                    
                    tmp[i] -= 1;
                    for (int j = i+1; j < len; j++) {
                        tmp[j] = '9';
                    }

                    if (check(tmp, len) == true) {
                        long long val = strtoll(tmp, 0, 10);
                        mmax = max(mmax, val);
                    }
                }
            }
            printf("Case #%d: %lld\n", times+1, mmax);
        }
    }
}
