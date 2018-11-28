#include <bits/stdc++.h>
#define ll long long int
#define pii pair<int,int>
#define pil pair<int,ll>
#define vll vector<ll>
#define vi vector<int>
#define cas(i) outp<<"Case #"<<i<<": "
#define d0(x) outp<<x<<" "
#define d1(x) outp<<x<<"\n"
#define d2(x,y) outp<<x<<" "<<y<<"\n"
#define d3(x,y,z) outp<<x<<" "<<y<<" "<<z<<"\n"
const ll mod=1e9+7;
using namespace std;
int main()
{
    ios_base::sync_with_stdio ( false );
    ifstream inp("input.txt");
    ofstream outp("output.txt");
    int t;inp>>t;
    for(int test=1;test<=t;test++)
    {
        cas(test);int n;inp>>n;
        int r,o,y,g,b,v;inp>>r>>o>>y>>g>>b>>v;int shru;
        if(r>y+b||y>r+b||b>r+y)
        {
           d1("IMPOSSIBLE");continue;
        }
        int last=0;
        if(r>=b&&r>=y)
        {
            outp<<"R";r--;last=0;
        }
        else if(b>=y)
        {
            outp<<"B";b--;last=1;
        }
        else
        {
            outp<<"Y";y--;last=2;
        }
        shru=last;
        for(int i=1;i<n;i++)
        {
            if(last==0)
            {
                if(b>y||(shru==1&&b==y))
                {
                     outp<<"B";b--;last=1;
                }
                else
                {
                    outp<<"Y";y--;last=2;
                }
            }
            else if(last==1)
            {
                if(r>y||(shru==0&&r==y))
                {
                      outp<<"R";r--;last=0;
                }
                else
                {
                    outp<<"Y";y--;last=2;
                }
            }
            else
            {
                if(r>b||(shru==0&&r==b))
                {
                     outp<<"R";r--;last=0;
                }
                else
                {
                     outp<<"B";b--;last=1;
                }
            }
        }
        if(shru==last)
        {
            cout<<test<<"\n";
        }
        outp<<"\n";
    }
}
