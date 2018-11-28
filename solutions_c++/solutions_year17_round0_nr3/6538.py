// bathroom.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>

#define max(a,b) (((a) > (b)) ? (a) : (b))
#define min(a,b) (((a) < (b)) ? (a) : (b))

typedef struct Value
{
	int l;
	int r;
	int minValue;
	int maxValue;
} Value;

int FindMin(int l, int r)
{
	return min(l, r);
}

int FindMax(int l, int r)
{
	return max(l, r);
}

typedef struct BathRoom
{
	std::string		status;
	int				numStall;
	int				minimax;
	int				maximax;
	std::vector<int> vMinimaxIndex;
	std::vector<Value>	values;

	BathRoom(int numSeat)
	{
		numStall = numSeat + 0;
		status = std::string(numStall, '.');
		values.reserve(numStall);
		for (int i = 0; i < numStall; ++i) {
			Value v;
			values.push_back(v);
		}
	}

	int FindLeftValue(int pos)
	{
		int empty = 0;
		int at = pos - 1;
		while (at >= 0 && status[at] == '.') {
			empty += 1;
			at -= 1;
		}

		return empty;
	}

	int FindRightValue(int pos)
	{
		int empty = 0;
		int at = pos + 1;
		while (at < numStall && status[at] == '.') {
			empty += 1;
			at += 1;
		}

		//if (at == numStall)			return -1;
		return empty;
	}

	void CalculateValue()
	{
		minimax = 0;

		for (int i = 0; i < numStall; ++i) {
			if (status[i] != '.')	
				continue;

			int l = FindLeftValue(i);
			int r = FindRightValue(i);

			auto& v = values[i];
			v.l = l;
			v.r = r;
			v.minValue = ::FindMin(l, r);
			v.maxValue = ::FindMax(l, r);

			if (v.minValue > minimax)	minimax = v.minValue;
		}

		vMinimaxIndex = FindMinimaxIndex();
		FindMaximaxValue();
	}

	std::vector<int> FindMinimaxIndex()
	{
		std::vector<int> vIndex;
		for (int i = 0; i < numStall; ++i) {
			if (status[i] != '.')
				continue;

			const auto& v = values[i];
			if (v.minValue == minimax) {
				vIndex.push_back(i);
			}
		}

		return vIndex;
	}

	void FindMaximaxValue()
	{
		maximax = 0;
		for (auto idx : vMinimaxIndex) {
			auto& v = values[idx];
			if (v.maxValue > maximax)
				maximax = v.maxValue;
		}
	}

	int FindEmptySeat()
	{
		if (vMinimaxIndex.size() == 1)
			return vMinimaxIndex[0];

		for (auto idx : vMinimaxIndex) {
			auto& v = values[idx];
			if (v.maxValue == maximax)
				return idx;
		}
		return -1;
	}

	void MovePeopleTo(int idx)
	{
		status[idx] = 'O';
	}
} BathRoom;


BathRoom CreateEmptyBathroom(int numSeat)
{
	BathRoom room(numSeat);
	//room.CalculateValue();

	return room;
}

BathRoom MovePeopleIn(const BathRoom& room)
{
	BathRoom output = room;
	output.CalculateValue();

	int seatIndex = output.FindEmptySeat();
	output.MovePeopleTo(seatIndex);

	return output;
}

BathRoom FindSolution(int numSeat, int numPeople)
{
	if (numSeat == numPeople) {
		BathRoom room = CreateEmptyBathroom(1);
		room.minimax = 0;
		room.maximax = 0;
		return room;
	}

	BathRoom room = CreateEmptyBathroom(numSeat);
	for (int i = 0; i < numPeople; ++i) {
		auto result = MovePeopleIn(room);
		room = result;
	}

	return room;
}
//////////////////////////////////////////////////////////////////////////
int main()
{
	std::ifstream in("input/C-small-1-attempt0.in");
	std::ofstream out("input/C-small-1-attempt0.out");
	
	int numCase;
	in >> numCase;
	for (int i = 1; i <= numCase; ++i) {
		int numSeat, numPeople;
		in >> numSeat >> numPeople;

		auto output = FindSolution(numSeat, numPeople);
		out << "Case #" << i << ": " << output.maximax << " " << output.minimax << std::endl;
	}
	//auto output = FindSolution(1000, 1);
    return 0;
}

