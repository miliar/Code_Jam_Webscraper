#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>
#include <string>
#include <iomanip>
using namespace std;

vector<int> bye;

bool cmp(pair<int, int> p1, pair<int, int> p2){
	return (p1.second < p2.second);// || (p1.second == p2.second && bye[p1.first] < bye[p2.first]));
}

int main(){
	freopen("D:\\temp\\r2bl.in", "r", stdin);
	freopen("D:\\temp\\r2bl.txt", "w", stdout);
	int o1;
	cin>>o1;
	for (int t = 1; t <= o1; ++t){
		int n, m, c;
		cin>>n>>c>>m;
		bye.assign(c + 1, 0);
		vector<int> places_c(n + 1);
		vector<pair<int, int>> tickets(m);
		for (int i = 0; i < m; ++i){
			int b, p;
 			cin>>p>>b;
			++places_c[p];
			++bye[b];
			tickets[i].first = b;
			tickets[i].second = p;
		}
		sort(tickets.begin(), tickets.end(), cmp);
		int trips_r = m;
		int trips_l = places_c[1];
		for (int i = 1; i <= c; ++i){
			trips_l = max(trips_l, bye[i]);
		}
		--trips_l;
		int trips = (trips_l + trips_r + 1) / 2;
		while (trips != trips_r){
			int prev = 0;
			int s = 0;
			for (int i = 0; i < m; ++i){
				prev += (trips) * (tickets[i].second - s);
				s = tickets[i].second;
				--prev;
				if (prev < 0){
					trips_l = trips;
					break;
				}
			}
			if (trips != trips_l){
				trips_r = trips;
			}
			trips = (trips_l + trips_r + 1) / 2;
		}
		int moves = 0;
		for (int i = 2; i <= n; ++i){
			 moves += max(0, places_c[i] - trips);
		}
		cout<<"Case #"<<t<<": "<<trips<<" "<<moves<<'\n'; //setprecision(9)<<fixed<<
	}
}