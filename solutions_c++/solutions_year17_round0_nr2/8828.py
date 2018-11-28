#include <iostream>
using namespace std;
 int checkdigits(int num)
{
int previous,next;
previous=num%10;
num/=10;
while(num>0)
{
next=num%10;
if(next>previous)
return 0;
previous=next;
num/=10;
}
return 1;
}
int main() {
	int t,i,n,check=0;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		do
		{
         if(checkdigits(n)==1)
         check=1;
         else
         n--;
		}while(check!=1);
		check=0;
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
	return 0;
}