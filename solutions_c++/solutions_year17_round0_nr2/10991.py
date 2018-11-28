#include<iostream>
#include<conio.h>
#include<fstream>
#include<string>
#include <stdlib.h> 
using namespace ::std;

bool TidyNumber(int n)
{
	int temp[20];
	int i=-1;
	while(n>0)
	{
		temp[++i]=n%10;
		n=n/10;
	}
	for(int j=0;j<=i-1;j++)
	{
		for(int k=j+1;k<=i;k++)
		{
			if(temp[j]<temp[k])
			{
				return false;
			}
			else if(temp[j]==temp[k] & temp[k-1]<temp[k])
			{
				return false;
			}
		}
		
	}
	return true;
	
}
void numbers()
{
	string mline;
	int line_num=0;
	int num=0;
	ifstream file;
	file.open("B-small-attempt3.in");
	if(file.is_open())
	{
		getline(file,mline);
		while(!file.eof())
		{
			
			getline(file,mline);
			line_num++;
			num=atoi( mline.c_str() );
		//	cout<<num<<"		";
			while(!TidyNumber(num))
			{
				num--;
			}
			cout<<"Case #"<<line_num<<": "<<num<<endl;
		}
	}
}
int main()
{
	
	numbers();
	
	getch();
	return 0;
}
