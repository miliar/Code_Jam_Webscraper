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
#define MAXINT 2147483647

double time()
{
    return 1E-9*mach_absolute_time();
}

ifstream fin("/Users/jlee/Desktop/CodeJam/2017Q1/A-large.in");
ofstream fout("/Users/jlee/Desktop/CodeJam/2017Q1/OutputQ1L.txt");

bool even(int N)
{
    int temp = N/2;
    int temp2 = 2*temp;
    return(N==temp2);
}

int total(VB& initial)
{
    int temp=0;
    for (int i=0; i<initial.size(); ++i)
    {
        temp+=initial[i];
    }
    return temp;
}

int main()
{
    int T;
    fin >> T;
    for (int i=0; i<T; ++i)
    {
        fout << "Case #" << i+1 << ": ";
        string S;
        int K;
        fin >> S >> K;
        VB initial;
        int L = int(S.size());
        for (int j=0; j<L; ++j)
        {
            if (S[j]=='+')
            {
                initial.push_back(1);
            }
            else
            {
                initial.push_back(0);
            }
        }
        int start = total(initial);
        if (start==L)
        {
            fout << 0 << endl;
        }
        else
        {
            int counter=0;
            int flag = 0;
            while ((flag+K)<=L)
            {
                if (initial[flag]==1)
                {
                    flag++;
                }
                else
                {
                    for (int j=flag; j<flag+K; ++j)
                    {
                        initial[j]=!initial[j];
                    }
                    counter++;
                    flag++;
                }
            }
            if (total(initial)==L)
            {
                fout << counter << endl;
            }
            else
            {
                fout << "IMPOSSIBLE" << endl;
            }
        }
    }
    return 0;
}

