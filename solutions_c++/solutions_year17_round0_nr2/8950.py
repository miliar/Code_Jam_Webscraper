#include <bits/stdc++.h>
using namespace std;
int arr[18];
int check(int n)
{
    int ch=0;
    for(int i=0;i<n;i++)
        if(arr[i-1]>arr[i])
        ch=1;
    return ch;
}
void tidy(int n)
{
    int j=n-2;
    if(check(n)==0)
        return;
    arr[n-1]=9;
    arr[n-2]-=1;
    while(arr[j]<0)
    {
        arr[j]=9;
        arr[j-1]-=1;
        j--;
    }
    tidy(n-1);

}
int main()
{
    std::ios::sync_with_stdio(false);
    freopen("a.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long n;
    int t,nod,temp,che=0,lc=1;
    cin>>t;
    while(t--)
    {
        che=0;
        cin>>n;
        nod=log10(n)+1;
        for(int i=0;i<nod;i++)
        {
            arr[i]=n%10;
            n=n/10;
        }
        for(int i=0;i<nod/2;i++)
        {
            temp=arr[i];
            arr[i]=arr[nod-1-i];
            arr[nod-1-i]=temp;
        }
            tidy(nod);
            cout<<"Case #"<<lc++<<": ";
            for(int i=0;i<nod;i++)
            {
            if(arr[i]!=0)
                che=1;
            if(che==1)
            cout<<arr[i];
            }
            cout<<endl;
    }


    return 0;
}
