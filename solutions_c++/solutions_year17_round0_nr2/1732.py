//
//  main.cpp
//  B-Tidy-Numbers
//
//  Created by Volodymyr Polosukhin on 08/04/2017.
//  Copyright © 2017 Volodymyr Polosukhin. All rights reserved.
//
#include <cassert>
#include <cstdio>
#include <algorithm>

using namespace std;

bool isTidy(long long n)
{
    char buffer[42];
    
    sprintf(buffer, "%lld", n);
    
    return is_sorted(buffer, buffer+strlen(buffer));
}

long long solveSmall(const char number[])
{
    long long n;
    
    sscanf(number, "%lld", &n);
    
    long long tested;
    
    for (tested = n; !isTidy(tested); --tested);
    
    return tested;
}

long long solveLarge(char number[])
{
    int i;
    
    for (i = 0; number[i+1] && number[i] <= number[i+1]; ++i);
    
    if (number[i+1])
    {
        int j;
        
        for (j = i; j >= 0 && number[j] == number[i]; --j);

        if (number[j] != number[i])
        {
            ++j;
        }
        
        assert(number[j] >= '1');
        --number[j];
        
        for (int k = j+1; number[k]; ++k)
        {
            number[k] = '9';
        }
    }
    
    long long answer;
    
    sscanf(number, "%lld", &answer);
    
    return answer;
}

void stress()
{
    const int MAXN = (int)1e8;
    
    long long tidy = 0;
    
    for (long long n = 1; n <= MAXN; ++n)
    {
        char buffer[42];
        sprintf(buffer, "%lld", n);
        
        if (isTidy(n))
        {
            tidy = n;
        }
        
        long long output = solveLarge(buffer);
        
        assert(output == tidy);
    }
}

int main(int argc, const char * argv[]) {
//    stress();
    
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
//    freopen("B-example.in", "r", stdin);
//    freopen("B-example.out", "w", stdout);
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    
    scanf("%d", &t);
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        char n[42];
        
        scanf("%s", n);
        
        printf("Case #%d: %lld\n", testcase, solveLarge(n));
    }
    
    return 0;
}
