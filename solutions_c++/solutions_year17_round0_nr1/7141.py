#include <iostream>
#include <map>
#include <limits>
#include <stack>
#include <vector>
#include <fstream>
#include <cstdlib>

#define rep(i,x,n) for(int i = x; i < n; ++i)
#define rrep(i,n,x) for(int i = n; i >= x; --i)
#define mod 1000000007

using namespace std;

int main()
{
    int t,k;
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("Aout.out");
    string s;
    in >> t;
    int p = 0;
    while(t--)
    {
        int cnt = 0;
        bool flag = true;
        in >> s >> k;
        for(int i = 0; i < s.size() - k + 1; i++)
        {
            if(s[i] == '-')
            {
                for(int j = 0; j < k; j++)
                {
                    if(s[i+j] == '-')
                        s[i+j] = '+';
                    else
                        s[i+j] = '-';
                }
                cnt++;
            }
        }

        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == '-')
            {
                flag = false;
                break;
            }
        }

        if(flag)
            out << "Case #" << ++p << ": " << cnt << endl;
        else
            out << "Case #" << ++p << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
