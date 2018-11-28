#include <iostream>
#include <cstdlib>
#include <map>
#include <sstream>

using namespace std;

map<int, bool> tidyMap;


int main()
{
	std::ios::sync_with_stdio(false);
	
	unsigned int T;
	cin >> T;
	
	
	
	for (unsigned int i = 0; i < T; ++i)
	{
		//bool OK = false;
		
		string numStr;
		cin >> numStr;
		
		int len = numStr.length();
		
		
		if (len == 1)
		{
			cout << "Case #" << i+1 << ": " << numStr << endl;
		}
		else
		{
			for (unsigned int j = len-1; j > 0; --j)
			{
				if (numStr[j-1] > numStr[j])
				{   
					if (j == 1 && numStr[j-1] == '1')
					{
						numStr = std::string(len-1, '9');
						break;
					}
				    else
				    {
						for (unsigned int k = j; k < len; ++k)
						{
							numStr[k] = '9';
						}
					    numStr[j-1] = numStr[j-1] - 1;
					    //numStr[j] = '9';
					}
				}
			}
			
			cout << "Case #" << i+1 << ": " << numStr << endl;
		}
	}
	
	
	return 0;
}
