#include <iostream>
#include <set>
#include <functional>
#include <unordered_map>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int N = 1; N <= T; N++)
	{
		__int64 n, k;
		cin >> n >> k;
		vector<__int64> pp;
		unordered_map<__int64,__int64> lib;
		lib.insert(pair<__int64, __int64>(n, 1));
		pp.push_back(n);
		__int64 lr, rr;

		for (int i = 0; i < pp.size();i++)
		{
			if (pp[i] % 2 == 0)
			{
				rr = pp[i] / 2;
				lr = pp[i] - rr - 1;
				if (rr < 0 || lr < 0) continue;
				if (lib.find(rr) == lib.end())
				{
					pp.push_back(rr);
					lib.insert(pair<__int64, __int64>(rr, lib[pp[i]]));
				}
				else
				{
					lib[rr] += lib[pp[i]];
				}

				if (lib.find(lr) == lib.end())
				{
					pp.push_back(lr);
					lib.insert(pair<__int64, __int64>(lr, lib[pp[i]]));
				}
				else
				{
					lib[lr] += lib[pp[i]];
				}
				
			}
			else
			{
				lr = rr = pp[i] / 2;
				if (lib.find(lr) == lib.end())
				{
					pp.push_back(lr);
					lib.insert(pair<__int64, __int64>(lr, lib[pp[i]]*2));
				}
				else
				{
					lib[lr] += lib[pp[i]]*2;
				}
			}
			
		} 
		__int64 sum = 0;
		for (int i = 0; i < pp.size(); i++) sum = lib[pp[i]];
		for (int i = 0; k != 0;i++)
		{
			k = max(k - lib[pp[i]], (__int64)0);
			if (k == 0)
			{
				if (pp[i] % 2 == 0)
					rr = pp[i] / 2, lr = pp[i] - rr - 1;
				else
					lr = rr = pp[i] / 2;
			}
		}
		cout << "Case #" << N << ": " << max(lr,rr) << " " << min(lr,rr) << endl;
	}
	return 0;
}