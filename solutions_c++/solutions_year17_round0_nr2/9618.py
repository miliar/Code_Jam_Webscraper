#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    long long int T,i,j,N;
    ifstream in("input.txt");
    ofstream out("output.txt");
    in>>T;
    for(i=0;i<T;i++)
    {
        long long int a[20],Count=0,temp,pos=-1,len,ans=0,flag=0;
        in>>N;
        temp=N;
        while(temp)
        {
            Count++;
            temp/=10;
        }
        temp=N;
        len=Count;
        while(temp)
        {
            a[--Count]=temp%10;
            temp=temp/10;
        }
        for(j=len-1;j>0;j--)
            if(a[j]<a[j-1])
                flag=1;
        if(flag==1)
        for(j=len-1;j>0;j--)
            if(a[j]<=a[j-1])
                pos=j-1;
        if(pos!=-1)
        {
            a[pos]=a[pos]-1;
            for(j=pos+1;j<len;j++)
                a[j]=9;
        }
        for(j=0;j<len;j++)
            ans=ans*10+a[j];
        out<<"Case #"<<i+1<<": "<<ans<<endl;
    }
}

