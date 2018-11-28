#include <iostream>

using namespace std;

int main()
{
    int t,p,maxi=10,temp1=0,flag=0;
    cin>>p;
     t=p;
    long long int n,temp;
    while(t--)
    {
        cin>>n;
        for(long long int i=n;i>0;i--)
        {
           temp=i;

           while(temp  !=0)
           {

               temp1=temp%10;
               temp =temp/10;


               if(maxi<temp1){
                    flag=1;
               break;

               }
               else
                maxi=temp1;
            }

            if(flag==0)
            {
                cout<<"Case #"<<p-t<<": "<<i<<endl;
                break;
            }
            flag=0;
            maxi=10;
        }
    }
    return 0;
}


