
//  main.cpp
//  B-Tidy-Numbers
//
//  Created by Volodymyr Polosukhin on 08/04/2017.
//  Copyright © 2017 Volodymyr Polosukhin. All rights reserved.
//

#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

pair < long long, long long > solveSmall1(long long n, long long k)
{
    vector < bool > occupied(n+2, false);
    vector < long long > ls(n+2, 0), rs(n+2, 0);
    occupied[0] = occupied[n+1] = true;
    
    long long y, z;
    
    for (long long person = 0; person < k; ++person)
    {
        long long leftOccupied;
        
        for (long long stall = 0; stall <= n+1; ++stall)
        {
            if (occupied[stall])
            {
                leftOccupied = stall;
            }
            else
            {
                ls[stall] = stall - 1 - leftOccupied;
            }
        }
        
        long long rightOccupied;
        
        for (long long stall = n+1; stall >= 0; --stall)
        {
            if (occupied[stall])
            {
                rightOccupied = stall;
            }
            else
            {
                rs[stall] = rightOccupied - (stall + 1);
            }
        }
        
        long long chosenStall, chosenMin = -1, chosenMax;
        
        for (long long stall = 0; stall <= n+1; ++stall)
        {
            long long currentMin = min(ls[stall], rs[stall]);
            long long currentMax = max(ls[stall], rs[stall]);
            
            if (!occupied[stall] &&
                (chosenMin < currentMin ||
                 (chosenMin == currentMin && chosenMax < currentMax)))
            {
                chosenStall = stall;
                chosenMin = currentMin;
                chosenMax = currentMax;
            }
        }
        
        occupied[chosenStall] = true;
        
        y = chosenMax;
        z = chosenMin;
    }
    
    return make_pair(y, z);
}

pair < long long, long long > solveSmall2(long long n, long long k)
{
    typedef pair < long long, long long > Segment;
    
    priority_queue<Segment> q;
    q.emplace(n, -1);
    
    long long y, z;
    
    for (long long person = 0; person < k; ++person)
    {
        Segment segment = q.top();
        q.pop();
        
        long long left = -segment.second - 1;
        long long right = -segment.second + segment.first;
        long long stall = -segment.second + (segment.first + 1) / 2LL - 1;
        long long ls = stall - left - 1;
        long long rs = right - stall - 1;
        
        if (ls)
            q.emplace(ls, -(left+1));
        
        if (rs)
            q.emplace(rs, -(right-1));
        
        y = max(ls, rs);
        z = min(ls, rs);
    }
    
    return make_pair(y, z);
}

pair < long long, long long > solveLarge(long long n, long long k)
{
    map < long long, long long > segments;
    segments.emplace(n, 1);
    
    while (k > 0)
    {
        while (0 == segments.rbegin()->second)
        {
            segments.erase(segments.rbegin()->first);
        }
        
        long long length = segments.rbegin()->first;
        long long count = segments.rbegin()->second;
        long long ls = (length - 1LL) / 2LL;
        long long rs = length / 2LL;
        
        assert(ls + rs + 1 == length);
        
        if (k <= count)
        {
            return make_pair(max(ls, rs), min(ls, rs));
        }
        
        k -= count;
        
        segments.erase(length);
        
        if (ls)
        {
            segments[ls] += count;
        }
        
        if (rs)
        {
            segments[rs] += count;
        }
    }
    
    assert(false);
}

void generate()
{
    FILE* fh = fopen("C-stress.in", "w");
    
    int t = 100;
    
    fprintf(fh, "%d\n", t);
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        fprintf(fh, "%lld %lld\n", (long long)1e18 - testcase + 1, (long long)1e18 - testcase + 1);
    }
    
    fclose(fh);
}


int main(int argc, const char * argv[]) {
//    freopen("C-small-2-attempt0.in.txt", "r", stdin);
//    freopen("C-small-2-attempt0.out", "w", stdout);
//    freopen("C-small-1-attempt0.in.txt", "r", stdin);
//    freopen("C-small-1-attempt0.out", "w", stdout);
//    freopen("C-example.in", "r", stdin);
//    freopen("C-example.out", "w", stdout);
    
//    generate();
//    
//    freopen("C-stress.in", "r", stdin);
//    freopen("C-stress.out", "w", stdout);

    freopen("C-large.in.txt", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    int t;
    
    scanf("%d", &t);
    
    for (int testcase = 1; testcase <= t; ++testcase)
    {
        long long n, k;
        
        scanf("%lld%lld", &n, &k);
        
        auto solution = solveLarge(n, k);
        
        printf("Case #%d: %lld %lld\n", testcase, solution.first, solution.second);
    }
    
    return 0;
}
