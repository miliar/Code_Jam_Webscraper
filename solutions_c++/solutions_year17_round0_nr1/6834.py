#include<bits/stdc++.h>
using namespace std;
int main()
{
     ifstream cin("pancako.in");
    ofstream cout("pancako.out");
    long long i,len,t,i2,z,we=0,x;
    string s;
    cin>>t;
    while(t--)
    {

        cout<<"Case #"<<++we<<": ";
        z=0;
        cin>>s>>x;
        len=s.length();
        //cout<<len<<endl;
        for(i=0;i<len;++i)
        {
            if(s[i]=='-')
            {
                //cout<<i<<endl;
                if(i+x>len)
                {
                    cout<<"IMPOSSIBLE\n";
                    goto sana;
                }
                for(i2=0;i2<x;++i2)
                {
                    if(s[i+i2]=='-')
                    s[i+i2]='+';
                    else s[i+i2]='-';
                }
                z++;
            }
        }
        cout<<z<<"\n";
        sana:;
    }

}
