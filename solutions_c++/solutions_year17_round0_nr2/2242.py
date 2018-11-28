#include <bits/stdc++.h>
using namespace std;

const int MAXN = 20;
typedef long long ll;

int v[MAXN];

int main()
{
    int tt;
    scanf("%d", &tt);

    for (int t = 1; t <= tt; t++) {
        ll n;
        scanf("%lld", &n);

        int m = 0;
        while (n) {
            v[m++] = n % 10;
            n /= 10;
        }

        int error = -1;
        for (int i = m-1; i > 0; i--) {
            if (v[i-1] < v[i]) {
                error = i;
                while (error+1 < m && v[error] == v[error+1]) error++;
                break;
            }
        }

        if (error != -1)  {
            v[error]--;
            for (int i = 0; i < error; i++) {
                v[i] = 9;
            }
        }

        printf("Case #%d: ", t);
        bool print = 0;
        for (int i = m-1; i >= 0; i--) {
            if (v[i] != 0 || print) {
                printf("%d", v[i]);
                print = true;
            }
        }
        printf("\n");
    }
}
