#include <bits/stdc++.h> 
using namespace std;
#include <fstream> 

int main()
{	
	    freopen("B-large.in","r",stdin);
    freopen("large2.out","w",stdout);

	long long int t,n;
	vector <long long int> v;
	cin>>t;
	for(long long int i=0;i<t;i++)
	{

		cout<<"Case #"<<i+1<<": ";

		vector <long long int> v;
		cin>>n;
		long long int m=n;
		while(m>0){
			long long int k=m%10;
			v.push_back(k);
			m=m/10;

		}

		long long int s=v.size();


		long long int p,j=0;
		for(p=s-1;p>0;p--){
			if(v[p]>v[p-1])
			{
				j=p;
				break;
				
				
			}

		}
		if(j==0)
			cout<<n<<endl;
		else{
			
			
			for(long long int a=0;a<j;a++){
				
				v[a]=9;

			}
			long long int f=0,a;
			for(a=j;a<s-1;a++){
				
				if(v[a]!=v[a+1]){
					v[a]=v[a]-1;

					f=1;
					break;
				}

				else{
					v[a]=9;
				}
				
				

			}
				
			
			if(f==0){
					v[s-1]=v[s-1]-1;

					}
			
		
		long long int nn=0;

		for(long long int a=s-1;a>=0;a--){
			nn=(nn*10)+v[a];
		}
		cout<<nn<<endl;

	}
		

	}


	
return 0;				
				
}
		
	