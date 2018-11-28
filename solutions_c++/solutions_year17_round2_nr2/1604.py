// Stable Neigh-bors.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <unordered_set>

std::vector<char> getString(int R, int O, int Y, int G, int B, int V)
{
	std::vector<char> result;

	if (G > 0)
	{
		for (int i = 0; i < G; i++)
		{
			result.push_back(*"R");
			result.push_back(*"G");
		}
		if (R > G)
		{
			
			result.push_back(*"R");
			R -= G + 1;
		}
		else R -= G;
	}
	if (O > 0)
	{
		for (int i = 0; i < O; i++)
		{
			result.push_back(*"B");
			result.push_back(*"O");
		}
		if (B > O)
		{

			result.push_back(*"B");
			B -= O + 1;
		}
		else B -= O;
	}
	if (V > 0)
	{
		for (int i = 0; i < V; i++)
		{
			result.push_back(*"Y");
			result.push_back(*"V");
		}
		if (Y > V)
		{

			result.push_back(*"Y");
			Y -= V + 1;
		}
		else Y -= V;
	}

	if (result.size() == 0)
	{
		if (B >= Y && B >= R)
		{
			result.push_back(*"B");
			B--;
		}
		else if (R >= Y)
		{
			result.push_back(*"R");
			R--;
		}
		else
		{
			result.push_back(*"Y");
			Y--;
		}
	}

	int N = B + R + Y;

	while (N > 0)
	{
		if (B > R && B > Y && (result.size() == 0 || result.back() != *"B"))
		{
			result.push_back(*"B");
			B--;
			N--;
		}
		else if (R > Y && R > B && (result.size() == 0 || result.back() != *"R"))
		{
			result.push_back(*"R");
			R--;
			N--;
		}
		else if (Y > R && Y > B && (result.size() == 0 || result.back() != *"Y"))
		{
			result.push_back(*"Y");
			Y--;
			N--;
		}
		else if (result.size() == 0 || result.back() == *"Y")
		{
			if (B > R)
			{
				result.push_back(*"B");
				B--;
				N--;
			}
			else if (R > B)
			{
				result.push_back(*"R");
				R--;
				N--;
			}
			else
			{
				if (result.size() == 0 || result.front() == *"R")
				{
					result.push_back(*"R");
					R--;
					N--;
				}
				else
				{
					result.push_back(*"B");
					B--;
					N--;
				}
			}
		}
		else if (result.size() == 0 || result.back() == *"B")
		{
			if (Y > R)
			{
				result.push_back(*"Y");
				Y--;
				N--;
			}
			else if (R > Y)
			{
				result.push_back(*"R");
				R--;
				N--;
			}
			else
			{
				if (result.size() == 0 || result.front() == *"R")
				{
					result.push_back(*"R");
					R--;
					N--;
				}
				else
				{
					result.push_back(*"Y");
					Y--;
					N--;
				}
			}
		}
		else if (result.size() == 0 || result.back() == *"R")
		{
			if (Y > B)
			{
				result.push_back(*"Y");
				Y--;
				N--;
			}
			else if (B > Y)
			{
				result.push_back(*"B");
				B--;
				N--;
			}
			else
			{
				if (result.size() == 0 || result.front() == *"B")
				{
					result.push_back(*"B");
					B--;
					N--;
				}
				else
				{
					result.push_back(*"Y");
					Y--;
					N--;
				}
			}
		}
	}
	return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nootests;
	std::cin >> nootests;
	for (int i = 1; i <= nootests; i++)
	{
		int N, R, O, Y, G, B, V;
		std::cin >> N >> R >> O >> Y >> G >> B >> V;
		std::cout << "Case #" << i << ": ";

		int Rtot = R + O + V;
		int Ytot = Y + O + G;
		int Btot = B + V + G;



		if ((Rtot > N / 2 || Ytot > N/2 || Btot > N/2 || (R < G +1 && G > 0) || (Y < V + 1 && V > 0) || (B < O + 1 && O > 0))
			&& !(R == G && R + G == N)
			&& !(Y == V && Y + V == N)
			&& !(B == O && B + O == N)
			)
		{
			
			std::cout << "IMPOSSIBLE" << std::endl;
			continue;
		}
		char firstChar = *" ";
		char previousChar = *" ";
		for (auto colour : getString(R, O, Y, G, B, V))
		{
			std::cout << colour;
		}
		std::cout << std::endl;
	}
	return 0;
}
