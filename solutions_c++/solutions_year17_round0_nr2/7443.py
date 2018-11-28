#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
    freopen("ab.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,naruto=1;
    cin>>t;
    while(t--)
    {
        long long int n,N;
        cin>>n;
        N=n;
        vector<int> v;
        while(n!=0)
        {
            int ans=n%10;
            v.push_back(ans);
            n=n/10;

        }
        reverse(v.begin(),v.end());

        for(int i=v.size()-1;i>0;i--)
        {
            if(v[i-1]>v[i])
            {
                v[i-1]=v[i-1]-1;
                for(int j=i;j<v.size();j++)
                    v[j]=9;
            }
        }
        if(v[0]==0)
        {
            cout<<"Case #"<<naruto++<<": ";
            for(int i=1;i<v.size();i++)
                cout<<v[i];
            cout<<endl;
        }
        else
            {
            cout<<"Case #"<<naruto++<<": ";
            for(int i=0;i<v.size();i++)
                cout<<v[i];
            cout<<endl;
        }
    }
    return 0;
}
