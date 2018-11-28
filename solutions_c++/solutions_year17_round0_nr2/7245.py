#include <iostream>
using namespace std;

int main()
{
   int t;
   cin>>t;
   for(int k=0; k<t; k++)
   {
       string a;
       cin>>a;
       int l=a.length();
       cout<<"Case #" <<k+1<<": ";
       if(l==1)
        cout<<a<<endl;
       else
       {
           int flag=0;
           while(flag==0)
           {
               
           flag=1;
           for(int i=0; i<l-1;i++)
       {
           if(a[i]>a[i+1])
           {
               flag=0;
               a[i]=(a[i])-1;

               for(int j=i+1; j<l; j++)
               {
                   a[j]='9';
               }

           }
       }
           }
       for(int i=0; i<l ;i++)
       {

           if(a[i]!='0')
           cout<<a[i];

       }
       cout<<endl;
       //cout<<a;

       }

   }
    return 0;
}
