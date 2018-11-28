#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int q=1; q<=t; q++)
    {

        long long int n,m,c=0,a,l,no;
        cin>>n;
        m=n;
        while(m!=0)
        {
            c++;
            m=m/10;
        }
        long long int arr[c];
        for(int i=c-1; i>=0; i--)
        {
            arr[i]=n%10;
            n=n/10;
        }
      X:  for(int i=0; i<c-1; i++)
        {
            if(arr[i]<=arr[i+1])
            {
arr[i]=arr[i];
            }
            else
            {
                if(arr[i]==1)
                {
                    for(int j=i+1; j<c; j++)
                    {
                        arr[j]=9;
                    }


                while(arr[i]==1)
                        { arr[i]=9;


                 i--; }

     arr[0]=0;

                    break;
                }
                else
                {

                    for(int j=i+1; j<c; j++)
                    {
                        arr[j]=9;
                    }
                    arr[i]--; i=0; goto X;

                }
            }

        }
        cout<<"case"<<" "<<"#"<<q<<":"<<" ";
        if(arr[0]==0)
        {
            for(int i=1; i<c; i++)cout<<arr[i];
        }
        else
        {
            for(int i=0; i<c; i++) cout<<arr[i];
        }
        cout<<endl;

    }
    return 0;
}
