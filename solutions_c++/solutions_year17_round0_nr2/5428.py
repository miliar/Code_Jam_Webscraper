#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

int NumOfDigs(lli num)
{
    lli len=0;
    while(num>0)
    {
        len++;
        num/=10;
    }
    return len;
}

int main()
{
    int t,k,c=1;
    cin>>t;
    while(t--)
    {
        lli temp,n,l;
        cin>>n;
        l=NumOfDigs(n);

        int arr[100];
        temp=n;
        for(int i=l-1;i>=0;i--)
        {
            arr[i]=temp%10;
            temp/=10;
        }

        while(1)
        {
            int i;
            for(i=1;i<l;i++)
            {
                if(arr[i]<arr[i-1])
                {
                    arr[i-1]--;
                    for(int j=i;j<l;j++)arr[j]=9;
                    break;
                }
            }
            if(i==l)
            {
                cout<<"Case #"<<c++<<": ";
                int k=0;
                while(arr[k]==0)k++;
                for(int i=k;i<l;i++)cout<<arr[i];
                cout<<endl;
                break;
            }
        }

    }
    return 0;
}
