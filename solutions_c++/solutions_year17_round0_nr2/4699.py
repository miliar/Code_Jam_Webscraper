#include <iostream>
#include <cstdio>

using namespace std;

int t;
long long n;

int digits(long long x)
{
    int c = 0;
    do {
        c++;
        x /= 10;
    }while(x);
    return c;
}

int aux[25], sol[25], crt;

void solve()
{
    int x = digits(n);
    long long v = n;
    for (int i = x; i >= 1; i--)
        aux[i] = v%10, v /= 10;
    crt = 0;
    for (int i = 1; i <= x; i++) {
        if (i == x) {
            sol[++crt] = aux[i];
            continue;
        }
        if (aux[i] > aux[i+1]) {
            sol[++crt] = aux[i]-1;
            for (int p = i+1; p <= x; p++)
                sol[++crt] = 9;
            break;
        }
        else if (aux[i] < aux[i+1]) {
            sol[++crt] = aux[i];
        }
        else {
            int p = i+1;
            for (p; p <= x && aux[p] == aux[i]; p++);
            if (p == x+1 || aux[i] < aux[p]) {
                sol[++crt] = aux[i];
                continue;
            }
            else {
                sol[++crt] = aux[i]-1;
                for (int p = i+1; p <= x; p++)
                    sol[++crt] = 9;
                break;
            }
        }
    }
    for (int i = 1, ok = 0; i <= crt; i++) {
        if (ok || sol[i] != 0)
            printf("%d", sol[i]), ok = 1;
    }
}

int main()
{
    freopen("tidy.in", "r", stdin);
    freopen("tidy.out", "w", stdout);

    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%lld", &n);
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }

    return 0;
}
