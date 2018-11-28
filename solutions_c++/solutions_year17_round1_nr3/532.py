#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

map<pair<pair<int, int>, pair<int, int> >, bool> mark;


int solve(int _hd, int _ad, int _hk, int _ak, int b, int d){
	vector<int> hd(1, _hd);
	vector<int> ad(1, _ad);
	vector<int> hk(1, _hk);
	vector<int> ak(1, _ak);

	vector<int> step(1, 1);
	mark.clear();
	for (int i = 0; i < step.size(); ++i)
	{
		//cerr << i << endl;
		if(hk[i] <= 0)
			return step[i] - 1;
		if(hd[i] <= 0)
			continue;
		if(mark[make_pair(make_pair(hd[i],ad[i]), make_pair(hk[i],ak[i]))])
			continue;
		mark[make_pair(make_pair(hd[i],ad[i]), make_pair(hk[i],ak[i]))] = true;
		// attack
		hd.push_back(hd[i] - ak[i]);
		ad.push_back(ad[i]);
		hk.push_back(max(0, hk[i] - ad[i]));
		ak.push_back(ak[i]);
		step.push_back(step[i] + 1);

		// Buff
		if (b != 0) {
		hd.push_back(hd[i] - ak[i]);
		ad.push_back(ad[i] + b);
		hk.push_back(max(0, hk[i] - 0));
		ak.push_back(ak[i]);
		step.push_back(step[i] + 1);
}
		// Cure
	
		hd.push_back(_hd - ak[i]);
		ad.push_back(ad[i]);
		hk.push_back(max(0, hk[i] - 0));
		ak.push_back(ak[i]);
		step.push_back(step[i] + 1);
	
		//Debuff
		if (d != 0) {
		hd.push_back(hd[i] - max(0, ak[i] - d));
		ad.push_back(ad[i]);
		hk.push_back(max(0, hk[i] - 0));
		ak.push_back(max(0, ak[i] - d));
		step.push_back(step[i] + 1);
	}
}
	

	return 0;
}


int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		int result = solve(hd, ad, hk, ak, b, d);
		cout << "Case #" << test+1 << ": ";
		if (result)
			cout << result << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
}