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
    ifstream infile;
    ofstream outfile;
    infile.open("A-large.in");
    outfile.open("Aout.out");
    string st;
    infile >> t;
    int a = 0;
    while(t--)
    {
        int count = 0;
        bool flag = true;
        infile >> st >> k;
        for(int i = 0; i < st.size() - k + 1; i++)
        {
            if(st[i] == '-')
            {
                for(int j = 0; j < k; j++)
                {
                    if(st[i+j] == '-')
                        st[i+j] = '+';
                    else
                        st[i+j] = '-';
                }
                count++;
            }
        }

        for(int i = 0; i < st.length(); i++)
        {
            if(st[i] == '-')
            {
                flag = false;
                break;
            }
        }

        if(flag)
            outfile << "Case #" << ++a << ": " << count << endl;
        else
            outfile << "Case #" << ++a << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
