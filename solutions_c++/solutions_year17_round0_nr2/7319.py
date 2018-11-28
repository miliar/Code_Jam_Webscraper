#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int t,a=1;
    cin>>t;
    while(t--)
    {
        long long int n,x;
        vector<int> v;
        cin>>n;
        x=n;
        while(x)
        {
            v.push_back(x%10);
            x=x/10;
        }
        int i=v.size()-1;

        for(int i=0;i<v.size()-1;i++)
        {
            if(v[i]<v[i+1])
            {
                v[i+1]--;
                for(int j=0;j<=i;j++)
                    v[j]=9;
            }
        }
        while(i>=0 && v[i]==0)
            {v.pop_back();i--;}
        cout<<"Case #"<<a<<": ";
        a++;
        for(int i=v.size()-1;i>=0;i--)
        {
            cout<<v[i];
        }
        cout<<endl;
    }

    return 0;
}
