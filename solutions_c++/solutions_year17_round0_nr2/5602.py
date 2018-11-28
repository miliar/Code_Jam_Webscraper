#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
    int t,n,test,i,f,j,flag;
    ifstream input;
    input.open("input.cpp");
    ofstream output;
    output.open("output.cpp");
    input>>t;
    string s;
    for(test=1;test<=t;test++)
    {
        input>>s;
        f=0;
        flag=0;
        for(i=0;i<s.size()-1;i++)
        {
             if(s[i]>s[i+1])
             {
                flag=1;
                break;
             }
        }
        if(flag)
        {
            while(s[i]>s[i+1])
            {
               if(s[i]=='1')
               {
                    for(i=0;i<s.size();i++)
                    {
                        s[i]='9';
                    }
                    f++;
                    break;
               }
                for(j=i+1;j<s.size();j++)
                {
                    s[j]='9';
                }
                s[i]=s[i]-1;
                i=i-1;
                if(i==-1)
                    break;
            }
        if(f)
        {
            output<<"Case #"<<test<<": ";
            for(i=0;i<s.size()-1;i++)
                output<<s[i];
            output<<endl;
        }
        else
        {
            output<<"Case #"<<test<<": "<<s<<endl;
        }
        }
        else
        {

             output<<"Case #"<<test<<": "<<s<<endl;
        }
    }
    return 0;
}
