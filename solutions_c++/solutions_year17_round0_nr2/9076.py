#include<bits/stdc++.h>
using namespace std;

long long int n;



int main()
{
	int T;
	scanf("%d",&T);
	int t,a,i,j;
	
	ofstream o("program3data.txt");
	for(t=1;t<=T;t++)
	{
	o<<"Case #"<<t<<": ";
	
		scanf("%d",&n);
		
		int ans=0,prev=0;
		for(i=1;i<=n;i++){
			
			int c=i,f=0;prev=9;
			while(c!=0){
				int r=c%10;
				if(r>prev)
				{f=1;
				break;
			}
			prev=r;
				c=c/10;
			}
			if(f==0)
			ans=i;
		}
		
				

	
	cout<<ans;
	o<<ans;

		cout<<"\n";
		o<<endl;
	
	}
	return 0;
}
