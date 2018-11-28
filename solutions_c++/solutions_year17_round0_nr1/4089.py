#include<iostream>
using namespace std;
main()
{
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        string s;int k;
        cin>>s>>k;
        int l = s.length(), ans = 0;
        bool pos = true;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                int tj = i+k;
                if(tj>l)
                {
                    pos = false;
                    break;
                }
                ans += 1;
                for(int j=i;j<tj;j++)
                    if(s[j]=='+')
                        s[j]='-';
                    else
                        s[j]='+';
            }
        }
        cout<<"Case #"<<ii<<": ";
        if(pos)
            cout<<ans;
        else
            cout<<"IMPOSSIBLE";
        cout<<endl;
    }
}

