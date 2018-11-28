#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>
#include <mach/mach_time.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <iomanip>
#include <string>
#include <queue>
#include <math.h>
using std::list;
using std::cout;
using std::cin;
using std::vector;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::fstream;
using std::sort;
using std::min;
using std::string;
using std::queue;

typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef unsigned long long ULL;
#define MAXINT 2147483647

double time()
{
    return 1E-9*mach_absolute_time();
}

ifstream fin("/Users/jlee/Desktop/CodeJam/2017Q2/B-large.in");
ofstream fout("/Users/jlee/Desktop/CodeJam/2017Q2/OutputQ2L.txt");

VI digitss(ULL N)
{
    VI nums;
    while (N>0)
    {
        long long tee = N/10;
        tee*=10;
        int t=int(N-tee);
        //int t=temp%10;
        nums.push_back(t);
        N/=10;
    }
    return nums;
}

bool tidy(ULL N)
{
    VI t=digitss(N);
    if (t.size()>1)
    {
        for (int i=0; i<t.size()-1; ++i)
        {
            if (t[i]<t[i+1])
            {
                return FALSE;
            }
        }
    }
    return TRUE;
}

ULL largething(int po)
{
    ULL t=1;
    for (int i=0; i<po; ++i)
    {
        t*=10;
    }
    return t;
}

ULL funct(VI digs)
{
    ULL answer=0;
    for (int i=0; i<digs.size(); ++i)
    {
        answer+=((digs[i])*(largething(i)));
    }
    return answer;
}

VI subvec(VI digs, int place)
{
    VI answer;
    for (int i=place; i<=digs.size()-1; ++i)
    {
        answer.push_back(digs[i]);
    }
    return answer;
}

ULL largest(ULL N)
{
    while (N>0)
    {
        if (tidy(N))
        {
            return N;
        }
        N--;
    }
    return 1;
}

int main()
{
    int T;
    fin >> T;
    for (int i=0; i<T; ++i)
    {
        ULL N;
        fin >> N;
        VI porary=digitss(N);
        if (tidy(funct(porary)))
        {
            fout << "Case #" << i+1 << ": " << N << endl;
        }
        else
        {
            int flag=int(porary.size()-1);
            if (flag==0)
            {
                fout << "Case #" << i+1 << ": " << N << endl;
            }
            else
            {
                while(tidy(funct(subvec(porary,flag)))==TRUE)
                {
                    flag--;
                }
                while(tidy(funct(subvec(porary,flag)))==FALSE)
                {
                    porary[flag]=9;
                    flag++;
                    porary[flag]-=1;
                }
                if (flag>=1)
                {
                    for (int j=flag-1; j>=0; --j)
                    {
                        porary[j]=9;
                    }
                }
                ULL sumbit=funct(porary);
                fout << "Case #" << i+1 << ": " << sumbit << endl;
            }
        }
    }
    return 0;
}

