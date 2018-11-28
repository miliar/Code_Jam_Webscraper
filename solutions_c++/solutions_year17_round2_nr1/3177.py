#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
typedef long double ll;
ll t;
ll d, n;
ll k, s;
int main()
{
    ifstream fin ("Downloads/horse2.in");
    ofstream fout ("horse3.out");
    fin >> t;
    for (int i=1; i<=t; i++)
    {
        ll ans=0;
        fin >> d >> n;
        for (int j=0; j<n; j++)
        {
            fin >> k >> s;
            ans=max(ans, (d-k)/s);
        }
        fout << "Case #" << i << ": ";
        fout << fixed << setprecision(8) << ((long double) (d))/ans;
        fout << endl;
    }
}
