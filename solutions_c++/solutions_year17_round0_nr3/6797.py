#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int t=0,i=0,k=0,l=0,n=0,f1,l1,m1,f11,l11=0,m11=0,pos,c,mx;

    cin>>t;
    for(int i=0; i<t; i++)
    {

        cin>>n>>k;
        int str[n];
        for(int z=0; z<=n+1; z++)
        {
            str[z]=1;
        }
        str[0]=0;
        str[n+1]=0;
        pos=0;
        f1=0;
        l1=n+1;
        m1=(f1+l1+1)/2;
        str[m1]=0;




        if(k==1)
        {
            pos=(l1+f1)/2;
            cout<<"Case #"<<i+1<<": "<<l1-pos-1<<" "<<pos-f1-1<<"\n";

        }
        else if(k==n)
        {
            cout<<"Case #"<<i+1<<": "<<0<<" "<<0<<"\n";

        }
        else
        {


            for(int j=0; j<k-1; j++)
            {
                mx=0;
                c=0;
                f1=0;
                l1=0;
                for(int z=1; z<=n+1; z++)
                {
                    if(str[z]==1&&str[z-1]==0)
                    {

                        c=1;
                        f1=z;
                        l1=z;

                    }
                    else if(str[z]==1&&str[z-1]==1)
                    {


                        c++;
                        l1=z;

                    }

                    else if(str[z]==0&&str[z-1]==1)
                    {
                        if(c>mx)
                        {
                            l11=l1;
                            f11=f1;

                            mx=c;
                            f1=0;
                            l1=0;


                        }
                    }

                }


                pos=(l11+f11)/2;
                str[pos]=0;

            }




            pos=(l11+f11)/2;
            cout<<"Case #"<<i+1<<": "<<l11-pos<<" "<<pos-f11<<"\n";
        }

    }
    return 0;
}

