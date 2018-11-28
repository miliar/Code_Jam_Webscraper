#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ifstream fin("A-large.doc",ios::in);
	ofstream fout("a.txt",ios::out);
	int t;
	char ch;
	fin>>t;
	fin.get(ch);
	int w=1;
	//cout<<t;
	while(t--)
	{
		string s;
		
		//fin.get(ch);
		int k;
		fin>>s>>k;
		fin.get(ch);
		int l=s.length();
		int arr[l];
		for(int i=0;i<l;i++)
			arr[i]=0;
		int i=0;
		int count=0;
		for(i=0;i<l-k+1;i++)
		{
			int q=1;
			if(s[i]=='+')
				q=1;
			else
			{
				q=0;
			}
			q=q+arr[i];
			if(q%2==0)
			{
			//	cout<<i<<endl;
			
				for(int j=i+1;j<i+k;j++)
					arr[j]++;
				count++;
			}
		}
		int flag=0;
		for(i;i<l;i++)
		{
			int q=1;
			if(s[i]=='+')
				q=1;
			else
			{
				q=0;
			}
			q=q+arr[i];
			if(q%2==0)
			{
				flag=1;
				break;
			}
		}
		fout<< "Case #" << w << ": " ;
		if(flag)
		{
			fout<<"IMPOSSIBLE";
		}
		else
			fout<<count;
		fout<<endl;
		w++;
		//fin.get(ch);
	}
	return 0;
}