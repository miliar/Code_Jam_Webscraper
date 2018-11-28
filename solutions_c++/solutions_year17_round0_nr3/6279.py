#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct interval
{
    long long int inc, sf;
    inline bool operator<(const interval& i) const
    {
        if((-inc+sf)/2 < (-i.inc+i.sf)/2)
            return true;
        if((-inc+sf)/2 == (-i.inc+i.sf)/2)
        {
            if((-inc+sf)%2 == 1 && (-i.inc+i.sf)%2 == 0)
                return false;
            if((-inc+sf)%2 == 0 && (-i.inc+i.sf)%2 == 1)
                return true;
            return (i.inc < i.inc);
        }
        return false;
    }
};

priority_queue<interval> q;
interval p, x;

int main()
{
    long long int i, n, t, c = 1, m, min, max, k;
    ifstream f("stalls.in");
    ofstream g("stalls.out");
    f >> t;
    while(t--)
    {
        g << "Case #" << c << ": ";
        c++;
        cout << c << "\n";
        f >> n >> k;
        p.inc = 1;
        p.sf = n;
        while(!q.empty())
            q.pop();
        q.push(p);
        //make_heap(q.begin(), q.end(), cmp);
        for(i=1; i<=k; i++)
        {

            p = q.top();
            //pop_heap(q.begin(), q.end(), cmp);
            q.pop();

            m = (p.inc + p.sf) / 2;
            if(p.inc < p.sf)
            {
                x.inc = p.inc;
                x.sf = m-1;
                if(x.inc <= x.sf)q.push(x);
                //push_heap(q.begin(), q.end(), cmp);

                x.inc = m+1;
                x.sf = p.sf;
                if(x.inc <= x.sf)q.push(x);
                //push_heap(q.begin(), q.end(), cmp);
            }
        }
        min = m-p.inc;
        max = p.sf-m;
        if(min > max)
            swap(min, max);
        g << max << " " << min << "\n";
    }
}
