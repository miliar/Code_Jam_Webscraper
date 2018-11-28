#include<iostream>
using namespace std;
int main()
{
    long long int t, i;
    cin>>t;
    for(i=0;i<t;i++)
    {
        long long int s=0, j, n, temp;
        cin>>n;
        temp=n;
        while(1)
            {
                n=temp;
                s=0;
                while(n!=0)
                {
                    s++;
                    n/=10;
                }
                n=temp;
                int arr[s];
                for(j=s-1;j>=0;j--)
                {
                    arr[j]=n%10;
                    n/=10;
                }
                n=temp;
                for(j=s-1;j>0;j--)
                {
                    if(arr[j]<arr[j-1])
                    {
                        temp=n-1;
                        break;
                    }
                }
                if(n!=temp)
                    continue;
                cout<<"Case #"<<i+1<<": ";
                for(j=0;j<s;j++)
                {
                    cout<<arr[j];
                }
                cout<<endl;
                break;
            }
    }
    return 0;
}
