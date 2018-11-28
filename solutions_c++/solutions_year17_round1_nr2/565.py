#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int notValid(int serves, int need, int have)
{
	int target = need * serves;
	int lower = target * 0.9;
	if(target % 10)
	{
		lower++;
	}
	int upper = target * 1.1;

	if(have < lower)
	{
		cerr << "Failed (-1): " << have << ", " << upper << endl;
		return -1;
	}
	if(have > upper)
	{
		cerr << "Failed ( 1): " << have << ", " << upper << endl;
		return 1;
	}

	return 0;
}


int main()
{
	int count;
	cin >> count;
	for(int i=1; i<=count; i++)
	{
		int answer = 0;
		int num, packs;
		cin >> num >> packs;

		vector<int> needs(num);
		for(int i=0; i<num; i++)
		{
			cin >> needs[i];
		}
		vector<vector<int>> amt(num, vector<int>(packs, 0));
		for(int i=0; i<num; i++)
		{
			for(int j=0; j<packs; j++)
			{
				cin >> amt[i][j];
			}
			sort(amt[i].begin(), amt[i].end());
		}


		vector<int> at(num, 0);
		while(at[0] < packs)
		{
			int goal = (amt[0][at[0]] * 0.9) / needs[0];
			cerr << "Starting at location " << at[0] << " of size: " << amt[0][at[0]] << " with a goal of: " << goal << endl;

			while(notValid(goal, needs[0], amt[0][at[0]]) > 0)
			{
				goal++;
				cerr << "Adjusted goal to: " << goal << " Returned: " << notValid(goal-1, needs[0], amt[0][at[0]]) << endl;
			}
reconsider:
			if(notValid(goal, needs[0], amt[0][at[0]]) != 0)
			{
				at[0]++;
				cerr << "Failed to match goal" << endl;
				continue;
			}

			bool failed = false;
			for(int i=1; (i<num) && !failed; i++)
			{
				while((at[i] < packs) && (notValid(goal, needs[i], amt[i][at[i]]) < 0))
				{
					at[i]++;
				}
				if(at[i] >= packs)
				{
					cerr << "Item: " << i << " failed goal by out of bounds" << endl;
					failed = true;
				}
				if(notValid(goal, needs[i], amt[i][at[i]]) > 0)
				{
					cerr << "Item: " << i << " failed goal: " << amt[i][at[i]] << endl;
					failed = true;
				}
			}

			if(failed)
			{
				goal++;
				goto reconsider;
//				at[0]++;
//				continue;
			}
			else
			{
				cerr << "Goal matched! ";
				answer++;
				for(int i=0; i<num; i++)
				{
					cerr << amt[i][at[i]] << " ";
					at[i]++;
				}
				cerr << endl;
			}

		}


		cout << "Case #" << i << ": " << answer << endl;
	}
	return 0;
}
