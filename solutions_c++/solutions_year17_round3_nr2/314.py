#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		int NA, NB;
		cin >> NA >> NB;
		
		vector <pair<pair<int,int> , int> > activities;
		
		for (int i=0; i<NA; i++) {
			int start, end;
			cin >> start >> end;
			activities.push_back({{start, end}, 0});
		}
		for (int i=0; i<NB; i++) {
			int start, end;
			cin >> start >> end;
			activities.push_back({{start, end}, 1});
		}
		
		const int day_lenght = 24*60;
		
		sort(activities.begin(), activities.end());
		
		vector <int> time_used = {0, 0};
		int zero_cost_time = 0;
		int changes = 0;
		vector <vector <int> > intra_time(2);
		
		int N = activities.size();
		for (int i=0; i<N; i++) {
			int next = (i+1)%N;
			pair<pair<int,int> , int> x = activities[i];
			pair<pair<int,int> , int> y = activities[next];
			int lenght = x.first.second - x.first.first;
			int who = x.second;
			time_used[who] += lenght;
			
			int free_time = y.first.first - x.first.second;
			if (free_time < 0) free_time += day_lenght;
			
			if (x.second != y.second) {
				zero_cost_time += free_time;
				changes++;
			}
			else {
				intra_time[who].push_back(free_time);
			}
		}
		
		for (int j=0; j<2; j++) {
			vector <int> & intra = intra_time[j];
			sort(intra.rbegin(), intra.rend());
			while (intra.size() > 0 && time_used[j] + intra.back() <= day_lenght/2) {
				time_used[j] += intra.back();
				intra.pop_back();
			}
			changes += 2*(int)intra.size();
		}
		
		cout<<"Case #"<<test<<": " << changes << "\n";
	}
	return 0;
}
