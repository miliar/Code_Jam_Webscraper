#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int t1=0;t1<t;t1++)
    {
        string s;
        cin>>s;
        int f=0;
        int n=s.size();
        while(f==0)
        {
            f=1;
            for(int i=0;i<n-1&&f==1;i++)
            {
                if(s[i]>s[i+1])
                {
                    f=0;
                    s[i]--;
                    for(int j=i+1;j<n;j++)
                    s[j]='9';
                }
            }
        }
        int fl=0;
        for(int i=0;i<n;i++)
        {
            if((s[i]!='0')||(fl==1))
            {
                fl=1;
                cout<<s[i];
            }
        }
        cout<<endl;
        
    }
    return 0;
}
