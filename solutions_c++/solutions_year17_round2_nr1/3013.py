#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;

long double calc(long double d, long double k, long double s)
{
    return (d-k)/s;
}
int main(int argc, char** argv)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    ULLI t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        ULLI n;
        long double d, k, s;
        cin >> d >> n;
        cin >> k >> s;
        long double mass = calc(d,k,s);
        for(int j=1; j<n; j++)
        {
            cin >> k >> s;
            long double tmp = calc(d,k,s);
            if(mass<tmp)
                mass = tmp;
        }
        cout.precision(6);
        cout << "Case #" << i+1 << ": " << fixed << (long double)(d/mass) << endl;
    }
    return 0;
}
