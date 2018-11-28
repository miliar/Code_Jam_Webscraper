#include <iostream>
#include <string>
#include <vector>

using namespace std;

char back(string s)
{
	return s[s.size() - 1];
}

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		bool possible = true;
		
		string output = "";
		
		if (R > 0)
		{
			output = "R";
			R--;
		}
		else if (O > 0)
		{
			output = "O";
			O--;
		}
		else if (Y > 0)
		{
			output = "Y";
			Y--;
		}
		else if (G > 0)
		{
			output = "G";
			G--;
		}
		else if (B > 0)
		{
			output = "B";
			B--;
		}
		else if (V > 0)
		{
			output = "V";
			V--;			
		}
		
			
		for (int i = 1 ; i < N ; ++i)
		{
			if (back(output) == 'O')
			{
				if (B > 0)
				{
					B--;
					output += "B";
				}
				else
				{
					break;
				}
			}
			
			
			if (back(output) == 'G')
			{
				if (R > 0)
				{
					R--;
					output += "R";
				}
				else
				{
					break;
				}
			}
			
			
			if (back(output) == 'V')
			{
				if (Y > 0)
				{
					Y--;
					output += "Y";
				}
				else
				{
					break;
				}
			}
			
			if (back(output) == 'R')
			{
				if (G > 0)
				{
					G--;
					output += "G";
				}
				else
				{
					if (Y > B)
					{
						Y--;
						output += "Y";						
					}
					else if (B > 0)
					{
						B--;
						output += "B";
					}
					else
					{
						break;
					}
				}
			}
			
			
			if (back(output) == 'Y')
			{
				if (V > 0)
				{
					V--;
					output += "V";
				}
				else
				{
					if (R > B)
					{
						R--;
						output += "R";						
					}
					else if (B > 0)
					{
						B--;
						output += "B";
					}
					else
					{
						break;
					}
				}
			}
			
			
			if (back(output) == 'B')
			{
				if (O > 0)
				{
					O--;
					output += "O";
				}
				else
				{
					if (Y > R)
					{
						Y--;
						output += "Y";						
					}
					else if (R > 0)
					{
						R--;
						output += "R";
					}
					else
					{
						break;
					}
				}
			}
		
		}

		// first and last
		if  (output.size() < N )
		{
			output = "IMPOSSIBLE";
		}
		else
		{
			char a = output[0];
			char b = back(output);
			if ((a == 'O' && b != 'B' ) ||
				(a == 'G' && b != 'R' ) ||
				(a == 'V' && b != 'Y' ) ||
				(a == 'R' && (b == 'R' ||b == 'O' ||b == 'V' ) )  ||
				(a == 'Y' && (b == 'Y' ||b == 'O' ||b == 'G' ) )  ||
				(a == 'B' && (b == 'B' ||b == 'G' ||b == 'V' ) )  )
				output = "IMPOSSIBLE";
				
		}
		
		cout << "Case #" << t+1 << ": " << output << endl;
	}

}