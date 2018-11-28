#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    long long int n;
    int t,test,i,j,flag=0;
    string s;
    cin>>test;
    t=test;
    while(test--)
    {
        cin>>n;
        flag=0;
        s=to_string(n);
        if(s.length()!=1)
        {
            for(i=0; i<s.length(); i++)
            {
                if(flag==1)
                {
                    s[i]='9';
                }
                if(s[i]>s[i+1] && i<s.length()-1 && flag!=1)
                {
                    s[i]=s[i]-1;
                    j=i;
                    flag=1;
                }
            }

            while(j-1>=0 && s[j]<s[j-1])
            {
                s[j-1]=s[j-1]-1;
                s[j]='9';
                j--;
            }
        }
            if(s[0]=='0')
                s[0]='\0';
            cout<<"Case #"<<t-test<<": "<<s<<endl;

    }
    return 0;
}
