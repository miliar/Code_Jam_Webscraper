#include <cstdio>

using namespace std;

int main()
{
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int tc, ti;
    int n, i, j;

    fscanf(fin, "%d", &tc);
    for(ti=1; ti<=tc; ti++) {

        fscanf(fin, "%d", &n);
        while(n > 9) {

            i = n;
            j = 10;
            while(i) {
                if(i%10 > j) break;
                j = i%10;
                i = i / 10;
            }

            if(i == 0) break;
            n--;
        }

        fprintf(fout, "Case #%d: %d\n", ti, n);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}