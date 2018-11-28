#include<iostream>
#include<cstdio>
  using namespace std;

  int main()
  {
    int t,n,i,c,k,j;
      int test[100];
     int d[10];
      int ctr,ctr1;

     freopen("B-small-attempt2.in","r",stdin);


      cin>>t;
     for(k=1;k<=t;k++)
         cin>>test[k];


      for(k=1;k<=t;k++)
      {  n=test[k];
       for(i=n;i>=1;i--)
           {  c=i;
              ctr=0;
                ctr1=0;
             while(c>0)
              {
                 d[ctr]=c%10;
                //  cout<<d[ctr]<<endl;
                 c=c/10;
                 ctr++;
               //  cout<<ctr<<endl;
               }

               if(ctr==1)
                 goto A;

               for(j=1;j<ctr;j++)
               { //
                  // cout<<d[j]<<endl;
                 if(d[j-1]>=d[j])
                   ctr1++;
                 }
                   if(ctr1==(ctr-1))
                    goto A;
           }
      A:

         cout<<"Case #"<<k<<": "<<i<<endl;

      }
          freopen("output_file_name.out","w",stdout);
      return 0;
   }
