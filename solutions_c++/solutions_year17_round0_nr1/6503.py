#if 1
#define _CRT_SECURE_NO_WARNINGS
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

/* ID Coinjam */

const int MAX_PANCAKE = 1000;
int T, K;
int pancake[MAX_PANCAKE];
string sample;
int cnt = 0;

int FindBack(string& str, int s)
{
	//cout << "FindBack start" << endl;
	while (s < str.size() && str[s] == '+')
		s++;
	//cout << "FindBack end" << endl;
	return s;
}

void FlipPanCake(string& str, int s)
{
	//cout << "FlipPanCake start" << endl;
	for (int i = s; i < s + K; i++)
	{
		if (str[i] == '+')
			str[i] = '-';
		else
			str[i] = '+';
		
	}
	cnt++;
	//cout << str << endl;
	//cout << "FlipPanCake end" << endl;
}

int CheckPossiblity(string& str)
{
	int N = str.size();
	if (N < K)
	{
		for (int i = 0; i < N; i++)
			if (str[i] == '-')
				return -1;
	}
	else
	{
		for (int i = N - K + 1; i < N; i++)
		{
			if (str[i] == '-')
				return -1;
		}
	}

	return 1;
}

string resultPrint[100];

void PanCake()
{
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//fout.open("PanCake_Small1.txt");

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> sample >> K;
		cnt = 0;
		//cout << sample.size() << endl;
		//cout << K << endl;

		int N = sample.size();
		int pos = 0;
		for (int i = 0; i <= N - K; i++)
		{
			//cout << i << endl;
			pos = FindBack(sample, pos);
			//cout << "pos = " << pos << endl;
			if (N-K < pos)
				break;
			FlipPanCake(sample, pos);
			pos++;
		}

		int result = CheckPossiblity(sample);

		cout << "Case #" << t << ": ";
		if (result == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << cnt << endl;

		//cout << "Case #" << t << ": ";
		//cout << resultPrint[t - 1] << endl;

	}

	//for (int t = 1; t <= T; t++)
	//{
	//	cout << "Case #" << t << ": ";
	//	cout << resultPrint[t - 1] << endl;
	//}
}

int main()
{
	PanCake();
	return 0;
}

#endif