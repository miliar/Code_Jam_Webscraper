#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>

#define BUFSZ 10000

// Tidy numbers

int main(int argc, char *argv[])
{
    FILE *fp;
    char strBuf[BUFSZ+1];
    char *token, *subtoken, *sptr1, *sptr2;
    int T;       // loops
    int i, j, k;

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
        int count=0;
        int len;
        int currdigit, lastdigit;
        int bignum[20];

        fgets(strBuf, BUFSZ, fp);
        token = strtok_r(strBuf, "\r\n", &sptr1);
        len = strlen(token);

        // alg
        // next digit must be same or larger than last
        // else
        //   remaining become 9s
        //   current gets lowered, but must be >= previous
        for (j=0; j<20; j++) bignum[j] = 0;
        for (j=0; j<len; j++)
        {
            currdigit = (token[j] - '0');
            if (j==0) bignum[j] = currdigit;
            else
            {
                if (currdigit >= lastdigit) bignum[j] = currdigit;
                else
                {
                    if (lastdigit == 1)
                    {
                        // all 9s, len is less 1
                        len--;
                        for (k=0; k<len; k++) bignum[k] = 9;
                        break;
                    }

                    k=j-1;
                    // fill the rest with 9s
                    while (j<len) bignum[j++] = 9;

                    // cap first j digits with lastdigit-1
                    for (; k>0; k--)
                    {
                        if (bignum[k] > bignum[k-1])
                        {
                            bignum[k]--;
                            // avoid dec-ing the first digit
                            k=0;
                        }
                        else
                        {
                            bignum[k] = 9;
                        }
                    }
                    // dec first digit
                    if (k==0) bignum[k]--;
                }
            }

            lastdigit = currdigit;
        }

        printf("Case #%d: ", i+1);
        for (j=0; j<len; j++)
        {
            printf("%d", bignum[j]);
        }
        printf("\n");
    }


    fclose(fp);
    return 0;
}
