#include <iostream>

using namespace std;

int main()

{

int t,i,a[20],arr[20],x;

long long int n,ans,ten;

cin>>t;

for(x=1;x<=t;x++)

{

ans=0;

int pos=20,len;

i=0;

len=0;

cin>>n;

while(n)

{

a[i++]=n%10;

n/=10;

}

len=i;

for(i=0;i<len;i++)

{

arr[i]=a[len-i-1];

}

for(i=len-2;i>=0;i--)

{

if(arr[i]>arr[i+1])

{

pos=i;

arr[pos]--;

}

}

for(i=pos+1;i<len;i++)

{

arr[i]=9;

}

ten=1;

for(i=len-1;i>=0;i--)

{

ans+=arr[i]*ten;

ten*=10;

}

cout<<"Case #"<<x<<": "<<ans<<endl;
}

return 0;

}