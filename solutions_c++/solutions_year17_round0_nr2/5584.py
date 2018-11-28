#include <iostream>
#include <string>

using namespace std;

int primeiraOcorrencia(string a, int start)
{
	for(int i = start; i < a.length(); i++)
		if(a[i] != a[start])
			return i;
	return -1;
}


int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		string c, d;
		cin >> c;
		bool zerum = true;
		
		if(c.length() == 1)
		{
			cout << "Case #" << i+1 << ": " << c << endl;
			continue;
		}
		
		
		for(int k = 0; k < c.length(); k++)
		{
			if(c[k] != '0' && c[k] != '1')
			{
				zerum = false;
			}
		}
		
		if(zerum)
		{
			if(c[c.length()-1] == '0')
			{
				for(int j = 0; j < c.length()-1; j++)
					d += '9';
				cout << "Case #" << i+1 << ": " << d << endl;
			}
			else
				cout << "Case #" << i+1 << ": " << c << endl;
			
			
		}
		else
		{
			d += c[0];
			int first = c.length();
			
			
			for(int j = 1; j < c.length(); j++)
			{
				if(c[j] > c[j-1])
					d += c[j];
					
				else if(c[j] == c[j-1])
				{
					int a = primeiraOcorrencia(c, j-1);
					if(a == -1)
						d = c;
					else if(c[a] > c[a-1])
					{
						for(int k = j; k < a; k++)
							d += c[j];
						j = a-1;
					}
					else
					{
						d[j-1]--;
						for(int k = j; k < c.length(); k++)
							d += '9';
						j = c.length();
					}
				}
					
					
				else
				{
					d[j-1]--;
					for(int k = j; k < c.length(); k++)
						d += '9';
					j = c.length();
				}
			}
		if(d[0] == '0')
			d.erase(0, 1);
		cout << "Case #" << i+1 << ": " << d << endl;
		}
	}
	return 0;
}