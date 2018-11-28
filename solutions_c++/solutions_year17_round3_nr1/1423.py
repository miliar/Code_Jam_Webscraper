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

#define DIE(format, ...) do{ wprintf(L"DIE: "format, ##__VA_ARGS__); }while(0);

typedef int sint32;
typedef long long sint64;
typedef sint64 sint;
typedef unsigned uint32;
typedef unsigned long long uint64;
typedef uint64 uint;

const int MAX = 1000;
const double PI = 3.14159265359;

struct PANCAKE
{
	double	R, H, S;
};

int			N, K;

std::vector<PANCAKE*>	PK;

bool byR(PANCAKE* a, PANCAKE* b)
{
	return a->R < b->R;
}

bool byS(PANCAKE* a, PANCAKE* b)
{
	return a->S < b->S;
}

void read_task(std::fstream & input, std::fstream & output)
{
	input >> N >> K;
	for(int i = 0; i < N; i++)
	{
		input >> PK[i]->R >> PK[i]->H;
		PK[i]->S = 2 * PK[i]->R * PK[i]->H;
	}
}

void solve_task(std::fstream & input, std::fstream & output)
{
	double best = 0;
	std::sort(PK.begin(), PK.begin() + N, byR);
	for(int i = K-1; i < N; i++)
	{
		std::vector<PANCAKE*> PK1(PK.begin(), PK.begin() + i);
		std::sort(PK1.begin(), PK1.end(), byS);

		double val = PK[i]->R*PK[i]->R + PK[i]->S;

		for(int j = i - (K-1); j < i; j++)
		{
			val += PK1[j]->S;
		}

		best = std::max(best, val);
	}

	best = best*PI;
	char str[256];
	sprintf(str, "%-16.7f", best);
	output << str;
}

int main(int argc, _TCHAR* argv[])
{
	int cTask, iTask;
	std::fstream input, output;

	input.open("input.in" , std::ios_base::in);
	output.open("output.out" , std::ios_base::out);

	PK.resize(MAX);
	for(int i = 0; i < MAX; i++)
	{
		PK[i] = new PANCAKE();
	}
	
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
