#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("tidy_numbers.txt","r",stdin);
    freopen("tidy_numbers.out","w",stdout);
    long long t,n;
    cin>>t;
    for(int k = 1;k<=t;k++)
    {
        cin>>n;
        vector <int> v;
        long long p = n;
        int a;
        while(p)
        {
            a = p%10;
            p /= 10;
            v.push_back(a);
            if(a<p%10)
            {
                p--;
                for(int i = 0;i<v.size();i++)
                {
                    v[i] = 9;
                }
            }
        }
        p = 0;
        for(int i = v.size()-1;i>=0;i--)
        {
            p *= 10;
            p += v[i];
        }
        cout<<"Case #"<<k<<": "<<p<<endl;
    }
    return 0;
}
