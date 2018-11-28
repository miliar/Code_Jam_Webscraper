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

const uint MAX = 200;

sint64 N, Q;	
sint64 E[MAX], S[MAX];
sint64 D[MAX][MAX];
sint64 U, V;
double T[MAX];

void read_task(std::fstream & input, std::fstream & output)
{
	sint64 i, j;
	input >> N >> Q;
	for(i = 1; i <= N; i++)
		input >> E[i] >> S[i];
	for(i = 1; i <= N; i++)
		for(j = 1; j <= N; j++)
			input >> D[i][j];
	for(i = 1; i <= Q; i++)
		input >> U >> V;
}

void solve_task(std::fstream & input, std::fstream & output)
{
	sint64 i, j, d;
	T[1] = 0;
	for(i = 2; i <= N; i++)
	{
		T[i] = 10e20;
		d = 0;
		for(j = i - 1; j >= 1; j--)
		{
			d += D[j][j+1];
			if(E[j] >= d)
			{
				double tmp = T[j] + (((double)d) / ((double)S[j]));
				T[i] = std::min(T[i], tmp);
			}
		}
	}
	char str[256];
	sprintf(str, "%-16.6f", T[N]);
	output << str;
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
		output << std::endl;
	}

	input.close();
	output.close();
	wprintf(L"DONE\n");
	getch();
	return 0;
}
