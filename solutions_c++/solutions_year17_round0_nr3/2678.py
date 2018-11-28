#include<iostream>
#include<set>
#include<map>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

map<ll,ll> cnt;
set<pll> pq;

int main()
{
	int TM;
	cin >> TM;
	for (int T=1; T<=TM; T++) {
		cout << "Case #" << T << ": ";

		ll K,N;
		cin >> N >> K;
		
		pq.clear();
		cnt.clear();

		pq.insert(pll(N,1));
		cnt[N] = 1;

		ll done=0,last_a=0,last_b=0;
		while (done < K) {
			pll top = *(pq.rbegin());
			//cout << "Moving " << top.first << ", " << top.second << " times\n";
			pq.erase(top);
			cnt.erase(top.first);
			
			ll a = top.first/2;
			if (cnt.count(a) == 0) {
				cnt[a] = top.second;
				pq.insert(pll(a,cnt[a]));
			} else {
				pq.erase(pll(a,cnt[a]));
				cnt[a] += top.second;
				pq.insert(pll(a,cnt[a]));
			}

			a  = (top.first-1)/2;
			if (cnt.count(a) == 0) {
				cnt[a] = top.second;
				pq.insert(pll(a,cnt[a]));
			} else {
				pq.erase(pll(a,cnt[a]));
				cnt[a] += top.second;
				pq.insert(pll(a,cnt[a]));
			}

			done += top.second;
			last_a = top.first/2;
			last_b = (top.first-1)/2;
		}

		cout << last_a << " " << last_b << "\n";
	}
}
