#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string.h>
#include <queue>
#include <list>
#include <iomanip>
#include <string>

using namespace std;

#define ll long long

ll MODE = 1000000007;

struct Horse
{
	ll pos;
	ll speed;
	double time;

};

vector<Horse> horseVec;
ll D, N;
void SingleProcess(ofstream& fout)
{
	float maxTime = -1;
	for (int i = 0; i < horseVec.size(); i++)
	{
		horseVec[i].time = ((double)(D - horseVec[i].pos)) / horseVec[i].speed;
		if (maxTime < horseVec[i].time)
		{
			maxTime = horseVec[i].time;
		}
	}
	fout << setiosflags(ios::fixed)<<setprecision(10)<<((double)D) / maxTime;
}


int main()
{
	FILE* fp = freopen("in.txt", "r", stdin);
	ofstream fout("out.txt");
	int Cases = 0;
	scanf("%d", &Cases);
	for (int time = 0; time < Cases; time++)
	{
		horseVec.clear();
		cin >> D >> N;
		for (int i = 0; i < N; i++)
		{
			Horse h;
			cin >> h.pos >> h.speed;
			horseVec.push_back(h);
		}
		fout << "Case #" << (time + 1) << ": ";
		SingleProcess(fout);
		fout << endl;
		std::cout << time << endl;
	}
	fclose(fp);
	fout.close();

	return 0;

}