#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream file("in.txt");
    freopen ("output.txt","w",stdout);
    int t;
    file>>t;
    for(int p=1;p<=t;p++)
    {
        string s;
        file>>s;
        int n=s.size();
        for(int i=0;i<n-1;i++)
        {
            if(s[i]>s[i+1])
            {
                char c=s[i];
                for(int j=i;j>=0;j--)
                {
                    if(c==s[j-1]&&j!=0)
                    {
                        s[j]='9';
                    }
                    else
                    {
                        int x=s[j]-'0';
                        x=x-1;
                        s[j]=x+'0';
                        break;
                    }
                }
                for(int j=i+1;j<n;j++)
                {
                    s[j]='9';
                }
                break;
            }
        }
        int u=0;
        cout<<"Case #"<<p<<": ";
        for(int i=0;i<n;i++)
        {
            if(s[i]>'0'||u==1)
            {
                cout<<s[i];
                u=1;
            }
        }
        cout<<endl;
    }
    fclose(stdout);
return 0;
}
