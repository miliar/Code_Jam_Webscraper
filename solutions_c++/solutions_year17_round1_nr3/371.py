#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

struct State
{
	int HD;
	int AD;
	int HK;
	int AK;

	bool operator<(const State &other) const
	{
		if (HD < other.HD)
			return true;
		else if (HD > other.HD)
			return false;
		if (AD < other.AD)
			return true;
		else if (AD > other.AD)
			return false;
		if (HK < other.HK)
			return true;
		else if (HK > other.HK)
			return false;
		return AK < other.AK;
	}
};

void doCase()
{
	int B, D;
	State start;
	cin >> start.HD >> start.AD >> start.HK >> start.AK >> B >> D;
	int initialHD = start.HD;
	set<State> old;
	set<State> states;
	states.insert(start);
	for (int iter = 1; iter < 2000; iter++)
	{
		old.insert(states.begin(), states.end());
		set<State> newstates;
		for (set<State>::iterator it = states.begin(); it != states.end(); ++it)
		{
			//cout << "Iter " << iter << " " << it->HK << " " << it->AK << endl;
			// attack
			{
				if (it->AD >= it->HK)
				{
					cout << iter << endl;
					return;
				}
				State newstate = *it;
				newstate.HK -= it->AD;
				newstate.HD -= it->AK;
				int copies = old.count(newstate);
				if (newstate.HD > 0 && !old.count(newstate))
					newstates.insert(newstate);
			}
			// heal
			if (it->HD < initialHD)
			{
				State newstate = *it;
				newstate.HD = initialHD - it->AK;
				if (newstate.HD > 0 && !old.count(newstate))
					newstates.insert(newstate);
			}
			// buff
			{
				State newstate = *it;
				newstate.AD += B;
				newstate.HD -= it->AK;
				if (newstate.HD > 0 && !old.count(newstate))
					newstates.insert(newstate);
			}
			// debuff
			{
				State newstate = *it;
				newstate.AK -= D;
				if (newstate.AK < 0)
					newstate.AK = 0;
				newstate.HD -= newstate.AK;
				if (newstate.HD > 0 && !old.count(newstate))
					newstates.insert(newstate);
			}
		}
		states = newstates;
	}
	cout << "IMPOSSIBLE" << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		doCase();
	}
}