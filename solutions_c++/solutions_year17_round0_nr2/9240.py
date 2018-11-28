#include<bits/stdc++.h>
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
#include<string.h>
using namespace std;
#define mod 1000000007

long double fact(int k)
{
    long int f=1;
    for (int i=1;i<=k;i++)
        f*=i;
    return (long double)(f*f);
}
int main()
{
   freopen("inp.in","r",stdin);
    freopen("out2.out","w",stdout);
    //getline(cin,str);
    int t,base,i,j,f;
    cin>>t;
    long long int n,num;
    for (i=0;i<t;i++)
    {
        cin>>n;
        cout<<"Case #"<<i+1<<": ";
        base=log10(n);
        base++;
        num=n;
        int arr[25];
        for (j=1;j<=base;j++)
        {
            arr[j]=num%10;
            num=num/10;
        }
        int flag=0;
        for (j=1;j<base;j++)
        {
            if (arr[j]<arr[j+1])
            {
                flag++;break;
            }
        }
        if (!flag)
            cout<<n<<endl;
        else
        {
            while (1)
            {
                for (j=base;j>1;j--)
                {
                    if (arr[j]>arr[j-1])
                    {
                        arr[j]--;
                        f=j-1;
                        while (f!=0)
                        {
                            arr[f]=9;f--;
                        }
                        break;
                    }
                }
                if (arr[base]==0)
                {
                    for (j=base-1;j>=1;j--)
                        cout<<9;
                    cout<<endl;
                    break;
                }
                for (j=base;j>1;j--)
                {
                    if (arr[j]>arr[j-1])
                    {
                        f++;break;
                    }
                }
                if (f==0)
                {
                    for (j=base;j>=1;j--)
                        cout<<arr[j];
                    cout<<endl;
                    break;
                }
            }
        }
    }
}
