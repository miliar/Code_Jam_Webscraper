#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{

freopen("B-small-attempt3.in","r",stdin);
freopen("output.txt","w",stdout);
    int t,case1=1;
    cin>>t;
    int r=0;
    while(t--)
    {
        long long int ans,temp,count=0,meow,meow2;
        long long int n;
        cin>>n;
        meow=n;
        meow2=n;
        while (meow) {

            meow /= 10;
            count++;

        }
       long long int a[count];

        if(n<10)
        {
              ans=n;
             cout<<"Case #"<<case1<<": "<<ans<<endl;
        }

        else
        {

            for(int i=count-1;i>=0;i--)
            {

                a[i]=meow2%10;
                meow2/=10;
            }



            for(int i=0;i<count;i++)
            {
                  if(a[i]>=a[i+1] && i!=count-1 && a[count-1]!=0)
            {
                if(a[i]>a[i+1])
                {
                    a[i]--;
                for(int j=i+1;j<count;j++)
                {
                    a[j]=9;
                }
                }
                else
                {
                    if(i=count-1)
                    {
                        if(a[count-2]>a[count-1])
                        {
                             a[0]--;
                for(int j=1;j<count;j++)
                {
                    a[j]=9;
                }
                        }
                    }
                }

            }
            else if(a[count-1]==0)
            {
                if(a[i]>=a[i+1])
                {
                    a[i]--;
                for(int j=i+1;j<count;j++)
                {
                    a[j]=9;
                }
                }

            }




            }
             cout<<"Case #"<<case1<<": ";
            if(a[0]==0)
            {
                for(int i=1;i<count;i++)
             {
                 cout<<a[i];
             }

            }
            else
            {
                for(int i=0;i<count;i++)
             {

                 cout<<a[i];
             }

            }

            cout<<endl;
        }



        case1++;
    }
 return 0;
}


