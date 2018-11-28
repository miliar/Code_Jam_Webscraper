#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <memory>
#include <map>

using namespace std;

typedef long long int ll;

struct segment_node {
	ll S_L, S_R;
	ll cnt;
};

const int MAXSIZE = 100;
const int INF = 2000*1000*1000;

std::shared_ptr<segment_node> split_segment(ll size) {
	std::shared_ptr<segment_node> node(new segment_node);
	node->cnt = 1;
	if (size%2 == 1) {
		node->S_L = size/2 + 1;
		node->S_R = size/2 + 1;
	} else {
		node->S_L = size/2;
		node->S_R = size/2 + 1;
	}
	return node;	
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie();

	int T;
	cin >> T;
	for(int t=1; t<=T; ++t) {
		ll n, k;
		cin >> n >> k;

		queue< std::shared_ptr<segment_node> > q;
		map< pair<ll,ll>, std::shared_ptr<segment_node> > m;
		
		//first node init
		std::shared_ptr<segment_node> first_node = split_segment(n);

		//push first node
		m.insert(make_pair(make_pair(first_node->S_L, first_node->S_R), first_node));
		q.push(first_node);

		std::shared_ptr<segment_node> node = q.front();
		ll sum = node->cnt;
		while (sum < k) {
			q.pop();

			auto node_r = split_segment(node->S_R - 1);
			node_r->cnt = node->cnt;
			auto seg_it_r = m.find(make_pair(node_r->S_L, node_r->S_R));
			if (seg_it_r != m.end()) {
				auto seg_ptr = seg_it_r->second;
				seg_ptr->cnt += node_r->cnt;
			} else {
				m.insert(make_pair(make_pair(node_r->S_L, node_r->S_R), node_r));
				q.push(node_r);
			}

			auto node_l = split_segment(node->S_L - 1);
			node_l->cnt = node->cnt;
			auto seg_it_l = m.find(make_pair(node_l->S_L, node_l->S_R));
			if (seg_it_l != m.end()) {
				auto seg_ptr = seg_it_l->second;
				seg_ptr->cnt += node_l->cnt;
			} else {
				m.insert(make_pair(make_pair(node_l->S_L, node_l->S_R), node_l));
				q.push(node_l);
			}

			node = q.front();
			sum += node->cnt;
		}

		cout << "Case #" << t << ": " << max(node->S_L, node->S_R)-1 << " " << min(node->S_L, node->S_R)-1;
		if (t != T) cout << endl;
	}

	return 0;
}