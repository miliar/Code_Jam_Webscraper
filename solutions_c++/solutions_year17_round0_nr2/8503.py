#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <ctime>

// #include <cstdio>
//#include <sstream>

using namespace std;

#define TASK "task2"

void printvec(vector<int> v)
{
	if (v[0]!=0)
		cout << v[0];
	for (int j = 1; j < v.size(); j++)
	{
		cout << v[j];
	}
	cout << endl;
}

int main()
{
//	clock_t begin = clock();

	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	ios_base::sync_with_stdio(false);

	int t; // kolvo_testovih_zadac;
	vector<int> vec_base;
	vector <vector <int> > vec_end;
	vector<int> vec_start;
	long long intA;
	string strA;
	char chA;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		vec_base.clear();
		vec_start.clear();
		cin >> strA;
		for (int j = 0; j < strA.size(); j++)
		{
			chA = strA[j];
			intA = atoi(&chA);
			vec_base.push_back(intA);
		}
	    vec_start = vec_base;
		bool state;
		state = false;
	    while (state == false)
	    {
			state = true;
		    for (int j = 0; j < vec_start.size() - 1; j++)
		    {
			  if (vec_start[j] > vec_start[j + 1])
			  {
				 vec_start[j] = vec_start[j] - 1;
				 for (int q = j + 1; q < vec_start.size(); q++) // vse starshie elementi posle j-ного ustanavlivaem v 9
					 vec_start[q] = 9;
				 state = false;  // ostaemsya v zikle while
				 j = vec_start.size(); // vihodim iz zikla for
			  } 
		    }
	    }
		cout << "Case #" << i + 1 << ": ";
		printvec(vec_start);
	}


//	clock_t end = clock();
//	long elapsed_secs = end - begin;
//	cout << "time" << elapsed_secs; 
}