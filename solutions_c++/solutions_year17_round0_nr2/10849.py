#include<iostream>
#include<fstream>
#include<string>
using namespace std;

bool isTidy(string s)
{
	
	bool check=true;
	if(s.length()==1) return true;

	for(int i=0;i<s.length()-1;i++)
	{
		if(i != s.length()-1)
		{
			if(s[i]<=s[i+1])
			{
				check=true;
			}
			else{
				check=false;
				return check;
			}
		}
	}

	return check;
}

int tidy_number(string s)
{

	int num=stoi(s);
	
	while(num!=0)
	{
		if(isTidy(to_string(num)))
		{
			return num;
		}
		num--;
	}
}
int main()
{
	ifstream fin("file.txt");
	ofstream fout("output.txt");
	int number=0;
	string snum;
	int cases=0;
	int result=0,i=1;
	bool flag=false;
	fin>>cases;
	while(fin>>snum)
	{
		result=tidy_number(snum);
		fout<<"Case #"<<i<<":"<<" "<<result<<endl;
		//cout<<snum<<" "<<result<<endl;
		i++;
	}
	

	return 0;
}