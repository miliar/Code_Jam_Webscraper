#include<iostream>
# include <stdio.h>
# include <conio.h>
# include <string>


using namespace std;

int main()
{
unsigned long long q,m,t,b,s,k,i,j,g,z,n;


    char a[1010];
    cin>>t;
    for(i=0;i<t;i++)
    {
        k=0,z=0,n=0;
        cin>>a;

       for(g=0;g<1010;g++)
       {
           if(a[g]!='\0')
           {
               n++;
           }
           else{break;}
       }


       for(j=0;j<n;j++)
       {
           if(a[j]<=a[j+1])
           {
               k++;
           }

           else
           {
               if(j<n-1)
               {
                   if(a[j-1]==a[j])
                   {



                   q=j;
                   while(a[q-1]==a[q] && q>0)
                      {   q--;
                      }

                           m=q;

                           a[q]=a[q]-1;

                            z++;

                           j=n+1;
                   }



                    else{

                          m=j;

                          a[j]=a[j]-1;

                           z++;

                           j=n+1;
                    }

               }

           }
       }

           if(z>0)
           {

               for(b=m+1;b<n;b++)
               {
                   a[b]='9';
               }
           }


              cout<<"Case #"<<i+1<<": ";
              if(a[0]=='0')
              {
                  for(s=1;s<n;s++)
              {
                  cout<<a[s];
              }
              cout<<endl;

              }
              else{
              for(s=0;s<n;s++)
              {
                  cout<<a[s];
              }
              cout<<endl;
              }

       }


}

