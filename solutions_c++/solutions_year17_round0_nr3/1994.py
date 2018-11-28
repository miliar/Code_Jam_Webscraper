#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin("C-large.in");
    ofstream cout("C-large.out");
    int tt;
    cin>>tt;
    for (int test=1; test<=tt; test++)
    {
        map < long long, long long, greater <long long> > m;
        long long n,k;
        cin>>n>>k;
        m[n]=1;
        while(true)
        {
            long long x=m.begin()->first;
            long long cnt=m.begin()->second;
            if (cnt>=k)
            {
                cout<<"Case #"<<test<<": "<<x/2<<' '<<(x-1)/2<<'\n';
                break;
            }
            else
            {
                k-=cnt;
                m[ x/2 ]+=cnt;
                m[ x/2 - (x%2==0) ]+=cnt;
                m.erase(x);
            }
        }

    }
    return 0;
}
