#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream ab("file.in");
	ofstream ob("output.txt");
	int a;
	ab>>a;
	
	int num;
	for(int i=0;i<a;i++)
	{
		ab>>num;
		int res;
		for(int j=num;j>=1;j--)
		{
		int temp=j;
			if(temp/10==0)
			{
			res=temp;
			break;
			}
			int f=0;
			int prev=temp%10;
			temp/=10;
			while(temp>0)
			{
				if(prev<(temp%10))
				{
					f=1;
					break;
				}
				prev=temp%10;
				temp=temp/10;
				
			}
			if(f==0)
			{
			res=j;
			break;
		}
		}
		ob<<"Case #"<<i+1<<": "<<res<<endl;
			
	}
}
