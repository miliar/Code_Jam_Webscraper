#include <bits/stdc++.h>
 
using namespace std;

void print( char input[1001],int k)
{
	for(int m=0; m<k; m++)
	{
		cout<<input[m];
	}
	cout<<endl;
}	
int main() 
{
	int t;
	ios_base::sync_with_stdio (false);
	cin>>t;
	int test=t;
	while(t--)
	{
		char input[1001];
		int flip;
		cin>>input>>flip;
		int i=0,k=0,j=0,count=0,index=0,flag=1,m=0;
		k=strlen(input);
		//cout<<"string length "<<k<<endl;
		j=k-1;
		while((j)>=0)
		{
			//cout<<"Entered"<<endl;
		//	cout<<"Index "<<j<<endl;
			if(input[j]=='-' && (j+1) >= flip)
			{
			//	cout<<"Entered-"<<endl;
				count++;
				input[j] = '+';
				//cout<<input[j-1]<<endl;
				for(i=1;i<flip;i++)
				{
					if(input[j-i]=='-')
						input[j-i] = '+';
					else if(input[j-i]=='+')
					{
						input[j-i] = '-';
						if((j-i)>index)
							index=j-i;
		//					cout<<"  New Index of - : "<<index<<endl;					
					}
				}
				for(m=k-1;m>=0;m--)
				{
					if(input[m]=='-')
					{
						index = m;
						break;
					}
				}
				j=index;
			//	print(input,k);	
			}
			
			else if(input[j]=='-' && (j+1) < flip)
			{
		//		cout<<input[j]<<""<<"FLip :"<<flip<<endl;
				flag=0;
				break;
			}
			
			else if(input[j]=='+')
			{
				//cout<<"Entered+"<<endl;
				j--;
				//cout<<j-1<<endl;
			}
			
		}
		if(flag==0)
		{
			cout<<"Case #"<<test-t<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
			cout<<"Case #"<<test-t<<": "<<count<<endl;
	}
}
