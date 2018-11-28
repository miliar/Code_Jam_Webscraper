#include <iostream>

using namespace std;

int main()
{
    int t,x,y,z,m,i;
    cin>>t;
    int a[t];

    for(i=0;i<t;i++)
    {
     cin>>a[i];
   }
    for(i=0;i<t;i++)
  {

  if(a[i]<10)
    cout<<"Case #"<<i+1<<": "<<a[i]<<"\n";
  else if(a[i]==1000)
        cout<<"Case #"<<i+1<<": "<<a[i]-1<<"\n";
    else
    {



    z=a[i]%10;
    x=a[i]/100;
    m=a[i]/10;
    y=m%10;



    if(y>x&&z>x&&z>y||x==y&&x==z||x<y&&y==z||x==y&&y<z)
    cout<<"Case #"<<i+1<<": "<<x*100+y*10+z<<"\n";
     if(x>y||x>z||y>z)
    {
    do
    {
       --a[i];
        z=a[i]%10;
    x=a[i]/100;
    m=a[i]/10;
    y=m%10;

    }while(x>y||x>z||y>z);

    cout<<"Case #"<<i+1<<": "<<a[i]<<"\n";
    }

     }
}

    return 0;
}
