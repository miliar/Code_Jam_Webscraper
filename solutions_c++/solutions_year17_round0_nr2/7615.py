#include<bits/stdc++.h>
#include<iostream>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("output.in");
int main()
{
    long long int n,i,j;
    int t,k,c,z;
    fin>>t;
    z=t;
    while(t!=0)
    {
        c=0;
        fin>>n;
        j=n;
        while(j!=0)
        {
            c++;
            j/=10;
        }
        int arr[c];
        i=0;
        while(n!=0)
        {
            arr[i]=n%10;
            n/=10;
            i++;
        }
        for(i=c-2;i>=0;i--)
        {
            if(arr[i]<arr[i+1])
            {
                arr[i+1]--;
                for(k=i;k>=0;k--)
                {
                    arr[k]=9;
                }
                i=c-1;
            }
        }
        for(i=c-1;i>=0;i--)
        {
            if(arr[i]!=0)
            {
                k=i;
                break;
            }
        }
        fout<<"Case #"<<z-t+1<<": ";
        for(i=k;i>=0;i--)
        {
            fout<<arr[i];
        }
        fout<<endl;
        t--;
    }
}
