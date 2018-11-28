#include<bits/stdc++.h>
using namespace std;
 int main()
{
  freopen("B-small-attempt0.in","r",stdin);
   freopen("B-small-attempt0.out","w",stdout);

    int t,i,n;
     cin>>t;
      int a[3];
      for(i=1;i<=t;i++)
      {
         cin>>n;
         if(n==1000 || n==100 || n==10)
        cout<<"Case #"<<i<<": "<<n-1<<endl;
         else if(n<10)
         cout<<"Case #"<<i<<": "<<n;
          else if(n<100 && n>10)
            {
            a[0]=0; a[1]=(n/10)%10; a[2]=n%10;
            if(a[1]<=a[2])
            cout<<"Case #"<<i<<": "<<n<<endl;
            else
            cout<<"Case #"<<i<<": "<<(a[1]-1)*10+9<<endl;
            }
            else if(n>100 && n<1000)
              {
                a[0]=n/100; a[2]=n%10; a[1]=(n/10)%10;
             if(a[0]<=a[1] && a[1]<=a[2])
               cout<<"Case #"<<i<<": " <<n<<endl;
            else if((a[2]<=a[0]) && a[0]>=a[1])
                cout<<"Case #"<<i<<": "<<(a[0]-1)*100+99<<endl;
            else if(a[2]<a[1] && a[1]>=a[0])
                cout<<"Case #"<<i<<": "<<((n/10)-1)*10+9<<endl;
                else
              cout<<"Case #"<<i<<": "<<(a[0]-1)*100+99<<endl;
               }

     }

}
