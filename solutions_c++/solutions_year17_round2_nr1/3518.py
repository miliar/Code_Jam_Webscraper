#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.out","w",stdout);
    int t,n,d;
    int cs=0;
    double time,vel,pos;
    cin>>t;
    while(t--)
    {
        cs++;
        cin>>d>>n;
        double mtime = 0.0;
        for(int i=0;i<n;i++)
        {
            cin>>pos;
            cin>>vel;
            time = ((d-pos)*1.0)/vel;
            mtime=max(mtime,time);
        }
        cout<<"Case #"<<cs<<": ";
        printf("%.6f\n",d/mtime);
    }
    return 0;
}
