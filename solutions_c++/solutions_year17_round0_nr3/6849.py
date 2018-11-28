#include <iostream>
#include <stdio.h>
#include <vector>
#include <map>
#include <time.h>

const long long unsigned int MAX_STALLS = 1000000000000000000;

using namespace std;

typedef struct stall
{
	bool taken;
	long long unsigned int distL;
	long long unsigned int distR;
//	struct stall *cL;
//	struct stall *cR;
} stall;

void printStall(const vector<stall> &stalls)
{
	cout << "[";
	for (size_t i = 0; i < stalls.size(); i++)
	{
		if (stalls[i].taken)
			cout << " 1";
		
		else
			cout << " 0";
	}
	cout << "]\n";
}

bool isPar(long long unsigned int num)
{
	return !(num % 2);
}

stall choose_min(std::map<long long unsigned int,stall> &stalls, long long unsigned int start, long long unsigned int end, long long unsigned int longestSoFar, long long unsigned int &longestIndex)
{	
	long long unsigned int i = start;
	long long unsigned int thisLongestSoFar = longestSoFar;
	
	if (stalls[i].distR > longestSoFar)
	{
		thisLongestSoFar = stalls[i].distR;
		longestIndex = i;
	}
	
	if (i + stalls[i].distR >= end) // Se passamos do alcance, retornamos
	{
		int paridade = isPar(thisLongestSoFar);
		stall newStall;
		newStall.taken = true;
		newStall.distR = thisLongestSoFar / 2;
		newStall.distL = stalls[longestIndex].distR = thisLongestSoFar / 2 - paridade;
		
				stalls[longestIndex + 1 - paridade + thisLongestSoFar / 2] = newStall;
		return 	stalls[longestIndex + 1 - paridade + thisLongestSoFar / 2];
	}
	
	return choose_min(stalls, i + 1 + stalls[i].distR, end, thisLongestSoFar, longestIndex);
}

int main()
{
	int T;
	long long unsigned int N, K;
	cin >> T;
	vector<int> Tees(T*2);
	for (size_t i = 0; i < Tees.size(); i+=2)
	{	
		cin >> N;
		cin >> K;
		Tees[i] 	= N;
		Tees[i + 1] = K;
	}

	
	
	for (int j = 0; j < Tees.size(); j+=2) 
	{
		long long unsigned int lsf = 0;
		long long unsigned int li = 0;
		std::map<long long unsigned int,stall> stalls;
		
		
		// Init o primeiro
		stall _1stStall;
		stall _NstStall;
		
		_1stStall.distR = Tees[j];
		_1stStall.distL = 0;
		_1stStall.taken = true;
		
		stalls[0] = _1stStall;	
		
		// Init o último
		_NstStall.distL = Tees[j];
		_NstStall.distR = 0;
		_NstStall.taken = true;
		
		stalls[Tees[j]] = _NstStall;
		
		for (long long unsigned int i = 0; i < Tees[j+1] - 1; i++)
		{	
			choose_min(stalls, 0, Tees[j], 0, li);
		}
		stall stallin = choose_min(stalls, 0, Tees[j], 0, li);
		cout << "Case #" << j/2 + 1 << ": " << (stallin.distL > stallin.distR ? stallin.distL : stallin.distR);
		cout << " " << (stallin.distL < stallin.distR ? stallin.distL : stallin.distR) << endl;
	}
}
