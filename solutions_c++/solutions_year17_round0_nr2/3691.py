#include<bits/stdc++.h>
using namespace std;

main()
{
    freopen("input-2.txt","r",stdin);
    freopen("output-2.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long num;
        cin>>num;
        int arr[20]={0},countt=0;
        while (num!=0)
        {
            arr[countt]=num%10;
            countt++;
            num/=10;
        }
        for(int p=0;p<countt;p++){
        for(int j=countt-1; j>p; j--)
        {
            if(arr[j]>arr[j-1])
            {
                arr[j]--;
                for(int k=j-1; k>=0; k--)
                    arr[k]=9;
                break;
            }
        }}
        cout<<"Case #"<<i<<": ";
        if(arr[countt-1]==0)
            countt--;
        for(int j=countt-1;j>=0;j--)
            cout<<arr[j];
        cout<<endl;
    }
}
