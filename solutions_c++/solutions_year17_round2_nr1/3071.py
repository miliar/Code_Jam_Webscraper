#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<map>
#include<unordered_map>
#include <iomanip>

using namespace std;

int D, N;
int k[1000];
int s[1000];


void _maininternal(int TEST)
{
	map<int, int> m;
	map<int, int>::reverse_iterator mri;
	int i;
	cin >> D >> N;
	int flag = 0;
	double time = 0;
	double time1 = 0;
	double time2 = 0;
	double speed;
	int distanceleft;

	for (i = 0; i < N; ++i)
	{
		cin >> k[i] >> s[i];
		m.insert(pair<int, int>(k[i], s[i]));
	}
	for (mri= m.rbegin(); mri != m.rend(); ++mri)
	{
		distanceleft = D - mri->first;
		time1 = ((double)distanceleft) / ((double)mri->second);
		if (time1 > time)
		{
			time = time1;
		}
	}
	speed = ((double)D) / time;
	std::cout << std::fixed;
	std::cout << std::setprecision(6);
	cout << speed;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cout<<"Case #"<<i<<": ";
		_maininternal(i);
		cout << endl;
	}
	return 0;
}
