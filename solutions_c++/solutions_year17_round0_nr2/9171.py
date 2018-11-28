#include <iostream>
#include<stdio.h>

using namespace std;

int main()
{
    FILE *f,*f2;
    f=fopen("test.txt","r");
    f2=fopen("test2.txt","w");

    int t;
    fscanf(f,"%d",&t);
    cout<<t<<"\n\n";


    for(int i=1;i<=t;i++)
    {
        long long n,m;
        fscanf(f,"%lld",&m);
        n=m;
        cout<<"m="<<m<<"\n";
        while(n)
        {
            long long int b=n;
            long long int v=b%10;
            int f=0;
            b=b/10;
            cout<<"b="<<b<<"\n";
            cout<<"v="<<v<<"\n";
            while(b)
            {
                cout<<"$";
                if(b%10<=v)
                {
                    v=b%10;
                    b=b/10;
                    //cout<<"v="<<v<<"\n";
                }
                else
                {
                    cout<<"Else part";
                    f=1;
                    break;
                }
            }
            //cout<<"$";
            if(f==0)
            {
                cout<<"Found";
                break;
            }
            n=n-1;
        }
        fprintf(f2,"Case #%d: %lld\n",i,n);
        cout<<"Case ans="<<n<<"\n";
    }
    return 0;
}
