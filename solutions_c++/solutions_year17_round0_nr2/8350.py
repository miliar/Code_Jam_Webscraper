#include <iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>
using namespace std;

int main()
{
    freopen("B-large (1).in","r",stdin);
    freopen("submit_tanya.out","w",stdout);
    long long int t,n,k,no,i,l=0;
    cin>>t;
    for(k=0;k<t;k++)
    {
        cin>>n;
        no=n;
        l=0;
        while(no!=0)
        {
            l++;
            no=no/10;
        }
        long long int a[l];
        no=n;
        i=l-1;
        while(no!=0)
        {
            a[i]=no%10;
            no=no/10;
            i--;
        }
        i=0;
        long long int flg=0,f=0;i=0;
       // cout<<"okkk";
       int check=0;
       long long int stop=99999;
        for(i=0;i<l-1 && i>=0;i++)
        {
        	if(i>stop)
        	{
        		break;
        	}
            if(a[i]>a[i+1])
            {
                a[i]=a[i]-1;
               //cout<<a[i]<<"\n";
                long long int z=i+1;
                while(z<l)
                {
                	if(check==0)
                	{
                		stop=z;
                		check=1;
                	}
                    a[z]=9;z++;
                }

                i=i-2;
            }

        }long long int sum=0,x;
            x=1;
        for(i=l-1;i>=0;i--)
        {
            sum=sum+a[i]*x;
            x=x*10;
            //cout<<"summm "<<sum<<"\n";
        }
        cout<<"Case #"<<k+1<<": "<<sum<<"\n";
        //cout<<sum<<"\n";
    }
    return 0;}
