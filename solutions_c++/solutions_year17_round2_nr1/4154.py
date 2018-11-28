#include<iostream>
#include<math.h>
using namespace std;

int main(){
int t,itr=1;
cin>>t;
while(t-- >0)
{
	long dist,n,i;
	cin>>dist>>n;
	long a1,a2;
	long dd;
	double slow=-1;
	for(i=0;i<n;++i)
	{
		cin>>a1>>a2;
		dd=dist;
		dd-=a1;
		a1=dd;
		dd=dd/a2;
		a1=a1%a2;
		double slowN=dd;
		slowN+=(double)a1/a2;
		if(slowN>slow)
			slow=slowN;
		
	}
	double dl=dist;
		dl/=slow;
		printf("Case #%d: %.6f\n",itr,dl);
		itr++;
}
return 0;
}