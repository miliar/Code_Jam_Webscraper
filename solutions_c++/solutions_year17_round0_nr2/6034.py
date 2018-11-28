#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fou("B-large.out");
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		long long number;
		string input,result;
		fin>>number;
		//cout<<number<<endl;
		ostringstream os;
		os<<number;
		input = os.str();
		if(number<20)
		{
			result = input;
		}
		else
		{
			int index = 1;
			int len = input.size();
			while(index < len)
			{
				if(input[index - 1] <= input[index])
					index++;
				else
					break;
			}
			if(index == len)
			{
				result = input;
				fou<<"Case #"<<i<<": "<<result<<endl;
				continue;
			}
			
			
			char last = input[index-1];
			while(index>1)
			{
				if(input[index-2] == last)
					index--;
				else
					break;
			}
			string prefix = input.substr(0,index);
			istringstream is(prefix);
			long long prefixNumber;
			is>>prefixNumber;
			prefixNumber--;
			ostringstream os;
			os<<prefixNumber;
			if(prefixNumber >0)
				result = os.str() + string(len - index,'9');
			else
				result = string(len - index,'9');
		}
		fou<<"Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}