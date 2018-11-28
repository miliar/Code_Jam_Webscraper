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
		//cout<<s<<"\n";
		
    	istringstream buf(s);
    	istream_iterator<string> beg(buf), end;

    	vector<string> tokens(beg, end); // done!

    	string patt = tokens.at(0);
		
		stringstream sStream( tokens.at(1) );
		sStream >> n;

		bool ch = true;
		int out = 0;
		
		for( int i = 0; i < patt.length(); i++ )
		{
			if( patt[i] == '-' )
			{
				if( (i+n) <= patt.length() )
				{
					patt[i] = '+';
					for( int j = i+1; j< (i+n); j++ )
						patt[j] = (patt[j] == '-') ? '+' : '-';
					out++;
				}
				else
				{
					ch = false;
					break;
				}
			}
		}
		if( ch )
		{
			file << "Case #"<<cnt<<": " << out << endl;
		}
		else
		{
			file << "Case #"<<cnt<<": IMPOSSIBLE" << endl;
		}
		
		cnt++;
	}
		
	return 0;
}
