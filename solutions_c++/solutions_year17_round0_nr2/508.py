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

std::string number;

void read_task(std::fstream & input, std::fstream & output)
{
	input >> number;
}

void solve_task(std::fstream & input, std::fstream & output)
{
	for(int i = 0; i + 1 < number.size(); i++)
	{
		if(number[i] > number[i+1])
		{
			int j = i;
			for(; j >= 0 && number[j] == number[i]; j--);
			j++;

			number[j]--;

			j++;
			for(; j < number.size(); j++)
			{
				number[j] = '9';
			}
			break;
		}
	}
	std::string ret = std::string(number.begin() + number.find_first_not_of('0'), number.end());
	output << ret;
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
