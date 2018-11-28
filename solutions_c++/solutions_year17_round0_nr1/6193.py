#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000
#define MYCAP 1000

//#define TEST

// Oversized Pancake Flipper

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int rowlen;
    int S[1001];
    int K;
    int i, j, k, l;

    if (argc != 2)
    {
        exit(-1);
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Usage: file is no good\n");
        exit(-1);
    }


    fgets(strBuf, BUFSZ, fp);
    token = strtok_r(strBuf, "\r\n", &sptr1);
    T = atoi(token);

    for (i=0; i<T; i++)
    {
        int foundarray = 0;
        int basenum;
        int currnum;
        int tempnum;
        int p = 0;
        int m = 0;


        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);

        subtoken = strtok_r(token, " ", &sptr2);
        rowlen = strlen(subtoken);

        for (j=0; j<1001; j++) S[j] = 0;
        for (j=0; j<rowlen; j++)
        {
            if (subtoken[j] == '+')
            {
                S[j]++;
                p++;
            }
            else m++;
        }

        subtoken = strtok_r(NULL, " ", &sptr2);
        K = atoi(subtoken);

        // alg
        // if 0 m's, done
        // find the first 0, and work way across
        if (m == 0)
        {
            printf("Case #%d: %d\n", i+1, 0);
        }
        else
        {
            int flips = 0;
            int lastp = 0;
            int lastm = 0;
            for (j=0; j<rowlen-K; j++)
            {
                // if current is even, then need to flip
                if ((S[j] % 2) == 0)
                {
                    flips++;
                    // flip K pancakes, starting with the current
                    for (k=0;k<K; k++)
                    {
                        S[j+k]++;
                    }
                }
            }
            // check if last K are all good or all bad; otherwise impossible
            for (;j<rowlen; j++)
            {
                ((S[j] % 2) == 0) ? lastm++ : lastp++;
            }

            if (lastp > 0 && lastm > 0)
            {
                printf("Case #%d: IMPOSSIBLE\n", i+1);
            }
            else
            {
                if (lastp == 0) flips++;
                printf("Case #%d: %d\n", i+1, flips);
            }
        }
    }

    fclose(fp);
    return 0;
}
