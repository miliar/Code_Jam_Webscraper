#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;


bool IsTidy(long long int val)
{
	double max = 10;
	while(val >0)
	{
		long double p = val%10;
		if(p <=max) { 
			max = p;
			val /= 10;
		}
		else return false;
	}

	return true;
}
void main()
{
	//ifstream f_in ("B-large-practice.in");
	ifstream f_in ("B-small.in");
	//ifstream f_in ("small_input.txt");
	//ifstream f_in ("test.in");
	ofstream f_out("test.out");
	//ofstream f_out("B-small-practice.out");
//	ofstream f_out("B-large-practice.out");
		int case_num;
		f_in >> case_num;
		string tstr;
		getline(f_in,tstr);
	for(int k = 1; k <= case_num; ++k)
	{
		long long int val;
		f_in>> val;
		while (!IsTidy(val))
			val-=1;
		
		f_out<<"Case #"<<k<<": "<<val<<endl;

	}
	f_in.close();
	f_out.close();
}