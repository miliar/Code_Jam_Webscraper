#include <fstream>
#include <vector>
#include <cstring>

using namespace std;
typedef pair<int, int> ii;

int main(void)
{
	ifstream in("D-small-attempt1.in");
	ofstream out("D-small-attempt1.out");
	
	int t;
	in >> t;
	for(int index = 0; index < t; index++)
	{
		int N, M;
		in >> N >> M;
		
		char griglia[N][N];
		int punteggio = 0;
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < N; j++)
			{
				griglia[i][j] = '.';
			}
		}
		for(int i = 0; i < M; i++)
		{
			char modello;
			int a, b;
			in >> modello >> a >> b;
			
			if(modello == 'o')
			{
				punteggio += 2;
			}
			else
			{
				punteggio++;
			}
			griglia[a-1][b-1] = modello;
		}
		
		vector<pair<char, ii> > mosse;
		bool magicX[N][N];
		memset(magicX, false, sizeof(magicX));
		for(int i = 0; i < N; i++)
		{
			bool control = true;
			for(int j = 0; j < N; j++)
			{
				if((griglia[i][j] == 'x') || (griglia[i][j] == 'o'))
				{
					control = false;
					break;
				}
			}
			
			if(control)
			{
				for(int j = 0; j < N; j++)
				{
					control = true;
					for(int k = 0; k < N; k++)
					{
						if((griglia[k][j] == 'x') || (griglia[k][j] == 'o'))
						{
							control = false;
							break;
						}
					}
					
					if(control)
					{
						if(griglia[i][j] == '.')
						{
							mosse.push_back(pair<char, ii>('x', ii(i, j)));
							griglia[i][j] = 'x';
							punteggio++;
							magicX[i][j] = true;
						}
						else
						{
							mosse.push_back(pair<char, ii>('o', ii(i, j)));
							griglia[i][j] = 'o';
							punteggio++;
						}
						break;
					}
				}
			}
		}
		
		for(int i = 0; i < N; i++)
		{
			bool control = true;
			for(int j = 0; j < N; j++)
			{
				if(i-j >= 0)
				{
					if((griglia[j][i-j] == '+') || (griglia[j][i-j] == 'o'))
					{
						control = false;
						break;
					}
				}
				else
				{
					break;
				}
			}
			if(control)
			{
				for(int j = 0; j < N; j++)
				{
					if(i+j < N)
					{
						if((griglia[j][i+j] == '+') || (griglia[j][i+j] == 'o'))
						{
							control = false;
							break;
						}
					}
					else
					{
						break;
					}
				}
				if(control)
				{
					if(griglia[0][i] == '.')
					{
						mosse.push_back(pair<char, ii>('+', ii(0, i)));
						griglia[0][i] = '+';
						punteggio++;
					}
					else
					{
						if(magicX[0][i])
						{
							for(vector<pair<char, ii> >::iterator j = mosse.begin(); j != mosse.end(); j++)
							{
								if(((j->second).first == 0) && ((j->second).second) == i)
								{
									mosse.erase(j);
									break;
								}
							}
						}
						mosse.push_back(pair<char, ii>('o', ii(0, i)));
						griglia[0][i] = 'o';
						punteggio++;
					}
				}
			}
		}
		
		for(int i = 0; i < N; i++)
		{
			bool control = true;
			for(int j = 0; j < N; j++)
			{
				if(i-j >= 0)
				{
					if((griglia[N-1-j][i-j] == '+') || (griglia[N-1-j][i-j] == 'o'))
					{
						control = false;
						break;
					}
				}
				else
				{
					break;
				}
			}
			if(control)
			{
				for(int j = 0; j < N; j++)
				{
					if(i+j < N)
					{
						if((griglia[N-1-j][i+j] == '+') || (griglia[N-1-j][i+j] == 'o'))
						{
							control = false;
							break;
						}
					}
					else
					{
						break;
					}
				}
				if(control)
				{
					if(griglia[N-1][i] == '.')
					{
						mosse.push_back(pair<char, ii>('+', ii(N-1, i)));
						griglia[N-1][i] = '+';
						punteggio++;
					}
					else
					{
						if(magicX[N-1][i])
						{
							for(vector<pair<char, ii> >::iterator j = mosse.begin(); j != mosse.end(); j++)
							{
								if(((j->second).first == N-1) && ((j->second).second) == i)
								{
									mosse.erase(j);
									break;
								}
							}
						}
						mosse.push_back(pair<char, ii>('o', ii(N-1, i)));
						griglia[N-1][i] = 'o';
						punteggio++;
					}
				}
			}
		}
		
		for(int i = 0; i < N; i++)
		{
			bool control = true;
			for(int j = 0; j < N; j++)
			{
				if(i-j >= 0)
				{
					if((griglia[i-j][j] == '+') || (griglia[i-j][j] == 'o'))
					{
						control = false;
						break;
					}
				}
				else
				{
					break;
				}
			}
			if(control)
			{
				for(int j = 0; j < N; j++)
				{
					if(i+j < N)
					{
						if((griglia[i+j][j] == '+') || (griglia[i+j][j] == 'o'))
						{
							control = false;
							break;
						}
					}
					else
					{
						break;
					}
				}
				if(control)
				{
					if(griglia[i][0] == '.')
					{
						mosse.push_back(pair<char, ii>('+', ii(i, 0)));
						griglia[i][0] = '+';
						punteggio++;
					}
					else
					{
						if(magicX[i][0])
						{
							for(vector<pair<char, ii> >::iterator j = mosse.begin(); j != mosse.end(); j++)
							{
								if(((j->second).first == i) && ((j->second).second) == 0)
								{
									mosse.erase(j);
									break;
								}
							}
						}
						mosse.push_back(pair<char, ii>('o', ii(i, 0)));
						griglia[i][0] = 'o';
						punteggio++;
					}
				}
			}
		}
		
		for(int i = 0; i < N; i++)
		{
			bool control = true;
			for(int j = 0; j < N; j++)
			{
				if(i-j >= 0)
				{
					if((griglia[i-j][N-1-j] == '+') || (griglia[i-j][N-1-j] == 'o'))
					{
						control = false;
						break;
					}
				}
				else
				{
					break;
				}
			}
			if(control)
			{
				for(int j = 0; j < N; j++)
				{
					if(i+j < N)
					{
						if((griglia[i+j][N-1-j] == '+') || (griglia[i+j][N-1-j] == 'o'))
						{
							control = false;
							break;
						}
					}
					else
					{
						break;
					}
				}
				if(control)
				{
					if(griglia[i][N-1] == '.')
					{
						mosse.push_back(pair<char, ii>('+', ii(i, N-1)));
						griglia[i][N-1] = '+';
						punteggio++;
					}
					else
					{
						if(magicX[i][N-1])
						{
							for(vector<pair<char, ii> >::iterator j = mosse.begin(); j != mosse.end(); j++)
							{
								if(((j->second).first == i) && ((j->second).second) == N-1)
								{
									mosse.erase(j);
									break;
								}
							}
						}
						mosse.push_back(pair<char, ii>('o', ii(i, N-1)));
						griglia[i][N-1] = 'o';
						punteggio++;
					}
				}
			}
		}
		
		out << "Case #" << index+1 << ": " << punteggio << " " << mosse.size() << endl;
		for(vector<pair<char, ii> >::iterator i = mosse.begin(); i != mosse.end(); i++)
		{
			out << i->first << " " << (i->second).first+1 << " " << (i->second).second+1 << endl;
		}
	}
	
	return 0;
}
