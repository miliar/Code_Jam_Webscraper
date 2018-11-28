#include <iostream>
#include <map>
#include <limits>
#include <stack>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cstdio>

#define rep(i,x,n) for(int i = x; i < n; ++i)
#define rrep(i,n,x) for(int i = n; i >= x; --i)
#define mod 1000000007

using namespace std;

int main()
{
    int t, m = 0;
    ifstream in;
    ofstream out;
    in.open("A.in");
    out.open("Aout.out");
    in >> t;
    while(t--)
    {
        int n,o,v,g,b,r,y;
        in >> n >> r >> o >> y >> g >> b >> v;
        if(r > (b+y) || y > (r+b) || b > (r+y))
        {
            out << "Case #" << ++m << ": IMPOSSIBLE" << endl;
            continue;
        }
        else
        {
            int a[] = {r,b,y};
            char c[3];
            if(r >= b && r >= y)
            {
                c[2] = 'R';
                a[2] = r;
                if(b >= y)
                {
                    c[1] = 'B';
                    a[1] = b;
                    c[0] = 'Y';
                    a[0] = y;
                }
                else
                {
                    c[1] = 'Y';
                    a[1] = y;
                    c[0] = 'B';
                    a[0] = b;
                }
            }
            else if(b >= r && b >= y)
            {
                c[2] = 'B';
                a[2] = b;
                if(r >= y)
                {
                    c[1] = 'R';
                    a[1] = r;
                    c[0] = 'Y';
                    a[0] = y;
                }
                else
                {
                    c[1] = 'Y';
                    a[1] = y;
                    c[0] = 'R';
                    a[0] = r;
                }
            }
            else if(y >= r && y >= b)
            {
                c[2] = 'Y';
                a[2] = y;
                if(r >= b)
                {
                    c[1] = 'R';
                    a[1] = r;
                    c[0] = 'B';
                    a[0] = b;
                }
                else
                {
                    c[1] = 'B';
                    a[1] = b;
                    c[0] = 'R';
                    a[0] = r;
                }
            }

            string s = "";
            int k = 0;
            int p = 0;
            for(int i = 0; i < n; i++)
            {
                while(a[2] != a[1])
                {
                    s += c[2];
                    s += c[0];
                    --a[2];
                    --a[0];
                    i += 2;
                }
                while(a[0] > 0)
                {
                    s += c[2];
                    s += c[1];
                    s += c[0];
                    --a[2];
                    --a[1];
                    --a[0];
                    i += 3;
                }
                while(a[2] > 0)
                {
                    s += c[2];
                    s += c[1];
                    --a[2];
                    --a[1];
                    i += 2;
                }
            }
            out << "Case #" << ++m << ": " << s << endl;
        }

    }
    return 0;
}
