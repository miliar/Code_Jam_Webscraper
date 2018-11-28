#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

int main()
{
int testCase;
unsigned long long int n,copy;
vector<int> vec(19);
cin>>testCase;
int ca=0;
while(testCase--)
{
ca++;
cin>>n;
copy=n;
unsigned long long count=1,a,b;
a=copy%10;
copy=copy/10;
long long int c;
long long int pos=0;
while(copy>0)
{
c=copy%10;
if(c>a)
{
c-=1;
pos=count;
}

++count;
a=c;
copy/=10;
}
if(pos>0)
{
n-=(long long)(pow(10,pos));
n/=(long long)(pow(10,pos));
n*=(long long)(pow(10,pos));
n+=(long long)(pow(10,pos))-1;
}
cout<<"Case #"<<ca<<":"<<" "<<n<<endl;
}
return 0;
}
