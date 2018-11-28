#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        long long n,k,l,r;
        cin>>n>>k;
        while(k)
        {
            n--;
            l=n/2;
            r=(n+1)/2;
            k--;
            if(k%2)
                n=r;
            else
                n=l;
            k=(k+1)/2;
        }
        cout<<"Case #"<<tc<<": "<<r<<" "<<l<<endl;
    }
}
