// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string> 
#include <vector>
#include <deque>          // std::deque
#include <list>           // std::list
#include <queue>          // std::queue
#include <memory>
#include <cstdio>
#include <strstream>
#include <iterator>
#include <sstream>
#include <stdarg.h>
#include <unordered_map>
#include <map>
#include <cassert>
#include "LargeNumber.h"
#include <math.h>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


enum ModelType
{
	EMPTY,
	PLUS,
	CROSS,
	CIRCLE
};

string solve1(int n);
string solveTidyNumbers(string);
string solveOversizedPancakeFlipper(string s, int n);
string solveBathroomStallsSmall(int n, int k);
string solveBathroomStallsSmall2(CLargeNumber n, CLargeNumber k);
void solveFashionShow(int n, ModelType matrix[100][100]);
int solve2(std::string str);
std::string solveAmpleSyrup(int n, int k);

void main() {
	freopen("A-small-attempt2.in", "r", stdin);
	//freopen("input.txt", "w", stdout);
	freopen("A-small-attempt2.out", "w", stdout);
	int t, n, m;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		//cin >> n;  // read n and then m.
		//auto res = solve1(n);


		//int n = 0, k;
		//cin >> n >> k;

		//int k;
		//char s[1000];
		//char s2[1000];
		//cin >> s >> s2;
		//string str = s;
		//CLargeNumber bn(str);
		//cout << "Case #" << i << ": " << solveBathroomStallsSmall2(bn, CLargeNumber(s2)).c_str() << endl;

		int n, k;
		cin >> n >> k;

		auto result = solveAmpleSyrup(n, k);

		cout << "Case #" << i << ": " << result.c_str() << endl;
		
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

string solve1(int n)
{
	bool flags[10] = {false};
	int count = 0;
	int number = 0;
	if (n == 0)
		return "INSOMNIA";
	else{
		int save = n;
		while (count < 10)
		{
			number++;
			n = save *  number;
			int f = n;
			while (f >= 1)
			{
				int d = f%10;
				f /= 10;
				if (flags[d] == false) count++;
				flags[d] = true;
			}
		}
		auto res = std::to_string(save *  number);
		return res;
	}
}

int solve2(std::string str)
{
	std::vector<bool> listHappy;
	int count = str.length();
	for (int i = 0; i < count; i++)
	{
		bool type = str[i] == '+';
		if (listHappy.size() == 0 || listHappy.at(listHappy.size() - 1) != type)
			listHappy.push_back(type);
	}
	if (count == 0) return 0;
	else
	{
		bool happyFirst = listHappy[0];
		if (happyFirst)
		{
			if (listHappy.size() == 1)
				return 0;
			else if ((listHappy.size() % 2) == 0)
				return listHappy.size();
			else
				return listHappy.size() - 1;
		}
		else
		{
			if ((listHappy.size() % 2) == 1)
				return listHappy.size();
			else
				return listHappy.size() - 1;
		}
	}
}

vector<int> listN;

void doSmallerAtPos(int pos, int value)
{


	if (value < listN[pos])
	{
		listN[pos]--;

		for (int i = pos + 1; i < listN.size(); i ++)
			listN[i] = 9;
	}

	if (pos > 0)
	{
		doSmallerAtPos(pos - 1, listN[pos]);
	}
}

void doTidyAtPos(int pos)
{
	if (pos == 0)
		return;
	else
		doSmallerAtPos(pos - 1, listN[pos]);
}


string solveTidyNumbers(string s)
{
	listN.clear();
	for (int i = 0; i < s.length(); i++)
	{
		listN.push_back(s.at(i) - '0');
	}
	doTidyAtPos(listN.size() - 1);

	bool first = true;
	string result = "";
	for (int i = 0; i < listN.size(); i++)
	{
		if (listN[i] == 0)
		{
			if (first == false)
			{
				result = result + std::to_string(0);
			}
		}
		else{
			result = result + std::to_string(listN[i]);
			first = false;
		}
	}

	return result;
}

enum type_cake{
	happy,
	empty
};

int removeHappy(std::list<type_cake> &listCake)
{
	int count = 0;
	while (listCake.size() > 0 && listCake.front() == happy)
	{
		count++;
		listCake.pop_front();
	}

	return count;
}

void flipCake(std::list<type_cake> &listCake, int n)
{
	if (listCake.size() >= n)
	{
		auto it = listCake.begin();
		int i = 0;
		while (i < n)
		{
			if (*it == happy)
				*it = empty;
			else
				*it = happy;
			i++;
			it++;
		}
	}
}

string solveOversizedPancakeFlipper(string s, int n)
{
	std::list<type_cake> listCake;
	for (int i = 0; i < s.length(); i++)
	{
		auto t = (s.at(i) == '+') ? happy : empty;
		listCake.push_back(t);
	}
	

	int count = 0;
	removeHappy(listCake);

	while (listCake.size() > 0)
	{
		flipCake(listCake, n);
		count++;
		int count1 = removeHappy(listCake);
		if (listCake.size() == 0)
			break;


		if (count1 == 0)
			return "IMPOSSIBLE";
	}

	if (listCake.size() > 0)
		return "IMPOSSIBLE";
	return to_string(count);
}

void insertSort(vector<int> &listStall, int min, int max)
{
	auto it = listStall.begin();
	while (it != listStall.end())
	{
		if (*it < max)
		{
			it = listStall.insert(it, min);
			listStall.insert(it, max);
			return;
		}
		it++;
	}

	listStall.push_back(max);
	listStall.push_back(min);
}

string solveBathroomStallsSmall(int n, int k)
{
	vector<int> listStall;
	listStall.push_back(n);
	auto min = 0;
	auto max = 0;
	while (k > 0)
	{
		k--;
		auto it_max = listStall.begin();

		float value = *it_max - 1;
		listStall.erase(it_max);

		max = ceil(value / 2.0f);
		min = floor(value / 2.0f);
		insertSort(listStall, min, max);
	}
	return to_string(max) + " " + to_string(min);
}

struct Stall
{
	CLargeNumber value;
	CLargeNumber num;
};

void insertSort(vector<Stall> &listStall, CLargeNumber v, CLargeNumber n)
{
	auto it = listStall.begin();
	while (it != listStall.end())
	{
		if ((*it).value == v)
		{
			(*it).num+=n;
			return;
		}
		it++;
	}

	listStall.push_back({ v, n });
}

string solveBathroomStallsSmall2(CLargeNumber n, CLargeNumber k)
{
	vector<Stall> listStall;
	listStall.push_back({ n, 1 });
	CLargeNumber min = 0;
	CLargeNumber max = 0;
	auto zero = CLargeNumber(0);
	while (k > zero)
	{
		auto it_max = listStall.begin();

		CLargeNumber value = (*it_max).value - CLargeNumber(1);
		if (k >= (*it_max).num)
			k -= (*it_max).num;
		else
			k = 0;

		CLargeNumber numAdd = (*it_max).num;
		listStall.erase(it_max);

		min = value / CLargeNumber(2);
		max = value - min;
		insertSort(listStall, max, numAdd);
		insertSort(listStall, min, numAdd);

	}
	return max.ToString() + " " + min.ToString();

}

bool validCell(int i, int j, int n)
{
	return i >= 0 && i < n && j >= 0 && j < n;
}

vector<ModelType> checkRowType = { EMPTY };
vector<ModelType> checkColumnType = { EMPTY };

bool checkRowColumnSameType(ModelType type, ModelType matrix[100][100], int row, int col, int n)
{
	//for (int i = 0; i < n; i++)
	//{
	//	if ((matrix[row][i] == type && i != col) || (matrix[i][col] == type && i != row)) return true;
	//}
	return (checkRowType[row] == type) || (checkColumnType[col] == type);
}

bool checkCrossSameType(ModelType type, ModelType matrix[100][100], int row, int col, int n)
{
	for (int i = 1; i < n; i++)
	{
		if (validCell(row - i, col - i, n) && matrix[row - i][col - i] == type) return true;
		if (validCell(row - i, col + i, n) && matrix[row - i][col + i] == type) return true;
		if (validCell(row + i, col - i, n) && matrix[row + i][col - i] == type) return true;
		if (validCell(row + i, col + i, n) && matrix[row + i][col + i] == type) return true;
	}

	return false;
}

bool validModel(ModelType matrix[100][100], int i, int j, int n)
{
	switch (matrix[i][j])
	{
	case CIRCLE:
	{
		if (checkRowColumnSameType(CIRCLE, matrix, i, j, n))
			return false;
		if (checkCrossSameType(CIRCLE, matrix, i, j, n))
			return false;
		if (checkRowColumnSameType(CROSS, matrix, i, j, n))
			return false;
		if (checkCrossSameType(PLUS, matrix, i, j, n))
			return false;
		break;
	}
	case CROSS:
	{
		if (checkRowColumnSameType(CIRCLE, matrix, i, j, n))
			return false;
		if (checkRowColumnSameType(CROSS, matrix, i, j, n))
			return false;
		break;
	}
	case PLUS:
	{
		if (checkCrossSameType(CIRCLE, matrix, i, j, n))
			return false;
		if (checkCrossSameType(PLUS, matrix, i, j, n))
			return false;
		break;
	}
	}

	return true;
}

int calculatePoint(ModelType matrix[100][100], int n)
{
	int count = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			switch (matrix[i][j])
			{
			case CIRCLE:
			{
				count += 2;
				break;
			}
			case CROSS:
			case PLUS:
			{
				count += 1;
				break;

			}
			}
		}
	}

	return count;
}

