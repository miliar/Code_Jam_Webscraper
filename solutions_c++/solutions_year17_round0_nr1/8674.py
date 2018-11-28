#include <iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("submit.out","w",stdout);
    int t,k,jz,v,sizee,i;
    cin>>t;
    string s;
    int count,flag=0;
    for(v=0;v<t;v++)
    {
        cin>>s>>k;
        sizee=k;
        count=0;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-' && i+k-1<s.size())
            {
                jz=i;
                sizee=k;
                while(sizee!=0)
                {
                    sizee--;
                    jz++;
                }

                for(sizee=i;sizee<jz;sizee++)
                {
                    if(s[sizee]=='+')
                        s[sizee]='-';
                    else
                    s[sizee]='+';

                }
                count++;
            }
        }
        flag=0;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')
                flag=1;
        }
        if(flag==1)
            cout<<"Case #"<<v+1<<": "<<"IMPOSSIBLE\n";
        else
        cout<<"Case #"<<v+1<<": "<<count<<"\n";

    }
    return 0;
}
