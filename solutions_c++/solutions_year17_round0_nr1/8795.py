#include <cstdio>
#include <cstring>

using namespace std;

const int N = 1001;

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int tc, ti;

    int n, k, ans;
    char ck[N];

    int i, j;

    fscanf(fin, "%d", &tc);
    for(ti=1; ti<=tc; ti++) {

        fscanf(fin, "%s%d", ck, &k);
        n = strlen(ck);

        ans = 0;
        for(i=0; i<n; i++) {

            if(ck[i] == '-') {

                if(i > n-k) {
                    ans = -1;
                    break;
                }

                ans++;
                for(j=i; j<i+k; j++) {
                    if(ck[j] == '-')
                        ck[j] = '+';
                    else
                        ck[j] = '-';
                }
            }
        }

        if(ans == -1) {
            fprintf(fout, "Case #%d: IMPOSSIBLE\n", ti);
        } else {
            fprintf(fout, "Case #%d: %d\n", ti, ans);
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
