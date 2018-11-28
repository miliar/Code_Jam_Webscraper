#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,k,flag,num,i,j,len,p;
    string s;
    ifstream input;
    input.open("input.cpp");
    ofstream output;
    output.open("output.cpp");
    input>>t;
    for(p=1;p<=t;p++)
    {
        flag=0;
        num=0;
        input>>s>>k;
        len=s.size();
        for(i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                num++;
                for(j=i;j<=i+k-1;j++)
                {
                    if(j>=len)
                    {
                        flag=1;
                        break;

                    }
                    if(s[j]=='+')
                      s[j]='-';
                    else if(s[j]=='-')
                        s[j]='+';
                }
            }
            if(flag==1)
            {
                break;
            }
        }
        output<<"Case #"<<p<<": ";
        if(flag==1)
        {
            output<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            output<<num<<endl;
        }
    }
    return 0;
}
