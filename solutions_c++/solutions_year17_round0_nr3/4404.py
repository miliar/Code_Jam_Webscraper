// C.cpp : Defines the entry point for the console application.
//
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;


int main(int argc, char* argv[])
{
	fstream In("c-small2.in", ios::in);
	fstream Out("c-small2.out", ios::out);

	int cases;
	In >> cases;

	for (int h = 0; h < cases; h++)
	{
		int N, K;

		In >> N >> K;

		int Ls, Rs;
		priority_queue<int> queue;
		//vector<int> queue;
		queue.push(N);
		//queue.push_back(N);

		for (int i = 0; i < K; i++)
		{
			int roomSize = queue.top();
				//[queue.size() - 1];
			queue.pop();

			Ls = (roomSize - 1) / 2;
			Rs = (roomSize - 1) - Ls;

			if (Ls > 0)
				queue.push(Ls);
			if (Rs > 0)
				queue.push(Rs);

		}

		Out << "Case #" << h + 1 << ": " << max(Rs, Ls) << " " << min(Rs, Ls) << endl;
	}

	In.close();
	Out.close();

	return 0;
}

