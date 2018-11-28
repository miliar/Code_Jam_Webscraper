#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>


using namespace std;

char ss[20];
#define LL long long

int main() {
    int test;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%s", ss);
        int n = strlen(ss);

        int i, j;

        LL val = 0;
        for (i = 0; i < n; i++) {
            val = val * 10 + (ss[i] - '0');
        }

        for (i = 1; i < n; i++) {
            if (ss[i] >= ss[i - 1]) {

            }
            else {
                break;
            }
        }

        printf("Case #%d: ", cas);

        if (i == n) {
            puts(ss);
        }
        else {
            for (j = i - 1; j >= 1; j--) {
                if (ss[j] == ss[j - 1]) {
                }
                else {
                    break;
                }    
            }
            
            LL tmp = 0;
            //cout << j << endl;
            for (j = j + 1; j < n; j++) {
                tmp = tmp * 10 + (ss[j] - '0');
            }

            printf("%lld\n", val - tmp - 1);
        }
    }
    return 0;
}
