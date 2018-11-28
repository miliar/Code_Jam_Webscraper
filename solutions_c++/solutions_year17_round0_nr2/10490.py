#include<iostream>
using namespace std;
int main()
{
int temp1,temp2,num,count=1;
int T;
cin>>T;
int arr[T];
int res[T];
for(int i=0;i<T;i++)
{
count=1;
cin>>arr[i];
//cout<<"Entered value:"<<arr[i]<<endl;
if(arr[i]==arr[i]%10)
{
res[i]=arr[i];
continue;
}


for(int j=arr[i];j>0;j--)
{
//cout<<"J has a value"<<j<<endl;

num=j;

while(num!=0)
{
temp1=num%10;
num=num/10;
temp2=num%10;
/*if(count==1&&temp1==temp2)
{
break;
}*/
if(temp1>=temp2)
{
res[i]=j;
}
else
{
res[i]=0;
//cout<<"We'are in break condition."<<endl;
break;

}
}
if(res[i]==0)
{
continue;
}
else
{
break;
}
//cout<<"Outside while"<<endl;
}
}
for(int k=0;k<T;k++)
{
cout<<"Case #"<<(k+1)<<": "<<res[k]<<endl;
}
return 0;
}
