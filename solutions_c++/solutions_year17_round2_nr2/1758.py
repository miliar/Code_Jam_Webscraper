// Google2017-R1B-B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef long long int64;


int64 n, r, o, y, g, b, v;


int main()
{
	ifstream input;
	ofstream output;
	input.open("B-small-attempt4.in", std::ios_base::in);
	output.open("B-small.txt");

	int T;
	input >> T;
	for (int t = 0; t < T; t++)
	{
		input >> n >> r >> o >> y >> g >> b >> v;

		string S = "";

		char let[3]{ 'R', 'Y', 'B' };
		int  var[3];
		var[0] = r;
		var[1] = y;
		var[2] = b;

		bool P = true;
		for (int i = 0; i < n && P; i++)
		{
			char c;
			if (i == 0)
				c = 'X';
			else
				c = S[i - 1];
			int maxx = 0;
			int j0 = 0;

			for (int j = 0; j < 3; j++)
			{

				if (let[j] != c)
				{
					if (var[j] > maxx)
					{
						maxx = var[j];
						j0 = j;
					}					
				}
			}

			if (maxx == 0)
				P = false;
			else
			{
				var[j0]--;
				S += let[j0];
			}

		}
		if (P)
		{
			// check whether we have problems in the end

			if (S[0] == S[n - 1])
			{
				bool G = false;

				if (S[0] != S[2])
				{
					G = true;
					swap(S[0], S[1]);
				}

				if (G == false)
				for (int i = 2; i < n - 1; i++)
				{
					if (S[i] == S[0])
						continue;
					if (S[i] != S[1] && S[0] != S[i - 1] && S[0] != S[i + 1])
					{
						G = true;
						swap(S[i], S[0]);
						break;
					}
				}

				if (G==false)
				if (S[n-1]!=S[n-3])
				{
					G = true;
					swap(S[n - 1], S[n - 2]);

				}

				if (G == false)
				for (int i = 2; i < n - 1; i++)
				{
					if (S[i] == S[0])
						continue;
					if (S[i] != S[n-2] && S[n-1] != S[i - 1] && S[n-1] != S[i + 1])
					{
						G = true;
						swap(S[i], S[0]);
						break;
					}
				}

				if (!G)
					P = false;
			}
		}


		if (P == false)
			S = "IMPOSSIBLE";


		output << "Case #" << t + 1 << ": " << S << "\n";

	}
	input.close();
	output.close();

	return 0;
}






