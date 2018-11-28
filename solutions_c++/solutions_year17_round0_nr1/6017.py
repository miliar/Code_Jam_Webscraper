#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,flip,pos,ans=0,k,j,xxx,ctr=1;
    ofstream ofile ("C:\\Users\\P Barik\\Desktop\\output.txt");
    string s;
    cin>>t;
    while(t--)
    {
        cin>>s>>k;
        ans=0;
        flip=pos=xxx=0;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-'&&i+k<=s.length())
            {
                ans++;
                for(j=i;j<i+k&&j<s.length();j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else s[j]='-';
                }
            }
            else if(s[i]=='-')
            {
                xxx++;
            }
        }
        if(xxx==0)
        {
            cout<<"Case #"<<ctr<<": "<<ans<<"\n";
        ofile<<"Case #"<<ctr<<": "<<ans<<"\n";
        ctr++;
        }
        else
        {
            cout<<"Case #"<<ctr<<": "<<"IMPOSSIBLE\n";
            ofile<<"Case #"<<ctr<<": "<<"IMPOSSIBLE\n";
            ctr++;
        }

    }
    return 0;
}
