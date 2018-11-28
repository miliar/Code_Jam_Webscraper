#include<bits/stdc++.h>
using namespace std;
int main()
{
   int t,y;
   cin>>t;
   for(y=0;y<t;y++)
   {
      long long int n,i,j,pos=-1,a=1,c,count=1;
      int brr[20],flag=0;
      cin>>n;
      c=n;
      i=0;
      while(c)
      {
        brr[i++]=c%10;
        c=c/10;
      }



      for(j=0;j<i-1;j++)
      {
           if(brr[j]<=brr[j+1])
             pos=j+1;
           if(brr[j]>=brr[j+1])
              a++;
            if(brr[j]==brr[j+1])
              count++;
      }

        cout<<"Case #"<<y+1<<": ";
        if(i==count || i==a)
        {
           cout<<n;
           flag=1;
        }
        for(j=i-1;j>=0;j--)
        {
            if(flag==1)
                break;
            if(j==pos)
            {
                if(brr[j]-1)
                    cout<<brr[j]-1;

            }
            else if(j<pos)
                cout<<"9";
            else
                cout<<brr[j];
        }
        cout<<endl;


      }
      return 0;
   }

