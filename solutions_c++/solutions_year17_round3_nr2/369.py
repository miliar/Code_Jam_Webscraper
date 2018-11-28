#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

struct TupleCompare
{
	bool operator()(tuple<int, int, int> const& lhs, tuple<int, int, int> const& rhs) {
		return std::get<0>(lhs) < std::get<0>(rhs);
	}
};

int main()
{
    //ifstream fin("B-small-attempt0.in");
	ifstream fin("B-large.in");
	//ofstream fout("B-small-attempt0.out");
	ofstream fout("B-large.out");    
    int T;
    fin >> T;
      
    int C, J;
    for (int t = 1 ; t <= T; t++)
    { 
    	fin >> C >> J;
    	
    	vector<tuple<int, int, int> > act;
    	int temp_start, temp_end;
    	for (int i = 0 ; i < C ; i++) {
    		fin >> temp_start >> temp_end;
    		act.push_back(make_tuple(temp_start, temp_end, 0));
		}
		for (int i = 0 ; i < J ; i++) {
    		fin >> temp_start >> temp_end;
    		act.push_back(make_tuple(temp_start, temp_end, 1));
		}
    	
    	std::sort(act.begin(), act.end(), TupleCompare());
    	for (int i = 0 ; i < act.size(); i++) {
    		//cout << std::get<0>(act[i]) << ", " << std::get<1>(act[i]) << ", " << std::get<2>(act[i]) << endl;
		}
		
		vector<int> time;
		time.push_back(0);
		time.push_back(0);
		for (int i = 0 ; i < act.size(); i++) {
			if (i == act.size()-1) {
				if (std::get<2>(act[i]) == std::get<2>(act[0])) {
					time[std::get<2>(act[i])] += (std::get<0>(act[0]) + 1440) - std::get<0>(act[i]);
				} else {
					time[std::get<2>(act[i])] += std::get<1>(act[i]) - std::get<0>(act[i]);
				}
				continue;
			}
			
			if (std::get<2>(act[i]) == std::get<2>(act[i+1])) {
				time[std::get<2>(act[i])] += std::get<0>(act[i+1]) - std::get<0>(act[i]);
			} else {
				time[std::get<2>(act[i])] += std::get<1>(act[i]) - std::get<0>(act[i]);
			}
		}
		//cout << time[0] << " : " << time[1] << endl;
		
		
		int min_idx;
		if (time[0] < time[1]) {
			min_idx = 0;
		} else {
			min_idx = 1;
		}
		int min_time = time[min_idx];
	
		int ans = 0;
		for (int i = 0 ; i < act.size(); i++) {
			if (i == act.size()-1) {
				if (std::get<2>(act[i]) != std::get<2>(act[0])) {
					min_time += (std::get<0>(act[0]) + 1440) - std::get<1>(act[i]);
					ans++;
				}
				continue;
			}
			
			if (std::get<2>(act[i]) != std::get<2>(act[i+1])) {
				min_time += std::get<0>(act[i+1]) - std::get<1>(act[i]);
				ans++;
			}
		}	
		//cout << ans << " -- " << min_time << endl;
		bool add_bool[300];
		for (int i = 0 ; i < act.size() ; i++) {
			add_bool[i] = false;
		}
		while(min_time < 720) {
			int max_add = 0;
			int idx = 0;
			for (int i = 0 ; i < act.size(); i++) {
				if (add_bool[i]) continue;
				int temp_add = 0;
				if (i == act.size()-1) {
					if (std::get<2>(act[i]) == std::get<2>(act[0]) && std::get<2>(act[i]) == (1-min_idx)) {
						temp_add = (std::get<0>(act[0]) + 1440) - std::get<1>(act[i]);
					}
				} else {
					if (std::get<2>(act[i]) == std::get<2>(act[i+1]) && std::get<2>(act[i]) == (1-min_idx)) {
						temp_add += std::get<0>(act[i+1]) - std::get<1>(act[i]);
					}
				}
				if (max_add < temp_add) {
					max_add = temp_add;
					idx = i;
				}
			}
			add_bool[idx] = true;
			min_time += max_add;
			ans += 2;
		}
		
    	fout << "Case #" << t << ": " << ans << endl;
	}
}

