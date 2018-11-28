#include<iostream>
using namespace std;
int main()
{
    int t,l=1,k,i,j,pos,f,ct,z;
    cin>>t;
    string s;
    while(t--)
    {
        cin>>s>>k;
        i=0;f=0;ct=0;z=0;
        while(s[i]!='\0')
        {
            if(s[i]=='-')
            {
                pos=i;
                j=i;
                f=0;
                while(j<i+k)
                {
                    if(s[j]=='\0')
                    {
                        z=1;
                        break;
                    }
                    if(s[j]=='+')
                      {
                          s[j]='-';
                         if(f==0)
                          {pos=j;
                           f=1;}
                      }
                    else
                        s[j]='+';
                    j++;
                }
                ct++;
                 i=pos;
            }
            else
            {
                i++;
            }
            if(z==1)
                break;

        }
        if(z==1)
            cout<<"Case #"<<l<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<l<<": "<<ct<<endl;
        l++;
    }
    return 0;
}
