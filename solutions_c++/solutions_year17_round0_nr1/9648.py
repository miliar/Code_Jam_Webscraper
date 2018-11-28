#include<bits/stdc++.h>

using namespace std;

int main()
{

freopen("A-large.in", "r", stdin);
    freopen("A-o0.txt", "w", stdout);

    int cases=1,t,k;
    cin>>t;

    string s;

    while(t--)
    {
        cin>>s>>k;
        int c=0;

        for(int i=0;i<=(s.size()-k);i++)
        {
            if(s[i]=='-')
            {
                //cout<<i<<endl;
                c++;
                for(int j=i;j<(i+k);j++)
                {
                    if(s[j]=='-')
                         s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }

         int ans=1;

    for(int i=0;i<s.size();i++)
         if(s[i]=='-')
             ans=0;

    if(ans==0)
         cout<<"Case "<<"#"<<cases<<": "<<"IMPOSSIBLE"<<endl;
    else
       cout<<"Case "<<"#"<<cases<<": "<<c<<endl;

       cases++;
    }





return 0;
}
