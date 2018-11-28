#include<iostream>
#include<cstring>
using namespace std;


int main()
{	//freopen("A-small-attempt0.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	
	int T; 
	cin>>T;
	if(T>100||T<1)
	{
		return 0;
	}
	char str[T][1300];
	int a[T];
	for(int i=0;i<T;i++)
	{
		cin>>str[i];
		cin>>a[i]; 
	}
	for(int j=0;j<T;j++)
	{
		
		
		int q=0;bool r=true;
		for(int k=0;k<=(strlen(str[j])-a[j]);k++)
			{
				if(str[j][k]=='-')
				{
					for(int l=k;l<k+a[j];l++)
					{
						if(str[j][l]=='-')
						{
							str[j][l]='+';
						}
						else if(str[j][l]=='+')
						{
							str[j][l]='-';
						}
						
					}
					q++;				
				}
			}
		for(int k=0;k<strlen(str[j]);k++)	
		{
			if(str[j][k]=='-')
			{
				r=false;
				break;
			}
		}
		if(r==false)
		{
			cout<<"Case #"<<j+1<<": IMPOSSIBLE\n";
		}
		else
		{
			cout<<"Case #"<<j+1<<": "<<q<<"\n";
		}	
			
	}
	return 0;
	
}

