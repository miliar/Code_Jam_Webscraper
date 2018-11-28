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
        double tim=0;double D,N;inp>>D>>N;
        for(int i=0;i<(int)N;i++)
        {
            double ki,si;inp>>ki>>si;
            tim=max(tim,(D-ki)/si);
        }
        cas(test);
        outp<<fixed<<setprecision(6)<<D/tim<<"\n";
    }
}
