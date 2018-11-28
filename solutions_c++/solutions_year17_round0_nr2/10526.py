#include<iostream>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    for(int j=1;j<=tc;j++)
    {
        int n,c=0;
        cin>>n;
        int n1=n;
        while(n1>0)
        {
            int a=n1%10;
            c++;
            n1=n1/10;
        }

        if(c==1)
        {cout<<"Case #"<<j<<": "<<n<<endl;}

        if(c==2)
        {
            int n2=n;
             while(n2>0)
            {
                int a, array[2];
                int t=n2;
                a=t%10;
                array[0]=a;
                t=t/10;
                array[1]=t;

                if(array[0]>=array[1])
                {
                cout<<"Case #"<<j<<": "<<n2<<endl;
                n2=0;
                }
                else n2--;
            }
        }

        if(c==3)
        {
            int n3=n;
            while(n3>0)
            {
                int a, array[3];
                int t=n3;

                a=t%10;
                array[0]=a;
                t=t/10;
                a=t%10;
                array[1]=a;
                t=t/10;
                array[2]=t;

               if( (array[0]>=array[1]) && (array[1]>=array[2]))
               {
                   cout<<"Case #"<<j<<": "<<n3<<endl;
                   n3=0;
               }
                else n3--;
            }
        }
        if(n==1000)
        cout<<"Case #"<<j<<": "<<999<<endl;

    }


 return 0;
}
