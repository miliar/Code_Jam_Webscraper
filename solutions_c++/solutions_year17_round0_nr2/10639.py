#include <iostream>
#include<string>

using namespace std;

int main()
{
	int T,N,ans=0,y=0,q=1;
	
	bool w=false;
	string x;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		cin>>N;
		for(int j=N;j>=1;j--)
		{
			x=to_string(j);
			if(x.length()==1)
					{
						cout<<"case #"<<q<<": "<<j<<endl;
						q++;
					}
			
			//cout<<x<<endl;
			for(int p=0;p<x.length()-1;p++)
			{
				if(x[p]-'0'<=x[p+1]-'0')
				{
					//cout<<j<<endl;
					y++;
					
					if(y==x.length()-1)
					{
						cout<<"case #"<<q<<": "<<j<<endl;
						q++;
						w=true;
					}
					
				}
				else
				{
					w=false;
					break;
					
				}
				
			}
			y=0;
			if(w==true)
			{
				break;
			}
			
		}
		
		
	}
	
	
	
	
	
	
	
	
	
	
	
	
}