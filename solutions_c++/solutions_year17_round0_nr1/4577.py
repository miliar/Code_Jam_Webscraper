#include<iostream>
#include<string>
#include<queue>
using namespace std;
typedef unsigned long long ull;
typedef pair<ull,ull> pi;
typedef pair<ull,pi> pii;
int main()
{

    int t;
    cin>>t;
    int g=1;
    while(g<=t)
    {
        string s;
        int k;
        cin>>s>>k;
        int c=0;
        for(int i=0;i<=s.length()-k;i++)
        {
            if(s[i]=='-')
            {   c+=1;
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
            //cout<<s<<endl;
        }
        int f=1;
        for(int i=0;i<s.length();i++)
            if(s[i]!='+')
            {
                f=0;
                break;

            }

        cout<<"Case #"<<g<<": ";
         if(!f)
            cout<<"IMPOSSIBLE";
         else
            cout<<c;

        cout<<endl;


       //cout<<"Case #"<<g<<": "<<mx<<" "<<mn<<endl;

       g++;
    }

}
