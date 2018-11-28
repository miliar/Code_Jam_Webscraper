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
        int k;
        file>>k;
        int n=s.size();
        int x=0;
        bool ok =true;
        for(int i=0;i<n;)
        {
            //cout<<i<<" ";
            if(s[i]=='-')
            {
                if(i+k>n)
                {
                    ok=false;
                    cout<<"Case #"<<p<<": IMPOSSIBLE"<<endl;
                    break;
                }
                x++;
                int m=0;
                int flag=0;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='+')
                    {
                        if(flag==0)
                          m=j;
                        flag=1;
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                }
                if(flag==1)
                i=m;
                else
                i=i+k;
            }
            else
            {
                i++;
            }
        }
        if(ok)
        cout<<"Case #"<<p<<": "<<x<<endl;
    }
    fclose(stdout);
    return 0;
}
