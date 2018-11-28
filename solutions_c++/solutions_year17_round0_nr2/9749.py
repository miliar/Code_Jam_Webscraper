#include<iostream>
using namespace std;

 main()
{
		freopen("input.in","r",stdin);
	
	freopen("output.txt","w",stdout);
	int tc;
	long long int num,n;
	
	cin >> tc;
	for(int m=1;m<=tc;m++)
	{
		cin >> num;
		cout<<"Case #"<<m<<": ";
	int a[20]={0};
	       int t;
		int k=-1;
		n=num;
		while(num!=0)
		{
			k=k+1;
			a[k]=(num%10);
			num=num/10;
			
		}
	int s;


	for( int g=k; g>0 ; g-- )
		{
			if(a[g]>a[g-1])
			{
				t=a[g];
				s=g;
				
				while(s<=k && t==a[s]  )
				{
				s=s+1;
				}
				s--;
				a[s]=a[s]-1;
				
				
				for(g=(s-1); g>=0 ; g-- )
				a[g]=9;
				
				break;
					}}
		
		
		for(int i=k; i>=0 ; i-- )
		{
			if(i==k && a[i]==0 )
			continue;
			
			else
			cout<<a[i];
		}
	cout<<endl;	
	}
				
			

}
