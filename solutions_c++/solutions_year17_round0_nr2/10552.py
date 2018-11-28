#include<bits/stdc++.h>
using namespace std;

bool is_ok(int n)
{
    int current;
    int prev=n%10;
    while(n>0)
    {
        current= n%10;
        n=n/10;
        if(current>prev)
        {
            return false;
        }
        prev=current;
    }
    return true;
}
int main()
{
    int t,n;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        cin>>n;
            for(int j=n; j>=0; j--)
            {
                if(is_ok(j)==true)
                {
                    cout<<"Case #"<<i<<": "<<j<<"\n";
                    break;
                }

            }
        }
}
