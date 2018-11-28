#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <hash_map>
#include <hash_set>
#include <unordered_map>
#include <unordered_set>
#include <string.h>
#include <queue>
#include <list>
#include <iomanip>
#include <string>

using namespace std;

#define ll long long

ll N, K;


void CoutLeftRight(ofstream& fout,ll slot)
{
	if (slot % 2 == 0)
	{
		ll k = slot / 2;
		fout << k << " " << k - 1;
	}
	else
	{
		ll k = slot / 2;
		fout << k << " " << k;
	}
}

void SingleProcess(ofstream& fout)
{
	ll level = 1;
	ll left = N;
	ll alreadyPut = 0;
	while (alreadyPut<K-level)
	{
		alreadyPut += level;
		level *= 2;
	}
	left = N - alreadyPut;
	ll smallSlot = left / level;
	ll bigSlot = smallSlot + 1;
	ll bigSlotNumber = left - level*smallSlot;
	ll smallSlotNumber = level - bigSlotNumber;

	if (K-alreadyPut > bigSlotNumber)
	{
		CoutLeftRight(fout, smallSlot);
	}
	else
	{
		CoutLeftRight(fout, bigSlot);
	}
}


int main()
{
	FILE* fp = freopen("in.txt", "r", stdin);
	ofstream fout("out.txt");
	int Cases = 0;
	scanf("%d", &Cases);
	for (int time = 0; time < Cases; time++)
	{
		cin >> N >> K;

		fout << "Case #" << (time + 1) << ": ";
		SingleProcess(fout);
		fout << endl;
		std::cout << time << endl;
	}
	fclose(fp);
	fout.close();

	return 0;

}