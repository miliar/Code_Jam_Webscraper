#include<bits/stdc++.h>
#define pb push_back
using namespace std;
int main()
{
    ofstream file;
    file.open("/home/sanban/Downloads/filename.txt");
    int tc;
    cin>>tc;
    for(int z=1;z<=tc;++z)
    {
        int n;
        double d;
        cin>>d>>n;
        double k[n],s[n];
        for(int i=0;i<n;++i)
        cin>>k[i]>>s[i];
        int mins[n];
        mins[n-1]=n-1;
        for(int i=n-2;i>=0;--i)
        {
            if(s[i]<=s[mins[i+1]])
            {
                mins[i]=i;
            }
            else
                mins[i]=mins[i+1];
        }
        double maxtime=0.000000;
        for(int i=0;i<n;++i)
        {
            if(mins[i]==i)
            maxtime=max(maxtime,(d-k[i])/s[i]);
            else maxtime=max(maxtime,(k[mins[i]]-k[i])/(s[i]-s[mins[i]]));
        }
        double ans=d/maxtime;
        file << "Case #" << z << ": " << fixed <<   setprecision(6) << ans << "\n";
    }
    file.close();
    return 0;
}
