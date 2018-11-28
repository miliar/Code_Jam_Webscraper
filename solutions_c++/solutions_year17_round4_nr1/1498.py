#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
#define f(i,x,y) for(int i = x; i < y; ++ i)
typedef long long ll;

vector< vector<int> > getPieces(int P)
{
	vector< vector<int> > ans;

	if (P == 2)
	{
		ans.push_back( {2} );
	}
	else if (P == 3)
	{
		ans.push_back( {1 ,1} );
		ans.push_back( {3, 0} );
		ans.push_back( {0, 3} );
	}
	else if (P == 4)
	{
		ans.push_back( {1, 0, 1} );
		ans.push_back( {0, 2, 0} );
		ans.push_back( {0, 1, 2} );
		ans.push_back( {2, 1, 0} );
		ans.push_back( {0, 0, 4} );
		ans.push_back( {4, 0, 0} );
	}
	return ans;
}

vector<int> getMoney(const vector<int>& iGroups, int P)
{
	vector<int> money(P, 0);
	for (auto group : iGroups)
		++ money[ group % P ];

	return vector<int>(money.begin() + 1, money.end());
}

int memo[105][105][105], P;

int dp(const vector<int> &money, const vector< vector<int> >& iPieces)
{
	int &res = P==2? 
				memo[0][0][money[0]] :
				P==3? 
					memo[0][money[0]][money[1]] :
					memo[money[0]][money[1]][money[2]];
	if (~res) return res;
	res = 0;
	for (int i = 0; i < money.size(); ++ i) if (money[i])
		res = 1;

	for (const auto &piece : iPieces)
	{
		bool valid = true;
		auto aMoney = money;
		for (int i = 0; i < money.size(); ++ i)
		{
			aMoney[i] -= piece[i];
			if (aMoney[i] < 0) valid = false;
		}
		if (valid)
			res = max(res, 1 + dp(aMoney, iPieces));
	}
	return res;
}


int main()
{
	int number_of_testcases;
	cin >> number_of_testcases;
	for (int testcase = 1; testcase <= number_of_testcases; ++ testcase)
	{
		int n, p; cin >> n >> p;
		vector<int> groups(n);
		int zeros = 0;
		for (auto& group : groups)
		{
			cin >> group;
			if (group % p == 0) ++ zeros;
		}

		auto money = getMoney(groups, p);
		auto pieces = getPieces(p);
		memset(memo, -1, sizeof(memo));

		P = p;
		cout << "Case #" << testcase << ": ";
		cout << dp(money, pieces) + zeros << endl;
	}
}

