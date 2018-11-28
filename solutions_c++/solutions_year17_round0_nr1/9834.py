#include<iostream>
#include<cstring>
using namespace std;


int main()

{
    int t;
       cin>>t;
    for(int y=0;y<t;y++)
    {

    char a[100];int k,n,j,count=0;
   cin>>a;
   n=strlen(a);
   cin>>k;
   for(int i=0;i<n-k+1;)
   {
       if(a[i]=='-')
        {  for(j=i;j<k+i;j++)
            {
                if(a[j]=='+')
                   {

                    a[j]='-';
                   }
                 else if(a[j]=='-')
                 {
                   a[j]='+';
                 }

            }

            for(j=i;j<i+k;j++)
            {
                if(a[j]=='-')
                    break;
            }
              i=j;

            count=count+1;


        }


       else if(a[i]=='+')
        i++;

   }
    //cout<<count;
   // cout<<a;
    int x=0;
    for(j=n-k;j<n;j++)
    {
        if(a[j]=='-')
        {
            cout<<"Case #"<<y+1<<": IMPOSSIBLE"<<endl;
            x=x+1;
              break;

        }

    }

    if(x==0)
        cout<<"Case #"<<y+1<<": "<<count<<endl;

    }
    return 0;
}







