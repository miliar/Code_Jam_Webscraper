#include <bits/stdc++.h>
using namespace std;

bool czy[7];
string kol = "#ROYGBV";

int n;
int ile_licz[7];

vector <int> obok[7];

string solve()
{
	for(int i = 1 ; i <= 6 ; i++)
		czy[i] = false;
	vector < pair <int, int> > V;
	for(int i = 1 ; i <= 6 ; i++)
		V.push_back({ile_licz[i], i});
	string ret;
	vector <int> retid;
	
	random_shuffle(V.begin(), V.end()); // moze nie
	for(int x = 1 ; x <= n ; x++)
	{
		if(x == n)
		{
			for(auto a : obok[retid[0]])
				czy[a] = true;
		}
		int id = 5;
		while(id >= 0 && czy[V[id].second] == true)
			id--;
		if(id == -1)
			return "IMPOSSIBLE";
		V[id].first--;
		if(V[id].first < 0)
			return "IMPOSSIBLE";
		ret.push_back(kol[V[id].second]);
		retid.push_back(V[id].second);
		for(int i = 1 ; i <= 6 ; i++)
			czy[i] = false;
		for(auto a : obok[V[id].second])
			czy[a] = true;
		sort(V.begin(), V.end());
	}
	
	return ret;
}

int main()
{
	srand(1234);
	
	obok[1] = {6,1,2};
	obok[2] = {1,2,3};
	obok[3] = {2,3,4};
	obok[4] = {3,4,5};
	obok[5] = {4,5,6};
	obok[6] = {5,6,1};

	int t;
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
	{
		string ret;
		scanf("%d", &n);
		for(int x = 1 ; x <= 6 ; x++)
			scanf("%d", &ile_licz[x]);
		for(int x = 1 ; x <= 5000 ; x++)
		{
			ret = solve();
			if(ret != "IMPOSSIBLE")
				break;
		}
		cout << "Case #" << i << ": " << ret << "\n";
	}
}
