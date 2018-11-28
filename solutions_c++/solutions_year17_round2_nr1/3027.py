#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    double T;
    int t=0;
    double d,n;
    double k,s;
    double Maxtime,Time;
    bool bol=0;
    cin>>T;
    while(T--)
    {
        bol=0;
        cin>>d>>n;
        while(n--)
        {
            cin>>k>>s;
            if(!bol){Maxtime=(d-k)/s;bol=1;}
            else
            {
                Time=(d-k)/s;
                if(Time-Maxtime>1e-7)Maxtime=Time;
            }
        }
        cout<<"Case #"<<++t<<": "<<fixed<<setprecision(8)<<d/Maxtime<<endl;
    }
    return 0;
}
