#include<iostream>
using namespace std;
int main(){
	
	int t;
	cin>>t;
	int q;
	long int n[100];
	for (q=0;q<t;q++)
	{
		cin>>n[q];
	}
	for(q=0;q<t;q++)
	{
		while(n[q]){
	    int a[100];
		int i;
		long int x=n[q];
		int count=0;
		for(i=0;x!=0;i++)
		{
			int r=x%10;
			a[i]=r;
			x=x/10;
			count++;
	    }
	    int flag=0;
		for(int j=0;j<(count-1);j++)
	    {
	    	if(a[j]>=a[j+1])
	    	{
	    		flag++;
	    		
			}
		}
		if(flag==(count-1))
		{
			cout<<"Case #"<<q+1<<": "<<n[q]<<endl;
		break;
		}
		else
		n[q]--;
	}
	}
	return 0;
}
