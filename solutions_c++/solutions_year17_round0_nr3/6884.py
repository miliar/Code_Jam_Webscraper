#include <cstdio>
#include <cstring>

using namespace std;

const int N = 1002;

int mymin(int a, int b) { return (a<b ? a:b); }
int mymax(int a, int b) { return (a>b ? a:b); }

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int tc, ti;
    int n, k;
    int tol[N];

    int lr[N];
    int i, j, ki, l, mx, mx1;

    fscanf(fin, "%d", &tc);
    for(ti=1; ti<=tc; ti++) {

        fscanf(fin, "%d%d", &n, &k);

        memset(tol, 0, sizeof(tol));
        tol[0] = 1;
        tol[n+1] = 1;

        for(ki=0; ki<k; ki++) {

            for(i=n+1; i>=0; i--) {
                if(tol[i] == 1)
                    lr[i] = -1;
                else
                    lr[i] = lr[i+1]+1;
            }

            l=-1;
            mx = -2;
            for(i=0; i<=n+1; i++) {
                if(tol[i] == 1) {
                    l = -1;
                    continue;
                }

                l++;

                if(mx < mymin(l, lr[i])) {
                    j = i;
                    mx = mymin(l, lr[i]);
                    mx1 = mymax(l, lr[i]);
                } else
                if(mx == mymin(l, lr[i])) {
                    if(mx1 < mymax(l, lr[i])) {
                        j = i;
                        mx1 = mymax(l, lr[i]);
                    }
                }
            }
            tol[j] = 1;
        }

        fprintf(fout, "Case #%d: %d %d\n", ti, mx1, mx);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
