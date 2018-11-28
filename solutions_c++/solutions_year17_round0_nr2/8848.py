#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t;
	long long n;
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");
	fin>>t;
	
		int counter=1;
	for(int i = 1; i <= t ; i++)
	{
		fin>>n;
		int flag=1;
		while(flag)
		{
		long long temp=n;
            int count=0;
		if(temp%10!=0)
		{
			if(temp/10==0)
			{
				 fout<<"Case #"<<counter<<": "<<n<<endl;
                counter++;
                break;
			}
			long first=temp%10;
			temp=temp/10;
			
			while(temp!=0)
			{
			
				long sec=temp%10;
				if(first>=sec)
				{
			
				flag=0;
				first=sec;
				temp=temp/10;	
			
				}
				else
				{
					flag=1;
					break;
				}
				
				
			}
		}
            if(flag==0 )
                {
                fout<<"Case #"<<counter<<": "<<n<<endl;
                counter++;
                break;
            }
		n--;
	}
	}
}
