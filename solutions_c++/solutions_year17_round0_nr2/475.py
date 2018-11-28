#include <fstream>
#include <cstring>

using namespace std;

int main(void)
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	
	int t;
	in >> t;
	for(int index = 0; index < t; index++)
	{
		string N;
		in >> N;
		
		int pos = -1;
		for(int i = 0; i < N.size()-1; i++)
		{
			if(N[i] > N[i+1])
			{
				pos = i;
				break;
			}
		}
		
		if(pos == -1)
		{
			out << "Case #" << index+1 << ": " << N << endl;
		}
		else
		{
			if((pos == 0) && (N[pos] == '1'))
			{
				out << "Case #" << index+1 << ": ";
				for(int i = 0; i < N.size()-1; i++)
				{
					out << "9";
				}
				out << endl;
			}
			else
			{
				N[pos]--;
				for(int i = pos+1; i < N.size(); i++)
				{
					N[i] = '9';
				}
				
				if(pos == 0)
				{
					out << "Case #" << index+1 << ": " << N << endl; 
				}
				else
				{
					bool control = false;
					for(int i = pos-1; i >= 0; i--)
					{
						if(N[i] > N[i+1])
						{
							if((i == 0) && (N[i] == '1'))
							{
								control = true;
								break;
							}
							else
							{
								N[i]--;
								for(int j = i+1; j < N.size(); j++)
								{
									N[j] = '9';
								}
							}
						}
						else
						{
							break;
						}
					}
					
					if(control)
					{
						out << "Case #" << index+1 << ": ";
						for(int i = 0; i < N.size()-1; i++)
						{
							out << "9";
						}
						out << endl;
					}
					else
					{
						out << "Case #" << index+1 << ": " << N << endl;
					}
				}
			}
		}
	}
	
	return 0;
}
