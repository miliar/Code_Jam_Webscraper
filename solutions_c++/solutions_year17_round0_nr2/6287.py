#include<iostream>
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
freopen("C:/Users/Ayush Garg/Downloads/input.txt","r",stdin);
int t;
scanf("%d",&t);
int cs=0;
while (t--)
{
cs++;
ll n;
scanf("%lld", &n);

int b[100];
ll store= n;
int i=0;
while (n!=0)
{
int rem=n%10;
b[i++]=rem;
n/=10;

}

int a[100];
i--;
int k=0;
int z=i;

for (int j=i; j>=0; j--)
a[k++]=b[j];


int end=0;
int flag=0;

for (int i=1; i<=z;i++)
{
    if (a[i]<a[i-1])
    {
        end=i;
        flag=1;
        a[i]=9;
        a[i-1]--;
        break;
    }
}

if (flag)
for (int i=end;i<=z;i++)
    a[i]=9;


for (int i=end-1;i>=1; i--)
{

     if (a[i]<a[i-1]){
        a[i-1]=a[i];
        a[i]=9;
    }

}

for (k=0;k<=z;k++)
{
    if (a[k]!=0)
        break;

}

printf("Case #%d: ", cs);
if  (k==0)
for (int i=k;i<=z; i++)
{
    if (a[i]==-1)
        cout<<"9";
    else
        cout<<a[i];
}
else
{
    for (int i=1; i<=z;i++)
        cout<<"9";
}
cout<<endl;

}

return 0;
}
