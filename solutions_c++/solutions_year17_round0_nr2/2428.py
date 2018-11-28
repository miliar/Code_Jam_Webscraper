#include <cstdio>
#include <cstring>

int main() {
    int t;
    long long n, pow;
    FILE *fin = fopen("input.in", "r");
    
    fscanf(fin, "%d", &t);

    for (int setnum=1; setnum<t+1; setnum++) {
        pow = 1;
        printf("Case #%d: ", setnum);
        fscanf(fin, "%lld", &n);
        while (n/pow > 1) {
            if ( (n%(10*pow) - n%pow)/pow < (n%(100*pow)-n%(10*pow))/(pow*10)) {
                n -= (n%(10*pow)+1);
            }
            pow*=10;
        }
        printf("%lld\n", n);
    }
    fclose(fin);
}
