#include<iostream>
#include<math.h>
using namespace std;

int main()
{	
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		long long int n,k,val,sum,parts,x1,x2,y1,y2,find,dble,pairs;
		cin>>n>>k;
		cout<<"Case #"<<z<<": ";
		
		for(int i=1;;i++)
		{
			if(k < pow(2,i))
			{
				val=i;
				break;
			}
		}
		//cout<<val;//4
		
		sum = n - (pow(2,val)-1);
		parts = pow(2,val);
		
		x1 = sum / parts; //18
		x2 = x1+1; //19
		
		y2 = sum-(x1*parts); //9 
		y1=parts-y1; 
		
		pairs = parts/2;
		
		find = k - (pow(2,val-1)) + 1;
		
		if(y2>=pairs)
		{
			dble = y2 % pairs;
			
			if( find <= dble) //same
				cout<<x2<<" "<<x2;
			else //diff
				cout<<x2<<" "<<x1;
		}
		else
		{
			if(find<=y2)
				cout<<x2<<" "<<x1;
			else
				cout<<x1<<" "<<x1;
		}
		cout<<endl;
	}
	return 0;
}