//template<typename ... Args>
//string string_format(const std::string& format, Args ... args)
//{
//	size_t size = std::snprintf(nullptr, 0, format.c_str(), args ...) + 1; // Extra space for '\0'
//	unique_ptr<char[]> buf(new char[size]);
//	snprintf(buf.get(), size, format.c_str(), args ...);
//	return string(buf.get(), buf.get() + size - 1); // We don't want the '\0' inside
//}

std::string string_format(const std::string fmt_str, ...) {
	int final_n, n = ((int)fmt_str.size()) * 2; /* reserve 2 times as much as the length of the fmt_str */
	std::string str;
	std::unique_ptr<char[]> formatted;
	va_list ap;
	while (1) {
		formatted.reset(new char[n]); /* wrap the plain char array into the unique_ptr */
		strcpy(&formatted[0], fmt_str.c_str());
		va_start(ap, fmt_str);
		final_n = vsnprintf(&formatted[0], n, fmt_str.c_str(), ap);
		va_end(ap);
		if (final_n < 0 || final_n >= n)
			n += abs(final_n - n + 1);
		else
			break;
	}
	return std::string(formatted.get());
}

struct OutputData
{
	char type;
	int i;
	int j;
};

void solveFashionShow(int n, ModelType matrix[100][100])
{
	auto countChangeModel = 0;
	string resultChange = "";
	checkRowType.clear();
	checkColumnType.clear();
	for (int i = 0; i < n; i++)
		checkRowType.push_back(EMPTY);
	for (int j = 0; j < n; j++)
		checkColumnType.push_back(EMPTY);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (matrix[i][j] == CIRCLE || matrix[i][j] == CROSS)
			{
				checkRowType[i] = matrix[i][j];
				checkColumnType[j] = matrix[i][j];
			}
		}
	}

	vector<OutputData> listOutput;
	//bool flag[100][100] = { false };
	int repeat = 0;
	for (; repeat < 2; repeat++)
	{
		for (int i = n - 1; i >= 0; i--)
		{
			for (int j = n - 1; j >= 0; j--)
			{
				//if (flag[i][j] == false)
				//	flag[i][j] = true;
				//else continue;
				auto saveValue = matrix[i][j];
				//if (matrix[i][j] == EMPTY)
				{
					if (saveValue != CIRCLE && repeat == 1)
					{
						matrix[i][j] = CIRCLE;

						if (validModel(matrix, i, j, n))
						{
							checkRowType[i] = CIRCLE;
							checkColumnType[j] = CIRCLE;
							countChangeModel++;
							listOutput.push_back({ 'o', i + 1, j + 1 });
							//resultChange = string_format("%s\n%s %d %d", resultChange.c_str(), "o", i + 1, j + 1);
							continue;
						}
						matrix[i][j] = saveValue;
					}

					if (saveValue == EMPTY && repeat == 0)
					{
						matrix[i][j] = PLUS;

						if (validModel(matrix, i, j, n))
						{
							countChangeModel++;
							listOutput.push_back({ '+', i + 1, j + 1 });
							//resultChange = string_format("%s\n%s %d %d", resultChange.c_str(), "+", i + 1, j + 1);
							continue;
						}

						matrix[i][j] = saveValue;
					}

					if (saveValue == EMPTY && repeat == 0)
					{
						matrix[i][j] = CROSS;

						if (validModel(matrix, i, j, n))
						{
							checkRowType[i] = CROSS;
							checkColumnType[j] = CROSS;
							countChangeModel++;
							listOutput.push_back({ 'x', i + 1, j + 1 });
							//resultChange = string_format("%s\n%s %d %d", resultChange.c_str(), "x", i + 1, j + 1);
							continue;
						}
						matrix[i][j] = saveValue;
					}
				}
			}
		}
	}
	cout << to_string(calculatePoint(matrix, n)) + " " + to_string(countChangeModel) << endl;
	for (int i = 0; i < listOutput.size(); i++)
	{
		cout << listOutput[i].type << " " << listOutput[i].i << " " << listOutput[i].j << endl;
	}
}

#define M_PI           3.14159265358979323846  /* pi */
#define PI M_PI
vector<pair<long long, long long>> listArea;

long long findMaxSum(int pos, int remain, long long lastCircle)
{
	long long maxSum = 0;
	while (pos >= 0 && remain > 0)
	{
		long long sum = 0;
		sum += listArea[pos].first - lastCircle + findMaxSum(pos - 1, remain - 1, listArea[pos].second);
		maxSum = maxSum < sum ? sum : maxSum;

		pos--;
	}

	return maxSum;
}

std::string solveAmpleSyrup(int n, int k)
{
	listArea.clear();
	for (int i = 0; i < n; i++)
	{
		long long r, h, c;
		cin >> r;
		cin >> h;

		c = r*r;
		auto a = c + 2 *r*h;
		listArea.push_back(make_pair(a, c));
	}

	std::sort(listArea.begin(), listArea.end(), [](pair<long long, long long>a, pair<long long, long long>b){
		return a.second > b.second;
	});

	return string_format("%.9f", findMaxSum(listArea.size() - 1, k, 0) * PI);
}