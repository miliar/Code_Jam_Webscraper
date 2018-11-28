#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <queue>
#include <deque>

using namespace std;

struct par
{
    long long val;
    long long num;
};

struct cmp
{
    bool operator()(par a, par b)
    {
        return (a.val < b.val);
    }
};

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int br = 1; br <= T; br++)
    {
        printf("Case #%i: ", br);
        priority_queue <par, deque <par>, cmp> h;
        long long n, k;
        cin >> n;
        cin >> k;
        par c;
        c.val = n;
        c.num = 1;
        h.push(c);
        long long num = 0;
        while(num < k)
        {
            c.val = h.top().val;
            c.num = 0;
            while(!h.empty() && c.val == h.top().val)
            {
                c.num += h.top().num;
                h.pop();
            }
            num += c.num;
            if(num >= k)
                printf("%lli %lli\n", c.val / 2, c.val - 1 - c.val / 2);
            if(c.val % 2)
            {
                c.val /= 2;
                c.num *= 2;
                if(c.val);
                    h.push(c);
            }
            else
            {
                c.val /= 2;
                h.push(c);
                c.val -= 1;
                if(c.val)
                    h.push(c);
            }
        }
    }
    return 0;
}
