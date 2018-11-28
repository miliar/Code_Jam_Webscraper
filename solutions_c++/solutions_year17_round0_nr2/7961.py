#include<bits/stdc++.h>
using namespace std;
long long int check(long long int a[],int n)
{
 for(int i=0;i<n;i++)
 {
     if(a[i]>=a[i+1])
        continue;
     else
        return 0;


 }
 return 1;
}
int main()
{

   int t;
    cin>>t;
   long long  int test=1;
    while(t--)
    {
        long long int n,y,a[20],r,s=0,i=0;
        cin>>n;

         while(n!=0)
            {

                r=n%10;
                a[i]=r;
                n=n/10;
                i++;



            }

            y=check(a,i-1);


            if(y==1)
            {
                 for(int j=i-1;j>=0;j--)
            {
                s=s*10+a[j];

            }

                cout<<"Case #"<<test<<": "<<s<<endl;
            }


      else{




            for(int j=0;j<i-1;j++)
            {
                if(a[j]==a[j+1]&&a[j]==9)
                    continue;
                else if(a[j]<=a[j+1])
                {for(int k=j;k>=0;k--)
                {
                    a[k]=9;
                }
                a[j+1]=a[j+1]-1;}
                y=check(a,i-1);
                if(y==1)
                    break;


            }

           for(int j=i-1;j>=0;j--)
            {
                s=s*10+a[j];

            }
          cout<<"Case #"<<test<<": "<<s<<endl;
           }


test ++;
    }
    return 0;

}

