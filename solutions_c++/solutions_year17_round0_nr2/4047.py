#include<iostream>
using namespace std;
main()
{
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        string s;
        cin>>s;
        int l = s.length(),ci = l,i,j;
        for(i=l-1;i>0;i--)
        {
            if(s[i-1]>s[i])
            {
                s[i-1] -= 1;
                ci = i;
            }
        }
        cout<<"Case #"<<ii<<": ";
        for(j = 0;j < ci;j++)
        {
            if(s[j]=='0')
                continue;
            cout<<s[j];
        }
        for(j = ci;j < l;j++)
            cout<<'9';
        cout<<endl;
    }
}
