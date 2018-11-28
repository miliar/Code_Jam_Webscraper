#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <limits>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <boost/spirit/include/karma.hpp>
#include <fstream>

using namespace boost::spirit;
using boost::spirit::karma::generate;
using namespace std;


bool is_tidy(char x[])
{

	string number(x);
	//std::cout<<"Size "<<number.length()<<" "<<number<<std::endl;
	for(int i=0;i<number.length()-1;i++)
	{
		//std::cout<<number[i]<<" "<<number[i+1]<<std::endl;
		if(number[i]>number[i+1])	
			return false;
	}

	return true;
}


int tide_number(uint64_t num,ofstream &fout)
{	
	char x[64];
	int count=0;
	while(true)
	{
		for(int i=0;i<64;i++)x[i]=0;

		char *ptr=x;	
		generate(ptr, int_, num);
		bool r=is_tidy(x);
	//	std::cout<<"Tide function "<<r<<" "<<num<<std::endl;
		count++;
		*ptr=0;
		if(r || num<10 || count >1000000)
			break;
		else	
			num--;
	}
	

	cout<<num<<endl;
	return 0;
}

int main(int argc, char **argv)
{

	if(argc!=3)
	{
		cout<<"Error"<<endl;
		return 0;
	}

	ifstream input(argv[1]);
	ofstream output(argv[2]);

	if(!input.is_open())
	{
		cout<<"File not found '"<<argv[1]<<"' "<<endl;
		return 0;
	}

	int T;
	
	input>>T;

	string line;
	getline(input,line);
	for(int t=0;t<T;t++)
	{
		cout<<"Case #"<<(t+1)<<": ";
		getline(input,line);
		//cout<<line<<endl;
		uint64_t num=std::stoll(line);
		tide_number(num,output);
	}

}
