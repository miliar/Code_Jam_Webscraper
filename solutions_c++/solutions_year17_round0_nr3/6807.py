#include <iostream>
#include <string.h>
using namespace std;

void checkdigits(int num,int k)
{
int a,b,temp_num=num,temp_k=k;
while(temp_k!=0){
a=temp_num/2;
if(temp_num%2==0)
b=temp_num/2-1;
else
b=temp_num/2;
if(temp_k%2==0)
temp_num=a;
else
temp_num=b;
temp_k/=2;
}
cout<<a<<" "<<b<<endl;
}
int main() {
	int t,i,k;
	int n;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		cin>>k;
        cout<<"Case #"<<i<<": ";
		 checkdigits(n,k);
	}
	return 0;
}
