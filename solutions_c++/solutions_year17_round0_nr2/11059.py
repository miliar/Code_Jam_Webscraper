#include <iostream>
#include <fstream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <string>

using namespace std;
std::ofstream fout;
std::ifstream ifs;

int main(int argc, char *argv[])
{
	fout.open(argv[2]);
	ifs.open(argv[1]);

	int n, currentDigit, cont, temp, cont2 = 0;
	std::string::size_type sz;
	bool isTidy;
	std::string input;
	getline(ifs,input);
	cont = atoi(input.c_str());
	int answers[cont];
	while(cont2 < cont)
	{
		getline(ifs,input);
		n = atoi(input.c_str());
		while(n > 0)
		{
			temp = n;
			isTidy = true;
			currentDigit = temp%10;
			temp /= 10;
			while(temp > 0)
			{
				if(temp%10 > currentDigit)
				{
					isTidy = false;
					break;
				}
				currentDigit = temp%10;
				temp /= 10;
			}
			if(isTidy)
			{
				fout << "Case #" << (cont2+1) << ": " << n << "\n";
				break;
			}		
			n--;	
		}
		cont2++;
	}

	ifs.close();
	fout.close();
	return 0;
}