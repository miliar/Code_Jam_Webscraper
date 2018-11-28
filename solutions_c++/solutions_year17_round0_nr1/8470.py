#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

void main()
{
	ifstream f_in ("A-large.in");
//	ifstream f_in ("A-small.in");
	//ifstream f_in ("small_input.txt");
	//ifstream f_in ("test.in");
	//ofstream f_out("test.out");
//	ofstream f_out("A-small.out");
	ofstream f_out("A-large.out");
		int case_num;
		f_in >> case_num;
		string tstr;
		getline(f_in,tstr);
	for(int k = 1; k <= case_num; ++k)
	{
		string str;
		int v;
		f_in>>str;
		f_in>>v;
		getline(f_in,tstr);

		int num = 0;
		int pos_minus = -1;
		int i = 0;
		while( i <str.length()  && str[i] != '-')
			++i;
		pos_minus = i;

	
		while((pos_minus+v) <=str.length() )
		{

			for(int j = pos_minus; j <(pos_minus+v) ; ++j)
				if(str[j] == '-')str[j] = '+';
				else str[j] = '-';
			++num;

			int i = 0;
			while( i <str.length()  && str[i] != '-')
				++i;
			pos_minus = i;
		}
		if(pos_minus==str.length())
			f_out<<"Case #"<<k<<": "<<num<<endl;
		else
			f_out<<"Case #"<<k<<": IMPOSSIBLE"<<endl;

		}
	f_in.close();
	f_out.close();
}