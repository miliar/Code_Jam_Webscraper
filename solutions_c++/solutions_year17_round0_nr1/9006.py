#include<iostream>
#include<stdio.h>
#include<string.h> 
long long int sum,i,j,k,T,x,c,b,flag;
char a[10000],p;
using namespace std;
main()
{
      cin>>T;
      c=T;
      while(T--)
      {
                cin>>a;
                cin>>k;
                x=strlen(a);
                j=(x-1);
                sum=0;
                flag=1;
                for(i=0;i<=j-k;i++)
                {
                                    if(a[i]=='+')
                                    continue;
                                    else
                                    {
                                        sum++;
                                        for(b=i;b<i+k;b++)
                                        {
                                                          if(a[b]=='+')
                                                          a[b]='-';
                                                          else
                                                          a[b]='+';
                                        }
                                    }
                }   
                p=a[i];
                for(j=i;j<x;j++)
                {
                              if(a[j]==p)
                              continue;
                              else
                              {
                                  flag=0;
                                  break;
                              }
                }
                if(flag==1)
                {
                           if(p=='-')
                           sum++;
                           cout<<"Case #"<<c-T<<": "<<sum<<"\n";
                }
                else
                cout<<"Case #"<<c-T<<": "<<"IMPOSSIBLE\n";                     
                //fprintf(fp,"Case #%d: ",(c-T));
                //fprintf(fp,"%d\n",sum);
                
      }
             return 0;
}
