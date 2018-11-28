#include <stdio.h>

int main(int p_Argc, char  **p_Argv)
{
    int T;
    int t = 0, first = 0;

    char A, B ,tmp;
    int repeat = 0;

    scanf("%d\n", &T);

    principal:
        t++;
        if (t>T)
            goto fin;
        printf("Case #%d: ", t);
        repeat = 0;
        scanf("%c", &B);

        boucle:
            tmp = B;
            scanf("%c", &B);
            A = tmp;
            repeat++;
            if ( B == 10){
                goto print_n_and_new;
            }
            if (B > A){
                goto print_n;
            }
            if (B < A){
                goto print_nine;
            }
            goto boucle;
    end_principal:
        printf("%c",10);
        goto principal;

    print_n:
        if (repeat == 0)
            goto boucle;
        printf("%c", A);
        repeat--;
        goto print_n;

    print_n_and_new:
        if (repeat == 0)
            goto end_principal;
        printf("%c", A);
        repeat--;
        goto print_n_and_new;
    print_nine:
        if (first == 0)
            goto check0;
        first = 1;
        printf("%c", A-1);
        print_nineA:
            if (repeat == 0)
                goto print_nineB;
            printf("%c", '9');
            repeat--;
            goto print_nineA;
        print_nineB:
            scanf("%c", &B);
            if (B == 10){
                goto end_principal;
            }
            printf("%c", '9');
            goto print_nineB;
    check0:
        if (A-1 == '0')
            goto print_nineA;
        printf("%c", A-1);
        goto print_nineA;

    fin:
    return 0;
}





