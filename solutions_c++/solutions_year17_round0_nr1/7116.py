#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("codejam1.txt");
    int t,y=0;
    input>>t;
    while (t--)
    {
        y++;
        char s[1001];
        long c=0,i,j,l,k,ans=1;
        input>>s;
        l=strlen(s);
        input>>k;
        for (i=0;i<=l-k;i++)
        {
           // cout<<i;
            if (s[i]=='-')
            {
                for (j=0;j<k;j++)
                {
                    if (s[i+j]=='-')
                    {
                        s[i+j]='+';
                    }
                    else
                    {
                    s[i+j]='-';
                    }
                }
                c++;
            }
        }
        for (i=0;s[i]!='\0';i++)
        {
            if (s[i]=='-')
            {
                ans=0;
                break;
            }
        }
        if (ans==0)
        {
            output<<"Case #"<<y<<": IMPOSSIBLE"<<endl;
        }
        else
        {
            output<<"Case #"<<y<<": "<<c<<endl;
        }
    }
}
