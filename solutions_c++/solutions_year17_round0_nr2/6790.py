#include <iostream>
#include <string.h>
 
using namespace std;

int main() 
{
	int t,test;
	ios_base::sync_with_stdio (false);
	cin>>t;
	test=t;
	while(t--)
	{
		char input[20],copy[20],copy1[20],flag=1;
		
		cin>>input;
		
		int k=0,i=0,j=0,index=0;
		
		k=strlen(input);
		
		//cout<<"String Length"<<k<<endl;
		
		for	(i=0;i<k;i++)
		{
			//cout<<"here";
			input[i] = input[i] -'0';	
		}	
		
		for	(i=0;i<k;i++)
		{
			copy[i]=input[i];	
		
		}
		//cout<<"Original String after copying ";
		
		//for	(i=0;i<k;i++)
		//{
		//	cout<<int(copy[i]);	
		//}
		//cout<<endl;
		
		for(j=k-1;j>=0;j--)
		{
			if(input[j] < input[j-1])
			{
				index= j-1;
				flag=0;
			//	break;
			}
		}
	//	cout<<"Index at which its violating "<<index<<endl;
		if (flag==1)
		{
			cout<<"Case #"<<test-t<<": ";
			for	(i=0;i<k;i++)
			{	
				cout<<int(input[i]);	
			}
			cout<<endl;	
		}
		if(flag==0)
		{
			if(index!=0)
			{
				for(i=0;i<=index;i++)
				{
					copy[i]=0;
				}
			}
			if(index==0)
			{
				for(i=0;i<=index;i++)
				{
					copy[i]=0;
				}
			}
		//	for	(i=0;i<k;i++)
		//	{
		//		cout<<int(copy[i]);	
		//	}
			
		//	cout<<endl;
			//cout<<"New integer";
			for	(i=0;i<k;i++)
			{
				input[i]= input[i] - copy[i];	
			}
		//	cout<<"After Subtracting";
		//	for	(i=0;i<k;i++)
		//	{
		//		cout<<int(input[i]);	
		//	}
		//	cout<<endl;
			int c =-1;
				int z=1,temp=0,temp1=-1;
//				if(flag==1)
//				{
					for( i=k-1;i>=0;i--)
					{
						if(input[i] != 0)
						{
							if(c == -1 && i!=0)
							{
								c =input[i];
								z=i;
								temp=z;
							}
							else if(input[i] == c && input[i+1] == c)
							{
								z=i+1;
								temp1=z;
								if(i==0)
								{
		//							cout<<k<<" 1"<<endl;
									for(int a=z;a<k;a++)
									{
										input[a] = 9;
									}
									input[z-1] = input[z-1]-1;					
								}
							}
							else
							{
								if(z == temp && temp != temp1)
									z=z+1;
		//						cout<<k<<endl;
								for(int a=z;a<k;a++)
								{
									input[a] = 9;
								}
								input[z-1] = input[z-1]-1;
								break;
							}
						}
					}
//				}
				cout<<"Case #"<<test-t<<": ";
				if(input[0]!=0 || k==1)
				//	cout<<s<<endl;
				{
					for(i=0;i<k;i++)
					{
						cout<<int(input[i]);
					}
					cout<<endl;
				}	
				else
				{
					for(int i=1;i<k;i++)
						cout<<int(input[i]);
					cout<<endl;
				}
		}
	}
}

