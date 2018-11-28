#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s;
        cin>>s;
        while(!is_sorted(s.begin(),s.end()))
        {
            long long x=stoll(s);
            x-=1;
            s=to_string(x);

        }
        cout<<"Case #"<<i<<": "<<s<<endl;
    }
    return 0;
}