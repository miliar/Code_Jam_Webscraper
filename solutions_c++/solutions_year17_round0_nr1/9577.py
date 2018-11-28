#include<iostream>
#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
    char s[1000];
    int k,t,i,j,l,m,counter=0,ans=0;
    cin>>t;
        for(m=0;m<t;m++)
            {
                        cin>>s;
                        cin>>k;
                        l=strlen(s);
                        for(i=0;i<l;i++)
                        {
                            if(s[i]=='-')
                            {
                                counter++;
                                if((l-i)>=k)
                                {
                                    for(j=i;j<(i+k);j++)
                                    {
                                        if(s[j]=='-')
                                        {
                                            s[j]='+';

                                        }
                                        else
                                            s[j]='-';
                                    }
                                }
                            }
                        }
                        for(i=0;i<l;i++)
                        {
                            if(s[i]=='+')
                                ans++;
                        }
                        if(ans==l)
                            cout<<"Case #"<<m+1<<": "<<counter<<endl;
                        else
                            cout<<"Case #"<<m+1<<": "<<"IMPOSSIBLE"<<endl;
                        counter=ans=0;
            }

return 0;
}
