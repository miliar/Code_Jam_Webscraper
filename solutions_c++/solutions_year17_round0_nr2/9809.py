#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        ll n;
        cin>>n;
        ll temp=n;
        while(1)
        {
            string s1=to_string(temp);
            string s2=s1;
            sort(s1.begin(),s1.end());
            if(s1==s2)
            {
                cout<<"Case #"<<k<<":"<<" "<<temp<<endl;
                break;
            }
            temp=temp-1;
        }
    }
    return 0;
}