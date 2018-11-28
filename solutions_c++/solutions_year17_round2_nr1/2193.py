#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream inp;
    ofstream out;
    inp.open("input.txt");
    out.open("output.txt");
    int T,d,n,k,s;
    inp>>T;
    for(int t=1;t<=T;t++)
    {
        inp>>d>>n;
        double time=-1,ans;
        for(int i=0;i<n;i++)
        {
            inp>>k>>s;
            int dis = d-k;
            double tm = (double)dis/s;
            time = max(time,tm);
        }
        ans = d/time;
        out<<fixed<<setprecision(7);
        out<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
