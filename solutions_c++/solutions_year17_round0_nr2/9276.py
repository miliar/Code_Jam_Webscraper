#include<bits/stdc++.h>
using namespace std;


int main()
{
    int t,j=1;
    ifstream cin("B-small-attempt0.in");
    ofstream cout("codejam1.txt");
    cin>>t;
    while(t--)
    {
        string s1,s2;
        cin>>s1;
        s2=s1;
        sort(s2.begin(),s2.end());
        if(s1==s2)
        {
            cout<<"Case #"<<j<<": "<<s1<<endl;
            j++;
        }
        else
        {
            int flag=0;
            for(int i=0;i<s1.length();i++)
            {
                if(flag==1)
                {
                    s1[i]='9';
                }
                if((s1[i]-'0'>=s1[i+1]-'0')&&(flag==0))
                {
                    //cout<<s1[i]-'0'<<endl;
                    //cout<<i<<" "<<endl;
                    s1[i]=(char)((s1[i]-1));
                    //cout<<s1[i]<<endl;
                    flag=1;
                }

            }
            int f=0;
            cout<<"Case #"<<j<<": ";
            j++;
            for(int i=0;i<s1.length();i++)
            {
                if(s1[i]=='0'&&f==0)
                    continue;
                else
                {
                    f=1;
                    cout<<s1[i];
                }
            }
            cout<<endl;
        }
    }
    return 0;
}
