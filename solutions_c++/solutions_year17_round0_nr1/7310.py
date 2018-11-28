#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, n) for( int i = 0; i < (int)(n); i++)

void Flip(char* str, int length)
{
	for (int i = 0; i < length; i++)
	{
		if (str[i] == '-')
		{
			str[i] = '+';
		}
		else
		{
			str[i] = '-';
		}
	}
}

void Pancakes()
{
	FILE* input = fopen("..\\Input\\A-large.in", "rt");
	FILE* output = fopen("..\\Output\\Pancakes.out", "wt");

	int testcase = 0;

	fscanf(input, "%d ", &testcase);

	for(int z = 0; z < testcase; z++)
	{
		int K = 0;
		int len = 0;
		char arr[10000] = { '\0' };
		int res = 0;

		fscanf(input, "%s %d", arr, &K);
		len = strlen(arr);

		for (int i = 0; i < len - K + 1; i++)
		{
			if (arr[i] == '-')
			{
				Flip(arr + i, K);
				res += 1;
			}
		}

		for (int i = len - K; i < len; i++)
		{
			if (arr[i] == '-')
			{
				res = -1;
			}
		}

		if (res == -1)
		{
			fprintf(output, "Case #%d: %s\r", z + 1, "IMPOSSIBLE");
		}
		else
		{
			fprintf(output, "Case #%d: %d\r", z + 1, res);
		}

		
				
		
	}

	/*while(1)
	{
		
		int pos = 0;
		int res = 0;

		while(1)
		{
			res = fscanf(input, "%d %d %d %d ", &A[pos][0], &A[pos][1], &B[pos][0], &B[pos][1]);
			if(res == EOF)
			{
				return;
			}

			if(testcase == 0 && pos == 6)
			{
				break;
			}
			else if(testcase == 1 && pos == 9)
			{
				break;
			}

			pos++;
		}
		testcase++;

		int count = 0;

		for(int i = 0; i < pos; i++)
		{
			for(int j = i + 1; j < pos; j++)
			{
				if(A[i][1] < A[j][1] && B[i][1] > B[j][1])
				{
					count++;
				}
				else if(A[i][1] > A[j][1] && B[i][1] < B[j][1])
				{
					count++;
				}
			}
		}

		fprintf(output, "%d\r\n", count);
	}*/


	/*while(1)
	{
		char str[1000] = { 0 };
		int value[256] = { 0 }, base = 0;
		int res = 0;

		res = fscanf(input, "%s\r\n", str);
		if(res == EOF)
		{
			break;
		}

		for (int i = 0; i < strlen(str); i++) 
		{
			if (value[str[i]] == 0) 
			{
				value[str[i]] = ++base;
			}
		}

		if (base <= 1) 
		{
			base = 2;
		}

		long long ans = 0;

		for (int i = 0; i < strlen(str); i++) 
		{
			long long tmp = value[str[i]];

			if (tmp == 1) 
			{

			} 
			else if (tmp == 2) 
			{
				tmp = 0;
			} else 
			{
				tmp--;
			}

			ans = ans*base + tmp;
		}
		fprintf(output, "%d\n", ans);
	}*/

/*
	double d[3] = { 0 };
	char str[1000] = { 0 };
	int pos = 0;
	
	while (1)
	{
		char a = 0;
		int res = 0;

		for(int j = 0; j < 8; j++)
		{
			double f = 0;

			for(int i = 0; i < 3; i++)
			{
				int res = fscanf(input, "%lf", &f);
				if(res == EOF)
				{
					break;
				}

				if(f <= 5)
				{
					d[i] = -5;
				}
				else
				{
					d[i] = 5;
				}
			}
			if(res == EOF)
			{
				break;
			}

			f = (d[0] + d[1] + d[2]) / 3;
			
			int bit = 0;
			
			if(f > 0.0)
			{
				bit = 1;
			}

			a = (a << 1) + bit;
		}
		if(res == EOF)
		{
			break;
		}

		fprintf(output, "%c", a);
	}*/

	/*for (int i = 1; i <= testCaseNum; i++)
	{
		unsigned int M = 0;
		unsigned int N = 0;
		fscanf(input, "%d %d ", &M, &N);

		vector<unsigned int> vect;

		unsigned int temp = 0;
		int res = 0;

		FOR(j, N)
		{
			fscanf(input, "%d ", &temp);
			vect.push_back(temp);
		}

		sort(vect.begin(), vect.end());

		FOR(j, vect.size())
		{
			if(vect[j] < A)
			{
				A += vect[j];
			}
			else if ( (A + A - 1) > vect[j] )
			{
				A += vect[j] + (A - 1);
				res += 1;
			}
			else if ( (A + A - 1) <= vect[j] )
			{
				res += vect.size() - j;
				break;
			}
		}

		fprintf(output, "Case #%d: %d\r\n", i, res);
	}*/
}

/*
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

#define FOR(i, n) for( int i = 0; i < (int)(n); i++)
#define MoteMaxSize 100

void round1_1()
{
	int testCaseNum = 0;

	FILE* input = fopen("..\\Input\\A-small-attempt3.in", "rt");
	FILE* output = fopen("..\\Output\\A-small-attempt3.out", "wt");
		

	fscanf(input, "%d\r\n", &testCaseNum);

	for (int i = 1; i <= testCaseNum; i++)
	{
		unsigned int A = 0;
		unsigned int N = 0;
		fscanf(input, "%d %d ", &A, &N);
		
		vector<unsigned int> vect;

		unsigned int temp = 0;
		int res = -1;
		unsigned int z = 0;

		do
		{
			if(A == 1)
			{
				res = N;
				break;
			}
			else if (A > MoteMaxSize)
			{
				res = 0;
				break;
			}
			for(z = 0; z < N; z++)
			{
				fscanf(input, "%d ", &temp);

				if(temp < A)
				{
					A += temp;
				}
				else
				{
					vect.push_back(temp);
				}

				if(A > MoteMaxSize)
				{
					res = 0;
					z++;
					break;
				}
			}
		} while(false);

		if (res != -1)
		{
			for(z; z < N; z++)
			{
				fscanf(input, "%d ", &temp);
			}
			fprintf(output, "Case #%d: %d\r\n", i, res);
			continue;
		}

		res = 0;
		sort(vect.begin(), vect.end());

		FOR(j, vect.size())
		{
			if(vect[j] < A)
			{
				A += vect[j];
			}
			else if ( (A + A - 1) > vect[j] )
			{
				A += vect[j] + (A - 1);
				res += 1;
			}
			else if ( (A + A - 1) <= vect[j] )
			{
				res += vect.size() - j;
				break;
			}
		}

		fprintf(output, "Case #%d: %d\r\n", i, res);
	}
}
*/