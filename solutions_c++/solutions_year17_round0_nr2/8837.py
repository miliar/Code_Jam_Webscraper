#include <iostream>
#include <string>
#include <cmath>
#include <vector>
using namespace std;

bool checkTidiness(string s)
{
	int len = s.length();
	bool isTidy = true;
	if(len == 1)
	{
		return true;
	}
	else
	{
		for(int i = 0; i < len-1; i++)
		{
			if(s[i]>s[i+1])
			{
				isTidy = false;
			}
		}
		return isTidy;	
	}
}

int main()
{
	freopen("B-small-attempt0.in.txt", "r", stdin);
	freopen ("myfile.txt","w",stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int64_t num;
		cin >> num;
		string num_string = to_string(num);
		
		bool isTidy = checkTidiness(num_string);
		
		if(isTidy)
		{
			cout << "Case #" << i+1 << ": " << num << endl;
		}
		else
		{
			int len = num_string.length();
			vector <int> digits;
			digits.clear();
			int dec = len - 1;
			int64_t d;
			int q;
			int64_t result = num;
			for(int j = dec; j >= 0; j--)
			{
				d = pow(10, j);
				q = result/d;
				digits.push_back(q);
				result = result - q * d;
			}	
			int k = 0;
			int m = 0;
			while(!isTidy)
			{
				num = num - (digits[digits.size()-1-k]+1)*(pow(10,m));
				result = num;
				num_string = to_string(num);
				int lenVar = num_string.length();				
				int decVar = lenVar - 1;
				isTidy = checkTidiness(num_string);
				digits.clear();
				for(int l = decVar; l >= 0; l--)
				{
					d = pow(10, l);
					q = result/d;
					digits.push_back(q);
					result = result - q * d;
				}
				k++;
				m++;
			}
			cout << "Case #" << i+1 << ": " << num << endl;
		}
	}
	return 0;	
}
