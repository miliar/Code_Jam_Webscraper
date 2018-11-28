#include <stdio.h>
#include <strings.h>

void
remove_preceeding_zero(char *s) 
{
    int l = strlen(s);
    while (*s == '0') {
        memmove(s, s+1, l); // + 1 for last null
        l--;
    }
}

#define C2N(c)      (int)(c - '0')

void
solve(char *s, int deep)
{
    int n = strlen(s);
    if (n == 1) {
        return;
    }

    int i = C2N(s[0]);
    int j = C2N(s[1]);
    if (i == 1 && i > j) { // 10xx -> 09999
        char *p = s;
        *p++ = '0';
        do {
            *p = '9';
            p++;
        } while (*p != 0);
        solve(s - deep, 0);
    }
    else if (i <= j) {
        solve(s + 1, deep + 1);
    }
    else { 
        char *p = s;
        *p++ = i - 1 + '0';
        do {
            *p = '9';
            p++;
        } while(*p != 0);
        solve(s - deep, 0);
    }
}

void
reverse(char *s)
{
    char r[18 + 1] = {0};
    int l = strlen(s);
    for (int i = 0; i < l; i++) {
        r[i] = s[l - 1 - i];
    }
    strcpy (s, r);
}

int
main(void)
{
    int T;
    int i;

    fscanf (stdin, "%d", &T);
    for (i = 0; i < T; i++) {
        char s[18 + 1] = {0,};

        fscanf (stdin, "%s", s);

        fprintf (stderr, "%s -> ", s); // debug

        solve(s, 0);
        remove_preceeding_zero(s);
        fprintf (stdout, "Case #%d: %s\n", i+1, s);

        fprintf (stderr, "%s \n", s); // debug
    }
    return 1;
}
