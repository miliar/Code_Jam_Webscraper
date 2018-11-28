#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#define maxn 300 
#define maxl 1000000000

using namespace std;

void solve()
{
	long long n, k;
	cin >> n >> k;
	map<long long, long long> mm;
	mm[n] = 1;
	while(true)
	{
		map<long long, long long>::iterator it = mm.end();
		--it;
		pair<long long, long long> tmp = *it;
		mm.erase(it);
		if(tmp.second >= k) 
		{
			cout << tmp.first / 2 << " " << (tmp.first-1) / 2 << endl;
			break;
		}
		k -= tmp.second;
		mm[tmp.first / 2] += tmp.second;
		mm[(tmp.first-1) / 2] += tmp.second;
	}

}

int main(){
	int t;
	ios::sync_with_stdio(false);
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

