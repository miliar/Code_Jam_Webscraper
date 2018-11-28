#include <iostream>
using namespace std;

int main() {
	long long t,n,k;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	    cin>>n>>k;
	    int a[n+10]={0};
	    a[n]++;
	   long long int m=n;
	   while(k>1)
	   {
	       a[m]--;
	       if(m%2==0)
	       {
	           a[m/2]++;
	           a[m/2-1]++;
	       }
	       else
	       a[m/2]+=2;
	       
	       if(a[m]==0)
	       for(;;m--)
	       if(a[m]>0)
	       break;
	       k--;
	   }
	   if(m%2 ==0)
	   {
	       cout<<"Case #"<<i<<": "<<m/2<<" "<<m/2-1<<endl;
	   }
	   else
	   cout<<"Case #"<<i<<": "<<m/2<<" "<<m/2<<endl;
	}
	return 0;
}
