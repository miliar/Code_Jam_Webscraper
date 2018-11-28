#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int kk=0;kk<t;kk++)
    {
        string s,s1;
        cin>>s;
        cout<<"Case #"<<kk+1<<": ";
        int l=s.length();
        if(l==1)
        cout<<s<<endl;
        else
        {
            int f=0;
            while(f==0)
            {
                f=1;
                for(int i=0;i<l-1&&f==1;i++)
                {
                    if(s[i]>s[i+1])
                    {
                        f=0;
                        s[i]--;
                        for(int j=i+1;j<l;j++)
                        s[j]='9';
                    }
                }
            }
            int flag=0;
            for(int i=0;i<l;i++)
            {
                if((s[i]!='0')||(flag==1))
                {
                    flag=1;
                    cout<<s[i];
                }
            }
            cout<<endl;
        }
    }
    return 0;
}

