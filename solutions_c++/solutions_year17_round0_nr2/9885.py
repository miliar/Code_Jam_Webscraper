#include <iostream>
#include<string.h>
#include<stdio.h>

using namespace std;

int main()
{
    int t,n,i,j,k,count=1,s;
    char a[3];
    cin>>t;
    for(i=0;i<t;i++)
    {
            cin>>s;
            count=1;
            while(count!=0)
            {
                    a[0]=s/100;
                    a[1]=((s%100)/10);
                    a[2]=((s%100)%10);
                    if(s==1000)
                    {
                        cout<<"Case #"<<i+1<<": "<<--s<<endl;
                        count=0;
                    }

                    else if((a[0]<=a[1])&&(a[1]<=a[2]))
                    {
                        cout<<"Case #"<<i+1<<": "<<s<<endl;
                        count=0;
                    }
                    else
                    {
                        s--;
                    }


            }
    }


    return 0;
}
