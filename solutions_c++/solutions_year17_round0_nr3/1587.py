#include<bits/stdc++.h>
//#include<conio.h>
using namespace std;

int main()
{
    freopen("000.in","r",stdin);
    freopen("0002.txt","w",stdout);

    long long t,n,l,k,i;
    map<long long, long long> m;

    cin>>t;

    for(l=1;l<=t;l++)
    {
        cin>>n>>k;

        m.clear();

        m[n]=1;

        i=0;

        while(i+m[n]<k)
        {
            i+=m[n];
            if(n%2==0)
            {
                m[n/2]+=m[n];
                m[n/2-1]+=m[n];
            }
            else
            {
                m[n/2]+=m[n];
                m[n/2]+=m[n];
            }
            auto it=m.find(n);
            m.erase(it);
            n=(m.rbegin())->first;
        }

        cout<<"Case #"<<l<<": ";
        if(n%2==0)
            cout<<n/2<<" "<<n/2-1<<endl;
        else
            cout<<n/2<<" "<<n/2<<endl;

    }

    return 0;
}
