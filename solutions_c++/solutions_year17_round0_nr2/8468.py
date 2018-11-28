#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>

#include <string>

#define repF(n) for(int i = 0; i < (n); ++i)
#define repR(n) for(int i = (n) - 1; i >= 0; --i)

static constexpr const char* s_smallIn = "small_in.txt";
static constexpr const char* s_smallOut = "small_out.txt";

static constexpr const char* s_bigIn = "big_in.txt";
static constexpr const char* s_bigOut = "big_out.txt";

void PrintCase(const int caseNum);

template<class T>
void SubdivideLine(const T& line, std::vector<T>& vecOut);

template<class T>
void FillVectorIO(std::vector<T>& vec, int elements);

template<class T>
using Vec2D = std::vector<std::vector<T>>;

using namespace std;

//#define SMALL
#ifndef SMALL
#define LARGE
#endif // SMALL

bool IsTidy(int num)
{
	int last = num % 10;
	int current = 0;

	while(num != 0)
	{
		current = num % 10;
		num /= 10;

		if(last < current)
		{
			return false;
		}

		last = current;
	}

	return true;
}

int main(char argc, char** argv)
{
	int cases = 0;

	{
		FILE* stream;
	
#ifdef SMALL
		freopen_s(&stream, s_smallIn, "rt", stdin);
		freopen_s(&stream, s_smallOut, "wt", stdout);
#endif // SMALL
#ifdef LARGE
		freopen_s(&stream, s_bigIn, "rt", stdin);
		freopen_s(&stream, s_bigOut, "wt", stdout);
#endif // LARGE
	}

	cin >> cases;

	for (int currentCase = 0; currentCase < cases; ++currentCase)
	{
		PrintCase(currentCase + 1);
	
		string num;
		cin >> num;

		if(num.size() > 1)
		{
			for(int i = num.size() - 1; i > 0; --i)
			{
				if(num[i] < num[i - 1])
				{
					num[i] = '9';
					--num[i - 1];
				}
				else
				{
					bool decrease = false;
					for(int j = i; j > 0; j--)
					{
						if(num[j] < num[j - 1])
						{
							decrease = true;
							break;
						}
					}

					if(decrease)
					{
						num[i] = '9';
						for(int j = i; j < 0; j--)
						{


							if(num[j] - 1 < num[j - 1])
							{
								num[j] = '9';
							}
							else
							{
								num[j]--;
								break;
							}
						}
					}
				}
			}
		}

		if(num.size() > 1)
		{
			if(num[0] != '0')
			{
				cout << num[0];
			}
		}
		else
		{
			cout << num[0];
		}

		for(int i = 1; i < num.size(); ++i)
		{
			cout << num[i];
		}
		cout << "\n";
	}
	
	return 0;
}

void PrintCase(int caseNum)
{
	printf("Case #%d: ", caseNum);
}

template<class T>
void SubdivideLine(const T& line, std::vector<T>& vecOut)
{
	vecOut.clear();
	istringstream iss(line);
	copy(istream_iterator<string>(iss),
		istream_iterator<string>(),
		back_inserter(vecOut));
}

template<class T>
void FillVectorIO(std::vector<T>& vec, int elements)
{
	for (int i = 0; i < elements; ++i)
	{
		T temp;
		cin >> temp;
		vec.push_back(std::move(temp));
	}
}