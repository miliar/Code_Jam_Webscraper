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

#define SMALL
#ifndef SMALL
#define LARGE
#endif // SMALL

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

		int64_t N, K;
		cin >> N >> K;

		vector<int> gaps;
		gaps.push_back(N);

		int minimal = N;
		int maximal = N;

		for(int i = 0; i < K; ++i)
		{
			int largestGap = gaps.back();
			--largestGap;
			minimal = largestGap / 2;
			maximal = largestGap - minimal;
			gaps.pop_back();

			gaps.push_back(minimal);
			gaps.push_back(maximal);
			
			sort(gaps.begin(), gaps.end());
		}

		printf("%d %d\n", maximal, minimal);
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