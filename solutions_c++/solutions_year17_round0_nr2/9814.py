#ifndef ALPER
#include <bits/stdc++.h>
#endif

#ifdef ALPER
#include <Windows.h>
#endif

#include <string>
#include <iostream>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;

bool is_ok(int i)
{
	string str = to_string(i);

	if (str.length() == 1)
	{
		return true;
	}

	for (int j = 0; j < str.length() - 1; ++j)
	{
		if (str[j + 1] < str[j])
			return false;
	}

	return true;
}

int answer(int N)
{
	for (int i = N; i >= 1; --i)
	{
		if (is_ok(i))
			return i;
	}
}

int main(int argc, char *argv[])
{
	int T;
	stringstream kk;


	cin >> T;
	int i = 1;
	while (T--)
	{
		kk << "Case #" << i++ << ": ";
		
		int N;
		cin >> N;

		kk << answer(N);
		
		kk << endl;
	}


#ifdef ALPER
	ofstream file("C:\\sonuc.txt");
	file << kk.str();
#endif // ALPER

#ifndef ALPER
	cout << kk.str();
#endif
	
	return 0;
}