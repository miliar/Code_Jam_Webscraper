#include <vector>
#include <iostream>
#include <string>
#include <functional>
#include <algorithm>


using namespace std;

int vira(string p, int pos, int k){
	bool did = 1;
	string q = p;


	for (int i = pos; i < pos + k; i++)
	{
		if (p[i] == '+')
			p[i] = '-';
		else
			p[i] = '+';
	}
	for (int i = 0; i < p.size(); i++)
		if (p[i] != '+')
		{
			did = 0;
			break;
		}
	if (did == 0)
	{
		if (pos + k == p.size())
			return 999999;
		else
			return min(vira(p, pos + 1, k) + 1, vira(q, pos + 1, k));
	}
	else
		return 1;
}

int main(){
	int t;
	vector<string> ans;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		string p;
		int k;
		int n;
		bool ok = 1;
		cin >> p >> k;
		for (int i = 0; i < p.size(); i++)
			if (p[i] == '-')
				ok = 0;
		if (ok == 1)
		{
			ans.push_back("0");
			continue;
		}
		n = vira(p, 0, k);
		if (n < 999999)
			ans.push_back(to_string(n));
		else
			ans.push_back("IMPOSSIBLE");



	}
	for (int i = 0; i < ans.size(); i++)
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	
	
	
	
	
	
	return 0;
}