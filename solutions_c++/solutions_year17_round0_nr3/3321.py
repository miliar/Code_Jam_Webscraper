#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stdio.h>
#include <fstream>
#include <cmath>
using namespace std;
unsigned long long N,K,res1,res2;
long long bres1, bres2;
void find ()
{
    unsigned long long stack1, stack2, mid, num_stack1, num_stack2;
    if (N % 2 == 0)
    {
        stack1 = N / 2 - 1;
        stack2 = N / 2;
    }
    else
    {
        stack1 = N / 2;
        stack2 = N / 2;
    }
    mid = 1;
    if (mid == K)
    {
        res1 = stack1;
        res2 = stack2;
        return;
    }
    num_stack1 = 1;
    num_stack2 = 1;
    while (stack1 != 0 || stack2 != 0)
    {
        unsigned long long tmp_stack1, tmp_stack2, tmp_mid, tmp_num_stack1, tmp_num_stack2;
        if (stack1 % 2 == 0 && stack2 % 2 == 0)
        {
            tmp_stack1 = stack1 / 2 - 1;
            tmp_stack2 = stack1 / 2;
            tmp_num_stack1 = num_stack1 + num_stack2;
            tmp_num_stack2 = num_stack1 + num_stack2;
        }
        if (stack1 % 2 == 1 && stack2 % 2 == 0)
        {
            tmp_stack1 = stack2 / 2 - 1;
            tmp_stack2 = stack2 / 2;
            unsigned long long tmp = stack1 / 2;
            if (tmp == tmp_stack1)
            {
                tmp_num_stack1 = num_stack2 + num_stack1 * 2;
                tmp_num_stack2 = num_stack2;
            }
            else
            {
                tmp_num_stack1 = num_stack2;
                tmp_num_stack2 = num_stack2 + num_stack1 * 2;
            }
        }
        if (stack1 % 2 == 0 && stack2 % 2 == 1)
        {
            tmp_stack1 = stack1 / 2 - 1;
            tmp_stack2 = stack1 / 2;
            unsigned long long tmp = stack2 / 2;
            if (tmp == tmp_stack1)
            {
                tmp_num_stack1 = num_stack1 + num_stack2 * 2;
                tmp_num_stack2 = num_stack1;
            }
            else
            {
                tmp_num_stack1 = num_stack1;
                tmp_num_stack2 = num_stack1 + num_stack2 * 2;
            }
        }
        if (stack1 % 2 == 1 && stack2 % 2 == 1)
        {
            tmp_stack1 = stack1 / 2;
            tmp_stack2 = stack1 / 2;
            tmp_num_stack1 = num_stack1 + num_stack2;
            tmp_num_stack2 = num_stack1 + num_stack2;
        }
        tmp_mid = num_stack1 + num_stack2;
        if (mid + tmp_mid >= K)
        {
            unsigned long long tmpr1 = 0, tmpr2=0, tmpr1_2 =0, tmpr2_2=0;
            if (stack1 > stack2)
            {
                if (num_stack1 + mid >= K)
                {
                    if (stack1 % 2 == 1)
                    {
                        tmpr1 = stack1 / 2;
                        tmpr2 = stack1 / 2;
                    }
                    else
                    {
                        tmpr1 = stack1 / 2 - 1;
                        tmpr2 = stack1 / 2;
                    }
                }
                else
                {
                    if (stack2 % 2 == 1)
                        {
                            tmpr1 = stack2 / 2;
                            tmpr2 = stack2 / 2;
                        }
                        else
                        {
                            tmpr1 = stack2 / 2 - 1;
                            tmpr2 = stack2 / 2;
                        }
                }
            }
            else
            {
                if (num_stack2 + mid >= K)
                {
                    if (stack2 % 2 == 1)
                    {
                        tmpr1_2 = stack2 / 2;
                        tmpr2_2 = stack2 / 2;
                    }
                    else
                    {
                        tmpr1_2 = stack2 / 2 - 1;
                        tmpr2_2 = stack2 / 2;
                    }
                }
                else
                {
                    if (stack1 % 2 == 1)
                    {
                        tmpr1_2 = stack1 / 2;
                        tmpr2_2 = stack1 / 2;
                    }
                    else
                    {
                        tmpr1_2 = stack1 / 2 - 1;
                        tmpr2_2 = stack1 / 2;
                    }
                }
            }


            res1 = tmpr1;
            res2 = tmpr2;
            if (min(tmpr1,tmpr2) < min(tmpr1_2,tmpr2_2))
            {
                res1 = tmpr1_2;
                res2 = tmpr2_2;
            }
            if (min(tmpr1,tmpr2) == min(tmpr1_2,tmpr2_2) && max(tmpr1,tmpr2) < max(tmpr1_2,tmpr2_2) )
            {
                res1 = tmpr1_2;
                res2 = tmpr2_2;
            }
            return;
        }
        stack1 = tmp_stack1;
        stack2 = tmp_stack2;
        num_stack1 = tmp_num_stack1;
        num_stack2 = tmp_num_stack2;
        mid += tmp_mid;
    }
}
bool brute ()
{
    bool checked[N];
    for (int i = 0; i < N; i++ ) checked[i] = false;
    int idx;
    for (int k = 0 ; k < K; k++)
    {
        bres1 = -1;
        bres2 = -1;
        for (int i = 0; i < N; i++)
        {
            if (!checked[i])
            {
                int L = 0;
                while (i - L - 1 >= 0)
                {
                    if (!checked[i - L - 1]) L++;
                    else break;
                }
                int R = 0;
                while (i + R + 1 < N)
                {
                    if (!checked[i + R + 1]) R++;
                    else break;
                }
                int tmp = min(L,R);
                if (tmp > bres1)
                {
                    idx = i;
                    bres1 = tmp;
                    bres2 = max(L,R);
                }
                if (tmp == bres1 && max(L,R) > bres2)
                {
                    idx = i;
                    bres1 = tmp;
                    bres2 = max(L,R);
                }
            }
        }
        checked[idx] = true;
    }
    if (bres2 == max(res1,res2) && bres1 == min(res1,res2)) return true;
    return false;
}
int main(void)
{
    int test;
    std::ifstream infile("C-large.in");
    infile >> test;
    FILE * pFile;
    pFile = fopen ("output.txt","w");
    for (int i = 0; i < test; i++)
    {
        infile >> N >> K;
        find ();
 /*       if (!brute())
            cout << "false: N: " << N << " K: " << K << " res1: " << max(res1,res2) << " res2: " << min(res1,res2)
            << " bres1: " << max(bres1,bres2) << " bres2: " << min(bres1,bres2) << endl;
        else cout << "Case #" << i+1 << ": passed" << endl;*/
        fprintf(pFile, "Case #%d: %llu %llu\n",i+1,max(res1,res2),min(res1,res2));
    }
    fclose (pFile);
}
