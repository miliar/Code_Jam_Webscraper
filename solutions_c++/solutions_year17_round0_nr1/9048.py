#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main()
{
	ofstream fout("out.in");
	ifstream fin("A-large.in");
	char ar[10000];	
	fin.getline(ar,10000);
	
	int t=atoi(ar);
	//cin>>t;
	for(int j=0;j<t;j++)
	{
		fin.getline(ar,10000,' ');
		
		string s=ar;;
		//cin>>s;
		fin>>ar;	
		int k=atoi(ar);
		//cin>>k;
		int f=0;int c=0;
		//cout<<s.size()-k;
		for(int i=0;i<=s.size()-k;i++)
		{//cout<<s<<endl;
			if(s.at(i)=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(s.at(j)=='-')s.at(j)='+';
					else
						s.at(j)='-';
				}
				f++;
			}
		}int ch=0;
		for(int k=0;k<s.size();k++)
			{
				if(s.at(k)=='-')
					ch=1;
			}
		if(ch==0){
		cout<<"Case #"<<j+1<<": "<<f<<endl;
		fout<<"Case #"<<j+1<<": "<<f<<endl;	}
		else{
		cout<<"Case #"<<j+1<<": "<<"IMPOSSIBLE"<<endl;
		fout<<"Case #"<<j+1<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
