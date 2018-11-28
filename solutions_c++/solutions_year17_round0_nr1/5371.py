// flip.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int try_flip(string, unsigned int);

int _DBG_LOG_ = 0;

int main(int argc, char* argv[])
{
	// inputs
	int T;
	vector<string> S;
	vector<unsigned int> K;

	int from_file = 1;

	string inFileName = "D:\\DEV\\VS2012\\GoogleCodeJam\\201704\\01\\flip\\input.txt";

	ifstream inFile(inFileName);

	if(!from_file)
	{
		cin >> T;
	}
	else 
	{
		inFile >> T;
	}

	for(int i = 0; i < T; i++)
	{
		unsigned int k;
		string s;

		if(!from_file)
		{
			cin >> s >> k;
		}
		else
		{
			inFile >> s >> k;
		}

		S.push_back(s);
		K.push_back(k);
	}

	for(int i = 0; i < T; i++)
	{
		int cnt = try_flip(S[i], K[i]);

		cout << "Case #" << i + 1 << ": ";
		if(cnt >= 0)
		{
			cout << cnt << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
}

int try_flip(string S, unsigned int K)
{
	if(K > S.length())
	{
		if(_DBG_LOG_ == 1)
		{
			cout << "K > S.length !!!" << endl;
		}
		return -2;
	}
	
	if(_DBG_LOG_ == 1)
	{
		cout << S << endl;
	}

	int flip_count = 0;

	for(unsigned int i = 0; i < S.length() - K + 1; i++)
	{
		if(S[i] == '-')
		{
			for(unsigned int j = i; j < i + K; j++)
			{
				S[j] = (S[j] == '-') ? '+' : '-';
			}
			flip_count++;
		
			// INFO
			if(_DBG_LOG_ == 1)
			{
				for(unsigned int k = 0; k < i; k++)
				{
					cout << " ";
				}

				for(unsigned int k = 0; k < K; k++)
				{
					cout << ".";
				}
				cout << endl;
				cout << S << " After FLIP " << flip_count << endl;
			}
		}
	}
	
	int possible = 1;
	for(unsigned int i = 0; i < S.length(); i++)
	{
		if(S[i] == '-')
		{
			possible = 0;
			break;
		}
	}

	if(possible == 1)
	{
		return flip_count;
	}
	else
	{
		return -1;
	}
}

