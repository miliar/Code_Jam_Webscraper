#include <iostream>

using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int i=0;i<test;i++)
    {
        string str;
        cin>>str;
        int l=str.length();
        int arr[l];
        for(int j=0;j<l;j++)
            {
                arr[j]=str[j]-48;
            }
        for(int j=l-1;j>0;j--)
        {
            if(arr[j]<arr[j-1])
            {
                for(int k=j;k<l;k++)
                    arr[k]=9;
                arr[j-1]--;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        int j=0;
        if(arr[0]==0)
            j=1;
        for(;j<l;j++)
            cout<<arr[j];
        cout<<endl;
    }
    return 0;
}
