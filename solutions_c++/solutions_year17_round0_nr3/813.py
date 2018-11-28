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
using std::max;
using std::string;
using std::queue;

typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<VI> VVI;
typedef unsigned long long ULL;
typedef vector<ULL> VULL;
#define MAXINT 2147483647

double time()
{
    return 1E-9*mach_absolute_time();
}

ifstream fin("/Users/jlee/Desktop/CodeJam/2017Q3/C-large.in");
ofstream fout("/Users/jlee/Desktop/CodeJam/2017Q3/OutputQ3L.txt");

int logar(ULL N)
{
    int counter=0;
    while (N>1)
    {
        N/=2;
        counter++;
    }
    return counter;
}

ULL largething(int po)
{
    ULL t=1;
    for (int i=0; i<po; ++i)
    {
        t*=2;
    }
    return t;
}

bool even(ULL N)
{
    ULL temp=N/2;
    temp*=2;
    return(temp==N);
}

int main()
{
    int T;
    fin >> T;
    for (int i=0; i<T; ++i)
    {
        ULL N,K;
        fin >> N >> K;
        ULL n=N;
        int p = logar(K)+1;
        for (int j=0; j<p-1; ++j)
        {
            n/=2;
        }
        if (even(n))
        {
            n/=2; //no pair of this
            ULL m;
            if (n==1)
            {
                m=0;
            }
            else
            {
                m=n-1;
            }
            ULL sum=N+1-largething(p);
            ULL x=sum-(m*(largething(p)));
            K-=largething(p-1);
            if (K<x)
            {
                fout << "Case #" << i+1 << ": " << n << " " << m << endl;
            }
            else
            {
                fout << "Case #" << i+1 << ": " << m << " " << m << endl;
            }
        }
        else
        {
            n/=2; //pair of this
            ULL m;
            if (n==0)
            {
                m=0;
            }
            else
            {
                m=n-1;
            }
            ULL sum=N+1-largething(p);
            ULL x=(n*(largething(p)))-sum;
            ULL y=largething(p-1)-x;
            K-=largething(p-1);
            if (K>=y)
            {
                fout << "Case #" << i+1 << ": " << n << " " << m << endl;
            }
            else
            {
                fout << "Case #" << i+1 << ": " << n << " " << n << endl;
            }
        }
        
        /*
        ULL m=n-1;
        ULL sum=N+1-(largething(p));
        
        nx+(n-1)(2^p-1-x)=sum;
        
        if (K>(N/2)+1)
        {
            fout << "Case #" << i+1 << ": " << 0 << " " << 0 << endl;
        }
        else
        {
            VULL inn;
            inn.push_back(N/2); //maximum
            if ((2*(N/2))==(N))
            {
                inn.push_back(N/2);
                inn.push_back((N/2)-1);
            }
            else
            {
                inn.push_back(N/2);
                inn.push_back(N/2);
            }
            while (K>1)
            {
                inn=choices(inn);
                if (inn[inn.size()-2]==0)
                {
                    break;
                }
                K--;
            }
            fout << "Case #" << i+1 << ": " << inn[inn.size()-2] << " " << inn[inn.size()-1] << endl;
        }
         */
    }
    return 0;
}

