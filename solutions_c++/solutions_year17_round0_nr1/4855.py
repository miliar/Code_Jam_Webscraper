#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    string s;
    int arr[1001];
    ll k;
    ll t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        int count=0;
        int flag=0;
        cin>>s;
        cin>>k;
        for(int j=0; j<s.length(); j++)
        {
            if(s[j]=='+')
            {
                arr[j]=1;
            }
            else
            {
                arr[j]=-1;
            }

        }

        for(int j=0; j<=s.length()-k; j++)
        {
           if(arr[j]==-1)
           {
               for(int l=0; l<k ; l++)
               {
                   arr[j+l]*=-1;
               }
            count++;
           }
        }

        for(int j=0; j<s.length(); j++)
        {
            if(arr[j]==-1)
            {
                flag=1;
            }
        }

        if(flag==0)
        {
            cout<<"Case #"<<i+1<<": "<<count<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
