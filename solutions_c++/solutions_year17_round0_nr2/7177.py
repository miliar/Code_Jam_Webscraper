#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("C:\\Users\\hp\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\hp\\Desktop\\output1.txt","w",stdout);
    int t;
    cin>>t;
    int x=0;
    while(t--)
    {x++;
        string s;
        cin>>s;
        for(int i=s.length()-1;i>0;i--)
        {
            if(s[i]<s[i-1])
            {
                s[i-1]--;
                for(int j=i;j!=s.length();j++)
                {
                    s[j]='9';
                }
            }
        }
        int k=0;
        cout<<"Case #"<<x<<": ";
        for(int i=0;i!=s.length();i++)
        {
            if(k==0&&s[i]=='0')
            {

            }
            else
            {
                k=1;
                cout<<s[i];
            }
        }
        cout<<"\n";
    }
}
