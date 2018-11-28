//
//  main.cpp
//  googlecode
//
//  Created by Thomas Rogg on 08.04.17.
//  Copyright © 2017 Thomas Rogg. All rights reserved.
//

#include <iostream>

int try_(const char *in, int k, int n, int l, int c)
{
    char txt[10240];
    strcpy(txt, in);
    int i;

//    printf("CHECKING %s\n", in);
    for(i = 0; i < n; i++)
    {
        if(in[i] == '-')
            break;
    }
    if(i == n)
        return c;

    int bestC = -1;
    for(i = l; i <= n - k; i++)
    {
        strcpy(txt, in);
        for(int j = 0; j < k; j++)
            txt[i + j] = txt[i + j] == '-' ? '+' : '-';

        int newC = try_(txt, k, n, i + 1, c + 1);
        if(bestC == -1 || (bestC > newC && newC != -1))
            bestC = newC;
    }
    return bestC;
}

void handle(int casen)
{
    char txt[10240];
    int k;

    scanf("%s %d", txt, &k);
    int n = strlen(txt);

    int c = try_(txt, k, n, 0, 0);
    if(c == -1)
        printf("Case #%d: IMPOSSIBLE\n", casen);
    else
        printf("Case #%d: %d\n", casen, c);
}

int main(int argc, const char * argv[]) {
    int num;
    scanf("%d", &num);
    for(int i = 0; i < num; i++)
        handle(i + 1);
    return 0;
}
