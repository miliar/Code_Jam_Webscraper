#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;


ifstream fin ("input.in");
ofstream fout("ouput.out");

int  n, nrt;
double t, d, k, s, v;
int main()
{
    ios_base::sync_with_stdio(false);fin.tie(0);
    int i;
    fin>>nrt;
    for(int T=1; T<=nrt; ++T)
    {
        fin>>d>>n;
        fin>>k>>s;
        t=(d-k)/s;
        v=d/t;
        for(i=2; i<=n; ++i)
        {
            fin>>k>>s;
            t=(d-k)/s;
            if(v > (d/t) )
                v=d/t;
        }
        fout<<"Case #"<<T<<": "<<fixed<<setprecision(6) <<v<<'\n';
    }
    return 0;
}
