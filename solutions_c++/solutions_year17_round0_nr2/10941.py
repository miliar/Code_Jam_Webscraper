#include <iostream>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
	
	int T; // test cases
	
	ifstream input("B-small-attempt5.in");
	input >> T;
	ofstream output ("B-small-attempt5.out");
	int i=0;
	int m;
	string s;
	int l;
	int x;
	string tempx,tempy;
	for(int q=0; q<T; q++)
	{
	input >> m;
	tempx=to_string(m);
	tempy=to_string(m);
	sort(tempy.begin(),tempy.end());
	if(tempy==tempx)
	{
		if(q+1==T)
		{
			
		
		output<<"Case #"<<q+1<<": "<<m;
		}
		else
		{
			output<<"Case #"<<q+1<<": "<<m<<endl;
		}
		
	}
	
	else
	{
		
			
/*	if(q>1)
	{
	
	output << endl;	
	}*/\
		i=0;
	
	s=to_string(m);
	//char s[4]="132";
	



	//char s[2]="7";
	//char s[5]="1000";
	//char s[19]="111111111111111000";
	//cout<<s<<endl;
	//int l=strlen(s);
	l=s.size();
	for(i=0;i<l;i++)
	{
		if(s[i]>=s[i+1])
		{
			break;
		}
	}
	for(i=i+1;i<l;i++)
	{
		s[i]='0';
	}
	//cout<<s<<endl;
	
   x=stoi(s);
	if(l>1)
	{
		x=x-1;
	}
	
		if(q+1==T)
		{
			
		
		output<<"Case #"<<q+1<<": "<<x;
		}
		else
		{
			output<<"Case #"<<q+1<<": "<<x<<endl;
		}
	//output<<"Case #"<<q+1<<": "<<x<<endl;
	} // else ka loop
	} //test cases loop ended
	
}
