#include <iostream>
using namespace std;  

int main() 
{
  long long int t;
  string s;
  long long int k;
  long long count = 0;
  cin >> t; 
  
  for (long long int j = 1; j <= t; ++j) 
  {
  	cin >> s >> k;
  	count = 0;
  	for(long long int i = 0; i <= s.length() - k; i++)
  	{
  		if(s[i] == '-')
		{
			for(long long int l = 0; l < k; l++)
			{
				if(s[i + l] == '-')
				{
					s[i + l] = '+';
				}
				else
				{
					s[i + l] = '-';
				}
			}
			count++;
		}	
	}
	
	int flag  = 1;
	for(long long int l = s.length() - k; l < s.length(); l++)
	{
		if(s[l] != '+')
		{
			flag = 0;	
		}
	}
	if(flag == 0)
	{
		cout << "Case #" << j << ": IMPOSSIBLE" << endl;
	}
	else
	{
		cout << "Case #" << j << ": " << count << endl;	
	}   
  }
  return 0;
}
 

