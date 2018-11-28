#include <cstdio>
#include <cstring>

void flipchar(char *c) {
    *c = *c=='-' ? '+' : '-';
}

void flip(char *line, int pos, int k) {
    for(int i=0; i<k; i++) {
        flipchar(&line[pos+i]);
    }
}

int main() {
    FILE *fin = fopen("input.txt", "r");
    int t, k, len, invcount;
    char line[1005];

    fscanf(fin, "%d", &t);

    for (int casenum=1; casenum<=t; casenum++) {
        invcount = 0;
        printf("Case #%d: ", casenum);
        fscanf(fin, "%s %d", &line, &k);
//        printf("%s\n", line);

        len = strlen(line);
        if (line[0] == '-') {
            flip(line, 0, k);
            invcount++;
        }

        for (int i=1; i<len; i++) {
            if (line[i] != line[i-1]) {
                if (i > len-k) {
                    invcount=-1;
                    break;
                }
                flip(line, i, k);
                invcount++;
//                printf("%s\n", line);
            }
        }
        if (invcount>=0) {
            printf("%d\n", invcount);
        } else {
            printf("%s\n", "IMPOSSIBLE");
        }
    }
    fclose(fin);
}
