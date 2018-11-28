#include <iostream>
#include <functional>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

#define debug cout

#define ll long long int

#define fori(n) for(int i = 0; i < n; i++)
#define forj(n) for(int j = 0; j < n; j++)
#define fork(n) for(int k = 0; k < n; k++)

#define forri(n) for(int i = n - 1; i >= 0; i--)
#define forrj(n) for(int j = n - 1; j >= 0; j--)
#define forrk(n) for(int k = n - 1; k >= 0; k--)
	
#define fori2(s,n) for(int i = s; i < n; i++)
#define forj2(s,n) for(int j = s; j < n; j++)
#define fork2(s,n) for(int k = s; k < n; k++)

#define forit(v) for(auto it = v.begin(); it != v.end(); it++)
#define forrit(v) for(auto it = v.rbegin(); it != v.rend(); it++)


ll N;
ll K;

int V[10000];

std::map<ll, int> m;
std::map<ll, int> save;

bool contains(ll x) {
	return m.find(x) != m.end();
}

void RunInstance()
{
	cin >> N >> K;
	ll bound = 2;

	save.clear();
	save[N] = 1;
	while (bound - 1 < K) {
		m.clear();

		forit(save) {
			ll first = it->first / 2;
			ll second = (it->first - 1) / 2;
			ll count = it->second;

			if (!contains(first))
				m[first] = 0;
			if (!contains(second))
				m[second] = 0;

			m[first] += it->second;
			m[second] += it->second;
		}

		save = m;
		bound *= 2;
	}

	ll pos = K - (bound + 1)/2;

	ll counter = 0;
	forrit(save) {
		counter += it->second;
		if (counter > pos) {
			cout << (it->first / 2) << " " << ((it->first - 1) / 2);
			return;
		}
	}

}	






// ======================================================== //

int main()
{
	int num_of_instances = 0;
	cin >> num_of_instances;

	for (int i = 1; i <= num_of_instances; ++i)
	{
		cout << "Case #" << i << ": ";
		RunInstance();
		cout << endl;
	}
}

