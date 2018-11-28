#include <fstream>
#include <iostream>
#include <string>
#include <functional>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

string fname = "c";

bool Compare(pair<ll,ll> a, pair<ll,ll> b)
{
	if (b.second-b.first > a.second-a.first)
		return true;
	if (b.second-b.first < a.second-a.first)
		return false;
	return a.first > b.first;
}

int main()
{
	string ifname = fname + ".in";
	string ofname = fname + ".out";
	ifstream f;
	ofstream of;
	of.open(ofname);
	f.open(ifname);
	int t;
	f >> t;
	for (int tt=0;tt<t;++tt){
		ll n, k;
		f >> n >> k;
		vector<bool> v(n,0);

		priority_queue<pair<ll,ll>, std::vector<pair<ll,ll>>, decltype(&Compare)> pq(&Compare);
		pq.push({0,n-1});
		ll mid;
		for (int i=0;i<k;++i)
		{
			auto p = pq.top();
			pq.pop();
			mid = p.first + (p.second-p.first)/2;
			v[mid] = 1;
			pq.push({p.first, mid - 1});
			pq.push({mid+1,p.second});
		}
		ll l = 0, r = 0, cur = mid - 1;
		while (cur >= 0 && v[cur] == 0)
		{
			++l;
			--cur;
		}
		cur = mid + 1;
		while (cur < n && v[cur] == 0)
		{
			++r;
			++cur;
		}
		of << "Case #" << tt+1 << ": " << max(l,r) << " " << min(l,r);
		of << "\n";
	}

	f.close();
	of.close();
}