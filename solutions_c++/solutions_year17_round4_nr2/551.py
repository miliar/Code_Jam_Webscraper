#include <bits/stdc++.h>
using namespace std;

void test() {
	int n, c, m;
	cin >> n >> c >> m;
	
	vector<vector<int>> tickets(c+1);  // [buyer] = { slot, slot, }
	
	int max_tickets = 0;
	for (int i = 0; i <m; ++i) {
		int p, b;
		cin >> p >> b;
		tickets[b].push_back(p);
		max_tickets=max<int>(max_tickets, tickets[b].size());
	}
	
	for (int rno = max_tickets; rno <= m; ++rno) {
		//cerr << "rno = " << rno << endl;
		int promos = 0;
		
		/*set<int> all_slots_free;
		for (int s = 1; s<=n; ++s)
			all_slots_free.insert(s);*/
		
		vector<pair<int /* last occ*/, set<int /*buyers*/>>> rides(rno, {99999, {}});
		
		priority_queue<pair<int /* pos*/, int /* buyer (- if already promoted)*/>> pq;		
		for (int b = 1; b <=c; ++b)
			for (int p : tickets[b])
				pq.push({p, b});
				
		while (!pq.empty()) {
			auto pa = pq.top();
			pq.pop();
			int pos = pa.first;
			if (pos == 0) {
				promos = -1;
				break;
			}
			int buy = abs(pa.second);
			//cerr << "pos = " << pos << ", buy = " << pa.second << endl;
			
			bool used = false;
			for(int r = 0; r < rno; ++r) {
				//cerr << "r = " << r << ", cb = " << rides[r].second.count(buy) << ", lo=" << rides[r].first <<  endl;
				//if (rides[r].second.count(buy)) continue;
				if (rides[r].first <= pos) continue;
				
				rides[r].first = pos;
				//rides[r].second.insert(buy);
				
				used = true;
				break;
			}
			
			if (!used) {
				if (buy == pa.second) {
					promos++;
				}
				pq.push({(pos-1), -buy});
			}
		}
		
		if (promos >= 0) {
			cout << rno << " " << promos;
			break;
		}
		
		//cerr << "Promos: " << promos << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		test();
		cout << endl;
	}
	return 0;
}
