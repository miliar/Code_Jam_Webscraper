#include <iostream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (size_t i = 0; i < T; ++i)
	{
		size_t N, R, O, Y, G, B, V;
		in >> N >> R >> O >> Y >> G >> B >> V;

		bool possible = ((R > G || G == 0) && (B > O || O==0) && (Y > V||V==0));
		string order;
		if (possible)
		{
			size_t R1 = R - G;
			size_t B1 = B - O;
			size_t Y1 = Y - V;

			possible = (2 * R1 <= R1 + B1 + Y1 && 2 * B1 <= R1 + B1 + Y1 && 2 * Y1 <= R1 + B1 + Y1);
			if (possible)
			{
				size_t pos = 0;
				size_t id;
				order.resize(R1 + B1 + Y1);

				int num[3] = { R1, B1, Y1 };
				char cha[3] = { 'R', 'B', 'Y' };

				if (num[0] < num[1])
					swap(num[0], num[1]), swap(cha[0], cha[1]);
				if (num[0] < num[2])
					swap(num[0], num[2]), swap(cha[0], cha[2]);
				if (num[1] < num[2])
					swap(num[1], num[2]), swap(cha[1], cha[2]);
				
				for (;num[0] > 0 && pos < order.size(); --num[0])
				{
					order[pos] = cha[0];
					pos += 2;
				}

				for (; num[1] > 0 && pos < order.size(); --num[1])
				{
					order[pos] = cha[1];
					pos += 2;
				}

				for (; num[2] > 0 && pos < order.size(); --num[2])
				{
					order[pos] = cha[2];
					pos += 2;
				}

				pos = 1;

				for (; num[0] > 0 && pos < order.size(); --num[0])
				{
					order[pos] = cha[0];
					pos += 2;
				}

				for (; num[1] > 0 && pos < order.size(); --num[1])
				{
					order[pos] = cha[1];
					pos += 2;
				}

				for (; num[2] > 0 && pos < order.size(); --num[2])
				{
					order[pos] = cha[2];
					pos += 2;
				}

				string insO(2 * O, 'B');
				for (size_t idd = 0; idd < O; ++idd)
					insO[1 + 2 * idd] = 'O';
				string insG(2 * G, 'R');
				for (size_t idd = 0; idd < G; ++idd)
					insG[1 + 2 * idd] = 'G';
				string insV(2 * V, 'Y');
				for (size_t idd = 0; idd < V; ++idd)
					insV[1 + 2 * idd] = 'V';

				if (O > 0)
					order.insert(order.find('B'), insO);
				if (G > 0)
					order.insert(order.find('R'), insG);
				if (V > 0)
					order.insert(order.find('Y'), insV);
			}
		}
		else if (R == G && R+G==N)
		{
			possible = true;
			order.resize(N);
			for (size_t idd = 0; idd < N; idd += 2)
				order[idd] = 'R', order[idd + 1] = 'G';
		}
		else if (B == O && B+O==N)
		{
			possible = true;
			order.resize(N);
			for (size_t idd = 0; idd < N; idd += 2)
				order[idd] = 'B', order[idd + 1] = 'O';
		}
		else if (Y == V && Y+V==N)
		{
			possible = true;
			order.resize(N);
			for (size_t idd = 0; idd < N; idd += 2)
				order[idd] = 'Y', order[idd + 1] = 'V';
		}


	    if (i > 0)
			out << endl;
		out << "Case #" << i+1 << ": " << (possible ? order : "IMPOSSIBLE");
	}

	in.close();
	out.close();
	return 0;
}