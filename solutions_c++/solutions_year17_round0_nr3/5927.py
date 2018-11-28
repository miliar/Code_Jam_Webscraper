#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
#include<sstream>
#include <vector>
#include <iterator>

using namespace std;

int t;

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

	int x = 1;

	while(x <= t)
	{	
		getline(infile, s);
		
    	istringstream buf(s);
    	istream_iterator<string> beg(buf), end;

    	vector<string> tokens(beg, end); // done!

    	string patt = tokens.at(0);
    	
    	long long n, k;
		
		stringstream sStream1( tokens.at(0) );
		sStream1 >> n;

		stringstream sStream2( tokens.at(1) );
		sStream2 >> k;

		//cout<<n<<"\t"<<k<<"\n";
		long long y = 0;
		long long z = 0;
		
		bool arr[n+2];
		arr[0] = true;
		arr[n+1] = true;
		for( int i = 1; i < n+1; i++ )
			arr[i] = false;

		if( n > k )
		{
			for( int i = 0; i < k; i++ )
			{
				int strt = 0;
				int max_diff = -1;
				int laststrt = 0;

				for( int j = 1; j < n+2; j++ )
				{
					int temp = j -strt - 2;
					if( arr[j] )
					{
						if( temp > max_diff )
						{
							max_diff = temp;
							laststrt = strt;
						}
						strt = j;
					}
				}
				
				if( max_diff & 1 )	//odd
				{
					y = (max_diff+1)>>1;
					z = y - 1;
				}
				else
				{
					y = max_diff/2;
					z = y;
				}
				arr[laststrt+z+1] = true;
			}
		}
		
		file << "Case #"<<x<<": " << y << " " << z << endl;
		x++;
	}
		
	return 0;
}
