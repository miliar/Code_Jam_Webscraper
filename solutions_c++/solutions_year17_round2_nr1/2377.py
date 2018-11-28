#include<bits/stdc++.h>
using namespace std;
double pos[1005];
double vel[1005];
int main()
{
    int t;
    cin>>t;
    int n;
    double d;
    for(int p=1;p<=t;p++)
    {
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            cin>>pos[i]>>vel[i];
        }
        double time = (d-pos[n-1])/vel[n-1];
        for(int i=n-2;i>=0;i--)
        {
            double t = (d-pos[i])/vel[i];
            if(t>time)
                time = t;
        }
        printf("Case #%d: 0.6%f\n",p,d/time);
        memset(pos,0,sizeof pos);
        memset(vel,0,sizeof vel);
    }
}
