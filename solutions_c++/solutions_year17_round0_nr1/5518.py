#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t,tc=1;
    cin>>t;
    while (t--)
    {
        string s;
        cin>>s;
        int k,i;
        cin>>k;
        int n=s.length(),over=0,cnt=0;
        for (i=0;i<n;i++)
        {
            int p;
            if (s[i]=='-')
            {
                if ((i+k)>n)
                {
                    over=1;
                    break;
                }
                for (p=1;p<=k;p++)
                {

                    if (s[i+p-1]=='-')
                        s[i+p-1]='+';
                    else
                        s[i+p-1]='-';

                }
                cnt++;
            }
        }
        cout<<"Case #"<<tc<<": ";
        if (over==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
        cout<<cnt<<endl;
        tc++;
    }
    return 0;
}
