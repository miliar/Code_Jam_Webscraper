#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,len,i,j,n1,n2,k,p;
    ifstream input;
    input.open("input.cpp");
    ofstream output;
    output.open("output.cpp");
    string s;
    input>>t;
    for(k=0;k<t;k++)
    {
        input>>s;
        len=s.size();
        i=0;
        while(i+1<len)
        {
            n1=s[i]-48;
            n2=s[i+1]-48;
            if(n1>n2 && n1!=1)
            {
                s[i]=s[i]-1;
                for(j=i+1;j<len;j++)
                {
                    s[j]='9';
                }
                if(i>=1)
                i=i-2;
            }
            else if(n1>n2 && n1==1)
            {
                for(p=0;p<len-1;p++)
                {
                    s[p]='9';
                }
                len=len-1;
                break;
            }
            i++;
        }
        output<<"Case #"<<k+1<<": ";
        for(i=0;i<len;i++)
        {
            output<<s[i];
        }
        output<<endl;
    }
    return 0;
}
