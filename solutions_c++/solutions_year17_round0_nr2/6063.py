#include <bits/stdc++.h>
using namespace std;
int main() {
  int size,a[20],arr[20];
  long long n,t;
  cin >> t;
  for(long long j=1;j<=t;j++) {
    cin>>n;
    size=0;
    while(n)
    {
        arr[size++]=n%10;
        n=n/10;
    }
    for(int z=0;z<size;z++)
    {
        a[z]=arr[size-z-1];
    }
    while(1){
            int flag=0;
    for(int i=0;i<size-1;i++)
    {
        if(a[i]>a[i+1])
        {
            flag++;
            a[i]=a[i]-1;
            for(int z=i+1;z<size;z++)
            {
                a[z]=9;
            }
        }
    }
    if(flag==0)
        break;
  }
    cout << "Case #" << j << ": ";
    int c=0;
    for(int z=0;z<size;)
{
    if(c!=0)
    {
        cout<<a[z++];
    }
    else
    {
        for(int m=0;m<size;m++)
        {
            if(a[m]==0)
                z++;
            else
            {
                c++;
                break;
            }
        }
    }
}
    cout<<endl;
  }
return 0;
}
