#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include <conio.h>
#include <map>
#include <list>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <stdint.h>
using namespace std;

#define DIE(format, ...) do{ wprintf(L"DIE: "format, ##__VA_ARGS__); DebugBreak(); }while(0);

typedef int sint32;
typedef long long sint64;
typedef sint64 sint;
typedef unsigned uint32;
typedef unsigned long long uint64;
typedef uint64 uint;

char	FORG[101][101];
char	F[101][101];
int		N, M;

void read_task(std::fstream & input, std::fstream & output)
{
	memset(FORG, 0, sizeof(FORG));

	input >> N >> M;
	for(int i = 0; i < M; i++)
	{
		char	V;
		int		R, C;
		input >> V >> R >> C;
		FORG[R][C] = V;
	}
	memcpy(F, FORG, sizeof(FORG));
}

void solve_rows_columns()
{
	int i, j;

	bool row[101];
	bool col[101];

	for(i = 1; i <= N; i++)
	{
		row[i] = false;
		for(j = 1; j <= N; j++)
		{
			if(F[i][j] == 'x' || F[i][j] == 'o')
			{
				row[i] = true;
				break;
			}
		}
	}
	
	for(j = 1; j <= N; j++)
	{
		col[j] = false;
		for(i = 1; i <= N; i++)
		{
			if(F[i][j] == 'x' || F[i][j] == 'o')
			{
				col[j] = true;
				break;
			}
		}
	}

	for(i = 1, j = 1; i <= N; i++)
	{
		if(!row[i])
		{
			for(; j <= N; j++)
			{
				if(!col[j])
				{
					row[i] = true;
					col[j] = true;
					
					if(F[i][j] == 'x' || F[i][j] == 'o')	
					{
						DIE(L"oops");
					}
					else if(F[i][j] == '+')	
					{
						F[i][j] = 'o';
					}
					else
					{
						F[i][j] = 'x';
					}

					break;
				}
			}
			if(!row[i])		DIE(L"oops");
		}
	}
}

void solve_diagonals()
{
	int i, j, k;

	for(k = 1; k <= N; k++)
	{
		bool bFree = true;

		for(i = 2, j = k - 1; i <= N && j >= 1; i++, j--)
		{
			if(F[i][j] == '+' || F[i][j] == 'o')
			{
				bFree = false;
				break;
			}
		}

		if(bFree)
		for(i = 2, j = k + 1; i <= N && j <= N; i++, j++)
		{
			if(F[i][j] == '+' || F[i][j] == 'o')
			{
				bFree = false;
				break;
			}
		}

		if(bFree)
		{	
			if( F[1][k]== '+' || F[1][k] == 'o')	
			{
			}
			else if(F[1][k] == 'x')	
			{
				F[1][k] = 'o';
			}
			else
			{
				F[1][k] = '+';
			}
		}
	}

	for(k = 1; k <= N; k++)
	{
		bool bFree = true;

		for(i = N - 1, j = k - 1; i >= 1 && j >= 1; i--, j--)
		{
			if(F[i][j] == '+' || F[i][j] == 'o')
			{
				bFree = false;
				break;
			}
		}

		if(bFree)
		for(i = N - 1, j = k + 1; i >= 1 && j <= N; i--, j++)
		{
			if(F[i][j] == '+' || F[i][j] == 'o')
			{
				bFree = false;
				break;
			}
		}

		if(bFree)
		{	
			if( F[N][k]== '+' || F[N][k] == 'o')	
			{
			}
			else if(F[N][k] == 'x')	
			{
				F[N][k] = 'o';
			}
			else
			{
				F[N][k] = '+';
			}
		}
	}

}

void solve_task(std::fstream & input, std::fstream & output)
{
	int i, j;


	solve_rows_columns();
	solve_diagonals();
	
#if 0
	printf("---------------------------------\n");
	for(i = 1; i <= N; i++)
	{
		for(j = 1; j <= N; j++)
		{
			printf("%c", F[i][j] ? F[i][j] : '.');
		}
		printf("\n");
	}
#endif

 	int cTotal = 0;
	int cPoints = 0;
	for(i = 1; i <= N; i++)
		for(j = 1; j <= N; j++)
		{
			if(FORG[i][j] != F[i][j])
			{
				cTotal++;
			}
			if(F[i][j] == '+' || F[i][j] == 'x')
				cPoints++;
			if(F[i][j] == 'o')
				cPoints+=2;
		}

	output << cPoints << " " << cTotal << std::endl;
	for(i = 1; i <= N; i++)
		for(j = 1; j <= N; j++)
		{
			if(FORG[i][j] != F[i][j])
			{
				output << F[i][j] << " " << i << " " << j << std::endl;
			}
		}
}

int main(int argc, _TCHAR* argv[])
{
	int cTask, iTask;
	std::fstream input, output;

	input.open("input.txt" , std::ios_base::in);
	output.open("output.txt" , std::ios_base::out);
	
	input >> cTask;
	for(iTask = 0; iTask < cTask; iTask++)
	{
		read_task(input, output);
		output << "Case #" << iTask + 1 << ": ";
		solve_task(input, output);
		//output << std::endl;
	}

	input.close();
	output.close();
	wprintf(L"DONE\n");
	getch();
	return 0;
}
