#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<fstream>

using namespace std;
void max_cal(long int arr[],long int st);
long int str,enda;

int main()
{
ifstream input;
    input.open("in.txt",ios::in);
    ofstream result;
    result.open("output.txt",ios::out);

int ts;
input>>ts;
for(int t=0;t<ts;t++)
{
long int st,np,y;
input>>st>>np;
    long int len=st+2;
long int arr[len];
  arr[0]=1;
  arr[st+1]=1;

for(int i=1;i<st+1;i++)
{
arr[i]=0;
}
for(int k=0;k<np;k++)
{
   max_cal(arr,st);
y=floor(((str+1)+(enda-1))/2);
arr[y]=1;

}
long int l,r,count=0;
for(long int j=y-1;j>0 && j<st+1 ;j--)
{
if(arr[j]==0)
{
count++;
}
else
{
break;
}
}
l=count;
count=0;
for(long int j=y+1;j>0 && j<st+1;j++)
{
if(arr[j]==0)
{
count++;
}
else
{
break;
}
}
r=count;
result<<"Case #"<<t+1<<": "<<max(l,r)<<" ";
result<<min(l,r)<<"\n";
}
input.close();
result.close();
return 0;
}

void max_cal(long int arr[],long int st)
{
long int len=st+2;
long int count=0,max_zeros=-1;
for(long int p=0;p<len;p=p+count+1)
{    count=0;
for(long int s=p+1;s<len;s++)
{
if(arr[s]==0)
{
count++;
}
else
{
if(max_zeros<count)
{
max_zeros=count;
str=p;
enda=p+count+1;
   }
break;
}
}
}
}

