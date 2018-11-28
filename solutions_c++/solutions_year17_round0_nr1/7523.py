#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int main()
{
	fstream fin;
	ofstream fout;
	fout.open("output.in");
	fin.open("A-large.in");
	int test;
	fin>>test;
	for(int i=0;i<test;i++)
	{
		string str;
		fin>>str;
		//cout<<str;
		int size;
		fin>>size;
		
		int k=0;
		int count=0;
		//cout<<str.size();
		while(k<str.size())
		{
			if(str[k]=='-')
			{
			//	cout<<k<<endl;
			if(k+size-1<str.size())
			{
			//	cout<<k<<" "<<k+2<<endl;
			count++;
				str[k]='+';
				int j=1;
				while(j<size)
				{
					if(str[k+j]=='+')
					{
						str[k+j]='-';
					}
					else{
						str[k+j]='+';
					}
					j++;
				}
			}
			else{
				fout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
				count=-1;
				break;
			}
		}k++;
		}if(count!=-1)
		{
			fout<<"Case #"<<i+1<<": "<<count<<endl;
		}
	
		
	}
}
