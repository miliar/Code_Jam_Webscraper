#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stdio.h>
#include <fstream>
using namespace std;
int arrN[20];
int lenN;
unsigned long long N;
unsigned long long find ()
{
    if (N < 10) return N;
    lenN = 0;
    int tmp[20];
    while (N > 0)
    {
        tmp[lenN] = N % 10;
        N /= 10;
        lenN++;
    }
    for (int i = 0 ; i < lenN; i++)
    {
        arrN[i] = tmp[lenN-i-1];
    }
    bool negative = false;
    bool positive = false;
    for (int i = 0 ; i < lenN-1; i++)
    {
        if (arrN[i] > arrN[i+1])
        {
            arrN[i]--;
            for (int j = i-1; j >= 0; j--)
            {
                if (arrN[j] > arrN[j+1] )
                {
                    arrN[j] = arrN[j+1];
                    arrN[j+1] = 9;
                }
            }
            for (int j = i+1; j < lenN; j++)
            {
                arrN[j] = 9;
            }
            if (arrN[0] == 0)
            {
                negative = true;
                break;
            }
            else
            {
                positive = true;
                break;
            }
        }
    }
    unsigned long long res = 0;
    if (positive)
    {
        for (int i =0; i < lenN; i++)
            res = res * 10 + arrN[i];
    }
    if (negative)
    {
        for (int i =0; i < lenN - 1; i++)
            res = res * 10 + 9;
    }
    if (!negative && !positive)
    {
        for (int i =0; i < lenN; i++)
            res = res * 10 + arrN[i];
    }
    return res;
}
bool brute(int num)
{
    int prev = num % 10;
    int cur; num /= 10;
    while (num)
    {
        cur = num % 10;
        num /= 10;
        if (cur > prev) return false;
        prev = cur;
    }
    return true;
}
int main(void)
{
    int test;
    std::ifstream infile("B-large.in");
    infile >> test;
    FILE * pFile;
    pFile = fopen ("output.txt","w");
    for (int i = 0; i < test; i++)
    {
        infile >> N;
        unsigned long long res = find ();
        fprintf(pFile, "Case #%d: %llu\n",i+1,res);
    }
    fclose (pFile);
}
