#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Activity
{
	int start;
	int end;
	int who;

	bool operator()(Activity a, Activity b)
	{
		if (a.start < b.start) return true;
		else return false;
	}
};

Activity act[201];
int cT = 720;
int jT = 720;
int cA, jA;
#define CAME	0
#define JAMI	1


void process(int tc)
{
	cT = jT = 720;
	cin >> cA >> jA;

	for (int i = 0; i < cA; i++){
		cin >> act[i].start >> act[i].end;
	}
	for (int i = cA; i < cA+jA; i++){
		cin >> act[i].start >> act[i].end;
	}
	for (int i = 0; i < cA; i++){
		cT -= (act[i].end - act[i].start);
		act[i].who = CAME;
	}
	for (int i = cA; i < cA+ jA; i++){
		jT -= (act[i].end - act[i].start);
		act[i].who = JAMI;
	}
	sort(act, act + cA + jA, Activity());

	int cnt = 0;
	vector<int> cJoint;
	vector<int> jJoint;
	for (int i = 0; i < cA + jA; i++)
	{
		int current = i;
		int next = i + 1;
		if (next >= cA + jA) next = 0;
		if (act[current].who != act[next].who) cnt++;
		else if (act[current].who == act[next].who && act[current].who == CAME)
		{
			int jointTime = act[next].start - act[current].end;
			if (jointTime < 0) jointTime += 1440;
			if (jointTime != 0)
			{
				cJoint.push_back(jointTime);
			}
			
		}
		else if (act[current].who == act[next].who && act[current].who == JAMI)
		{
			int jointTime = act[next].start - act[current].end;

			if (jointTime < 0) jointTime += 1440;
			if (jointTime != 0) jJoint.push_back(jointTime);
		}
	}
	sort(cJoint.begin(), cJoint.end());
	sort(jJoint.begin(), jJoint.end());

	int cRemain = 0;
	int jRemain = 0;
	for (int i = 0; i < cJoint.size(); i++)
	{
		if (cT>=cJoint[i])
			cT -= cJoint[i];
		else
		{
			cRemain = cJoint.size() - i;
			break;
		}
	}
	for (int i = 0; i < jJoint.size(); i++)
	{
		if (jT >= jJoint[i])
			jT -= jJoint[i];
		else
		{
			jRemain = jJoint.size() - i;
			break;
		}
	}
	cnt = cnt + (cRemain * 2) + (jRemain * 2);

	cout << "Case #" << tc << ": " << cnt << endl;

}

int main()
{
	int C;
	cin >> C;

	for (int i = 0; i < C; i++) process(i + 1);
	return 0;
}