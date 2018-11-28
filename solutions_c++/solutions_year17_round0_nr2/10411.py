#include<bits/stdc++.h>
using namespace std;
 int main()
{
   freopen("B-small-attempt3.in","r",stdin);
   freopen("B-small-attempt3.out","w",stdout);

    int t,i,n;
    cin>>t;
      for(i=1;i<=t;i++)
      {
          cin >> n;
          if (n==1000)
            cout << "Case #"<<i<<": "<< "999" <<endl;
           if (n<10)
            cout << "Case #"<<i<<": "<< n<<endl;
           if (n<100 && n>=10)
           {
              int a[2];
               a[0]=n/10;
               a[1]=n%10;
               if (a[0]<=a[1])
               cout <<  "Case #"<<i<<": " << n<<endl;
               else
               {
                   while (a[0]>a[1])
                   {
                       n=n-1;
                       a[0]=n/10;
                       a[1]=n%10;
                   }
                   cout << "Case #"<<i<<": " <<n<<endl;
               }
            }
            if (n>=100 && n<1000)
            {
                int b[3];
                b[0]=n/100;
                b[1]=(n/10)%10;
                b[2]=n%10;
                    while (b[0]>b[1] || b[1]>b[2])
                    {
                        n=n-1;
                         b[0]=n/100;
                         b[1]=(n/10)%10;
                         b[2]=n%10;
                    }
                    cout << "Case #"<<i<<": "<< n <<endl;

                }

            }


     }


