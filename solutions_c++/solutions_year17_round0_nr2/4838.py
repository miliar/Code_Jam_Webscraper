#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    ll t;
    ll sum=0;
    string s;
    int arr[20];
    cin>>t;
    for(int i=0; i<t; i++)
    {
        ll sum=0;
        cin>>s;
        for(int j=0; j<s.length(); j++)
        {
            arr[j]=s[j] - 48;
        }
        for(int j=s.length()-1; j>0; j--)
        {
            if(arr[j]<arr[j-1])
            {
                arr[j-1] = arr[j-1] - 1;

                for(int k=j; k<s.length(); k++)
                {
                    arr[k]=9;
                }
            }
        }
        for(int j=0; j<s.length(); j++)
        {
            sum = 10*sum + arr[j];
        }
        cout<<"Case #"<<i+1<<": "<<sum<<endl;
    }
}
