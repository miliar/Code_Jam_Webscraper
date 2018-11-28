#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    int tt, n;
    double d;
    cin>>tt;
    for(int t = 1; t <= tt; t++)
    {
        cin>>d>>n;
        double k, s, hp, maxtime = 0;

        for(int i = 0; i < n; i++)
        {
            cin>>k>>s;
            if((d-k)/s > maxtime)
            {
                maxtime = (d-k)/s;
                hp = k;
            }
        }

        cout<<fixed<<setprecision(6);
        cout<<"Case #"<<t<<": ";
        cout<<d/maxtime<<"\n";
    }
    return 0;
}
