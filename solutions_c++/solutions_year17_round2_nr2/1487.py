#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cmath>
#include <inttypes.h>

#include <string>
#include <vector>
#include <set>
#include <map>

inline int RANDOM_NUM(int from, int tillExcl) {
    int n;

    do
    {
        n = rand() / (double)RAND_MAX * (tillExcl - from) + from;
    } while(n == tillExcl);
    return n;
}


int main()
{
    srand(time(NULL));

    int numTasks;
    scanf("%d", &numTasks);

    for(int taskNo = 1; taskNo <= numTasks; taskNo++)
    {
    int R, O, Y, G, B, V, N;
    bool ok;
    char result[1024];
        
        {
        scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
        if(N != R + O + Y + G + B + V)
            return false;
        }
        {
        ok = O <= B && G <= R && V <= Y;
        if(ok)
        {
            int pos = 0;
            if(O && O == B && !G && !V)
            {
                for(int i = 0; i < O; i++)
                {
                    result[pos++] = 'O'; result[pos++] = 'B';
                }
            }
            else if(R && R == G && !O && !V)
            {
                for(int i = 0; i < R; i++)
                {
                    result[pos++] = 'R'; result[pos++] = 'G';
                }
            }
            else if(Y && Y == V && !O && !G)
            {
                for(int i = 0; i < Y; i++)
                {
                    result[pos++] = 'Y'; result[pos++] = 'V';
                }
            }
            else
            {
                B -= O;
                R -= G;
                Y -= V;
//                fprintf(stderr, "O %d G %d V %d\n", O, G, V);
  //              fprintf(stderr, "R %d B %d Y %d\n", R, B, Y);

                char last;
                if(B)
                {
                    last = 'B';
                    if(B-- == 0)
                        ok = false;
                }
                else if(R)
                {
                    last = 'R';
                    if(R-- == 0)
                        ok = false;
                }
                else if(Y)
                {
                    last = 'Y';
                    if(Y-- == 0)
                        ok = false;
                }
                else
                {
                   ok = false;
                }
                if(ok)
                {
//                fprintf(stderr, "last %c R%d B%d Y%d\n", last, R, B, Y);
                result[pos++] = last;
                if(last == 'B' && O)
                {
                    result[pos++] = 'O';
                    result[pos++] = 'B';
                    O--;
                }
                if(last == 'R' && G)
                {
                    result[pos++] = 'G';
                    result[pos++] = 'R';
                    G--;
                }
                if(last == 'Y' && V)
                {
                    result[pos++] = 'V';
                    result[pos++] = 'Y';
                    V--;
                }
                    while(R || B || Y)
                    {
                        if(last != 'R' && (R >= B || last == 'B') && (R >= Y || last == 'Y'))
                        {
                            last = 'R';
                            if(R-- == 0)
                            {
                           //     fprintf(stderr, "ERR1\n");
                                ok = false;
                                break;
                            }
                        }
                        else if(last != 'B' && (B >= Y || last == 'Y') && (B >= R || last == 'R'))
                        {
                            last = 'B';
                            if(B-- == 0)
                            {
                           //     fprintf(stderr, "ERR2\n");
                                ok = false;
                                break;
                            }
                        }
                        else if(last != 'Y')
                        {
                            last = 'Y';
                            if(Y-- == 0)
                            {
                          //      fprintf(stderr, "ERR3\n");
                                ok = false;
                                break;
                            }
                        }
                        else
                        {
                 //               fprintf(stderr, "ERR4\n");
                            ok = false;
                            break;
                        }
            //    fprintf(stderr, "last2 %c R%d B%d Y%d\n", last, R, B, Y);
                        result[pos++] = last;
                        if(last == 'B' && O)
                        {
                            result[pos++] = 'O';
                            result[pos++] = 'B';
                            O--;
                        }
                        if(last == 'R' && G)
                        {
                            result[pos++] = 'G';
                            result[pos++] = 'R';
                            G--;
                        }
                        if(last == 'Y' && V)
                        {
                            result[pos++] = 'V';
                            result[pos++] = 'Y';
                            V--;
                        }
                    }
                }
                if(R || G || B || O || V || Y)
                    ok = false;
            }
                if(ok && result[0] == result[pos - 1])
                {
                    ok = false;
                }
                result[pos] = '\0';
        //        fprintf(stderr, "OK=%d POS=%d RES=%s\n", ok, pos, result);
        }
        }

        printf("Case #%d: ", taskNo);
        {
        if(!ok)
            printf("IMPOSSIBLE\n");
        else
            printf("%s\n", result);
        }
    }

    return EXIT_SUCCESS;
}
