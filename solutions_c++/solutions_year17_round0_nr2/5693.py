#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
#include<sstream>
#include <vector>
#include <iterator>

using namespace std;

int t;
int n;

int main()
{	
	ifstream infile;
	ofstream file;
	
	infile.open ("D:\\devc\\A-large-practice.txt");
	file.open("D:\\devc\\output.txt");
	
	string s;
	
	getline(infile, s);
	stringstream sStream( s );
	sStream >> t;

	int cnt = 1;

	while(cnt <= t)
	{	
		getline(infile, s);
		bool ch = true;
		int len = s.length();
		
		for( int i = 1; i < len; i++ )
		{
			if( (int)s[i] < (int)s[i-1]  )
			{
				ch = false;
				break;
			}
		}
		
		if(!ch)
		{
			int pos = len-1;
			for( int i = len-1; i > 0; i-- )
			{
				if( (int)s[i] < (int)s[i-1] )
				{
					pos = i;
					s[i-1] = (int)s[i-1] - 1;
				}
			}
			string temp(len-pos, '9');
			s.replace(pos, (len-pos), temp);
			if( s[0] == '0' )
				s = s.substr(1);
		}

		file << "Case #"<<cnt<<": " << s << endl;
		cnt++;
	}
		
	return 0;
}
