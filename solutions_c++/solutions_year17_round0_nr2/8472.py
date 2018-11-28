#include <iostream>
#include <string>
#include <sstream>
#include <vector>

//#include <ctime>

using namespace std;

string decrease(string line)
{
	int c = 1, i;
	int pos;
	while(1)
	{
		pos = line.length() - c;
		if(pos<0)
			break;

		int val = (char)(line[pos]) - 48;
		if(val-1 >= 0)
		{
			val = val-1 + 48;
			line[pos] = (char)val;
			break;
		}
		else
			line[pos] = '9';
		c++;
	}

	if(line.length()>1)
	{
		c = 0;
		for(i = 0; i<line.length(); i++)
		{
			if((char)(line[i]) == 48)
				c++;
			else
				break;
		}
		if(c>0)
			line = line.substr(c);
	}

	return line;
}

int check(string line)
{
	int i;
	for(i = 0; i<line.length()-1; i++)
	{
		if((char)(line[i+1])<(char)(line[i]))
			return 0;
	}
	return 1;
}

int main(int argc, char* argv[])
{
	string line;
	getline(cin, line);
	istringstream ss(line);

	int T;
	ss >> T;
//	cout << "T: " << T << endl;

	for(int i=0; i<T; i++)
	{
		getline(cin, line);

//		clock_t begin = clock();

		cout << "Case #" << i+1 << ": ";

		if(line.length()==1)
			cout << line << endl;
		else
		{
			string dline = line;
			if(check(dline))
				cout << dline << endl;
			else
			{
				while(1)
				{
					dline = decrease(dline);
					if(dline.length()==1)
					{
						cout << dline << endl;
						break;
					}
					if(check(dline))
					{
						cout << dline << endl;
						break;
					}
					
				}
			}
		}

//		clock_t end = clock();
//		double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
//		cout << "TIME: " << elapsed_secs << endl;
	}

	return 0;
}
