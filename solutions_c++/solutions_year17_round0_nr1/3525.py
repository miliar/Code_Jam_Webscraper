#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
#include <climits>
#include <queue>
#include <numeric>
#include <thread>
using namespace std;
#define MAXV 900
#define MAXN 1005
int aa[MAXN];
int bb[MAXN];
int A[MAXN][MAXN];
int b[MAXN];
int N, M;
void eliminate(int j, int i)
{
	for (size_t k = 0; k < M; k++)
		A[j][k] ^= A[i][k];
}
bool rowAllZero(int i)
{
	for (size_t j = 0; j < M; j++)
	{
		if (A[i][j] != 0)
			return false;
	}
	return true;
}
vector<int> Gauss(int &state)
{
	//state -1 无解 0 唯一解 1 无穷解
	//N个方程,M个未知数
	state = 0;
	//处理上三角矩阵
	for (size_t i = 0; i < N; i++)
	{
		bool find = false;
		//令对角线上的元素 !=0
		for (size_t j = i; j < M && (!find); j++)
		{
			if (A[j][i]!=0)
			{
				for (size_t k = 0; k < M; k++)
					swap(A[i][k], A[j][k]);
				swap(b[i], b[j]);
				find = true;
				break;
			}
		}
		//多解的情况
		if (!find)
		{
			//state = 1;
			continue;
		}
		//将当前列第i行后的所有行都化为0（非上三角部分的化为0）
		for (size_t j = i + 1; j < N; j++)
		{
			if (A[j][i] == 0) continue;
			eliminate(j,i);
			b[j] = b[j] ^ b[i];
		}
	}
	//判断无解
	for (size_t i = 0; i < N; i++)
	{
		bool allZero = true;
		allZero = rowAllZero(i);
		if (allZero && b[i] != 0)
		{
			state = -1;
			return vector<int>();
		}
	}
	//判断无穷解
	if (state == 1)	return vector<int>();
	//求值过程
	vector<int> result(MAXN, 0);
	for (int i = N - 1; i >= 0; i--)
	{
		for (size_t j = 0; j < M; j++)
		{
			b[i] ^= result[j]*A[i][j];
			//A[i][j] = 0;
		}
		result[i] = b[i];
	}
	return result;
}
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	int T,K;
	string initstate;
	cin >> T;
	for (size_t i = 1; i <= T; i++)
	{
		fill_n(A[0], MAXN*MAXN, 0);
		fill(b,b+ MAXN, 0);
		cin >> initstate >> K;
		N = initstate.length();
		M = N;
		for (size_t j = 0; j < N; j++)
		{
			b[j] = (initstate[j] == '+') ? 1 : 0;
			b[j] ^= 1;
		}
		for (int j = 0; j < N; j++)
		{
			for (int k=j-K+1;k<=j;k++)
			{
				if (k >= 0 && k + K - 1 < N)
				{
					A[j][k] = 1;
				}
			}
		}
		vector<int> result;
		int state;
		result = Gauss(state);
		if (state == -1)
			cout <<"Case #"<<i<<": "<<"IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << count(result.begin(), result.end(), 1) << endl;
	}

	return 0;
}
