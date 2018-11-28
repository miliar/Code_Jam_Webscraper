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

ll N;


void SingleProcess(ofstream& fout)
{
	vector<ll> digits;
	ll temp = N;
	while (temp > 0)
	{
		digits.push_back(temp % 10);
		temp = temp / 10;
	}

	for (int i = 1; i < digits.size(); i++)
	{
		if (digits[i]>digits[i - 1])
		{
			digits[i]--;
			for (int j = i - 1; j >= 0; j--)
			{
				digits[j] = 9;
			}
		}
	}

	ll ret = 0;
	ll wei = 1;
	for (int i = 0; i < digits.size(); i++)
	{
		ret += wei*digits[i];
		wei *= 10;
	}

	fout << ret;

}


int main()
{
	FILE* fp = freopen("in.txt", "r", stdin);
	ofstream fout("out.txt");
	int Cases = 0;
	scanf("%d", &Cases);
	for (int time = 0; time < Cases; time++)
	{
		cin >> N;

		fout << "Case #" << (time + 1) << ": ";
		SingleProcess(fout);
		fout << endl;
		std::cout << time << endl;
	}
	fclose(fp);
	fout.close();

	return 0;

}