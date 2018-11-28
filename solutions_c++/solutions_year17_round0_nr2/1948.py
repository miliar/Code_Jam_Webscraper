#include <iostream>
#include <string>

using namespace std;
using UInt = unsigned int;

int main()
{
	UInt N;
	cin >> N;
	for (UInt n = 0; n < N; ++n)
	{
		string val;
		cin >> val;
		bool go(true);
		for (UInt i = 0; i < val.size()-1 && go; ++i)
		{
			if (val[i] == val[i+1])
			{
				UInt k(i+1);
				while (k < val.size()-1)
				{
					if (val[k] == val[k+1])
						++k;
					else
						break;
				}
				
				if (k == val.size()-1)
				{
					cout << "Case #" << n+1 << ": " << val << endl;
					go = false;
				}
				else
				{
					if (val[k] > val[k+1])
					{
						if (i == 0 && val[0] == '1')
						{
							string out(val, 1, val.size()-1);
							for (UInt j = 0; j < val.size()-1; ++j)
								out[j] = '9';	
							cout << "Case #" << n+1 << ": " << out << endl;	
							go = false;			
						}
						else 
						{	
							if (val[i] == '1')
							{
								string out(val, 0, val.size()-1);
								for (UInt j = 0; j < val.size()-1; ++j)
									out[j] = '9';	
								cout << "Case #" << n+1 << ": " << out << endl;	
								go = false;
							}
							else
							{
								--val[i];	
								for (UInt j = i+1; j < val.size(); ++j)
									val[j] = '9';
								cout << "Case #" << n+1 << ": " << val << endl;
								go = false;
							}
						}
					}
				}		
			}
			if (val[i] > val[i+1])
			{
				if (i == 0 && val[0] == '1')
				{
					string out(val, 1, val.size()-1);
					for (UInt j = 0; j < val.size()-1; ++j)
						out[j] = '9';	
					cout << "Case #" << n+1 << ": " << out << endl;	
					go = false;			
				}
				else 
				{	
					if (val[i] == '1')
					{
						string out(val, 0, val.size()-1);
						for (UInt j = 0; j < val.size()-1; ++j)
							out[j] = '9';	
						cout << "Case #" << n+1 << ": " << out << endl;	
						go = false;
					}
					else
					{
						--val[i];	
						for (UInt j = i+1; j < val.size(); ++j)
							val[j] = '9';
						cout << "Case #" << n+1 << ": " << val << endl;
						go = false;
					}
				}
			}
		}
		if (go)
			cout << "Case #" << n+1 << ": " << val << endl;
	}
}
