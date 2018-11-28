#include<iostream>
using namespace std;
int main()
{
int test;
long long int r5,r;
cin>>test;
for(int i=1;i<=test;i++)
{
int max=0;
cin>>r;
r5=r;
while(r>0)
{
r = r/10;
max++;
}
int array[max];
for(int p=max-1;p>=0;p--) 
{
array[p] = r5%10;
r5 = r5/10;
}
for(int l=max-1;l>0;l--)
{
if(array[l-1]>array[l])
{
array[l-1]-=1;
for(int d=l;d<max;d++)
{
array[d]=9;
}
}
}
if(array[0]==0)
cout<<"Case #"<<i<<": ";
else
cout<<"Case #"<<i<<": "<<array[0];
for(int b=1;b<max;b++)
{
cout<<array[b];
}
cout<<"\n";
} 
}