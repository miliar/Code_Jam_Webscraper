//
//  main.cpp
//  CodeJam #1
//
//  Created by Daniel Huang on 4/7/17.
//  Copyright (c) 2017 Daniel Huang. All rights reserved.
//
#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;
void makeStallsArray(char stalls[], long long N) //makes the initial array
{
    for(long long i = 0LL; i < (N+2); i++) //only fills the last two elements with 'o'
    {
        stalls[i] = '.';
        if(i == 0 || i == (N+1))
        {
            stalls[i] = 'o';
        }
    }
}
long long getLs(char stalls[], long long N, long long stallindex) //get array, get stall, return Ls
{
    long long varLs = 0LL;
    for(long long i = stallindex-1; i>0; i--) //goes from right to left starting from stallindex-1 and ends on 1
    {
        if(stalls[i] == 'o')
        {
            break;
        }
        varLs++;
    }
    return varLs;
}
long long getRs(char stalls[], long long N, long long stallindex) //get array, get which stall, return Rs
{
    long long varRs = 0LL;
    for(long long i = stallindex+1; i < (N+1); i++) //goes from left to right starting from stallindex+1 and ends on N
    {
        if(stalls[i] == 'o')
        {
            break;
        }
        varRs++;
    }
    return varRs;

}
void arrayofMinsMaxes(char stalls[], long long N, long long mins[], long long max[]) //makes and array with the mins and maxes
{
    for(long long i = 0LL; i < (N+2); i++)
    {
        mins[i] = fmin(getLs(stalls, (N+2), i), getRs(stalls, (N+2), i));
        max[i] = fmax(getLs(stalls, (N+2), i), getRs(stalls, (N+2), i));
        if(stalls[i] == 'o')
        {
            mins[i] = 0LL;
            max[i] = 0LL;
        }
    }
}
long long chooseStall(char stalls[], long long mins[], long long max[], long long N) //chooses and fills that stall
{
    long long index = 0;
    for(long long b = N+1; b > -1; b--)
    {
        if(stalls[b] == '.')
        {
            index = b;
        }
            
    }
    for(long long i = 1LL; i < (N+1); i++)
    {
        bool notFilled = (stalls[i]!='o');
        if(notFilled && (mins[i] == mins[index]))
        {
            if((max[i] > max[index]))
            {
                index = i;
            }
        }
        if(notFilled &&(mins[i] > mins[index]))
        {
            index = i;
        }
        
    }
    stalls[index] = 'o';
    return index;
}
int main()
{
    ifstream in;
    ofstream out;
    in.open("/Users/danielhuang/Downloads/C-small-1-attempt0.in");
    out.open("/Users/danielhuang/Desktop/Tester/CodeJam/CodeJam #1/CodeJam #1/output.txt");
    int numberofTests;
    in >> numberofTests;
    string* ptr1 = new string[numberofTests];
    for(int i = 0; i < numberofTests; i++)
    {
        long long n;
        in >> n;
        long long k;
        in >> k;
        char * ptr2 = new char[n+2];
        makeStallsArray(ptr2, n);
        long long * ptrMin = new long long[n+2];
        long long * ptrMax = new long long[n+2];
        arrayofMinsMaxes(ptr2, n , ptrMin, ptrMax);
        long long maxLsRs = 0;
        long long minLsRs = 0;
        for(long long j = 0LL; j < k; j++)
        {
            long long l = chooseStall(ptr2, ptrMin, ptrMax, n);
            if(j == k - 1 )
            {
                maxLsRs = ptrMax[l];
                minLsRs = ptrMin[l];
            }
            arrayofMinsMaxes(ptr2,n, ptrMin,ptrMax);
        }
        
        ptr1[i].append(to_string(maxLsRs));
        ptr1[i] += " ";
        ptr1[i].append(to_string(minLsRs));
        delete []ptr2; delete []ptrMax; delete []ptrMin;
    }
    for(int a = 0; a < numberofTests; a++)
    {
        out << "Case #" << (a+1) << ": " << ptr1[a] << endl;
    }
    delete []ptr1;
    in.close();
    out.close();
    return 0;
}