#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h> 

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

using namespace std;

bool pair_sorter(pair<int, int> first, pair<int, int> second){
	if(first.first != second.first){
		return first.first < second.first;
	}
	else if(first.second != second.second){
		return first.second < second.second;
	}
	else{
		return true;
	}
}

int main(){

	int test_cases;
	cin >> test_cases;

	for(int case_num = 0; case_num < test_cases; case_num++){
		int N;
		int P;

		cin >> N;
		cin >> P;

		vector<int> required;
		for(int a = 0; a < N; a++){
			int inp;
			cin >> inp;

			required.push_back(inp);
		}

		vector< vector<int> > packages;
		for(int a = 0; a < N; a++){
			vector<int> package_values;
			for(int b = 0; b < P; b++){
				int inp;
				cin >> inp;

				package_values.push_back(inp);
			}

			packages.push_back(package_values);
		}

		vector< vector< pair<int, int> > > package_servings;
		
		for(int y = 0; y < packages.size(); y++){
			int required_quantity = required[y];
			vector< pair<int, int> > servings_for_ingredients;

			for(int x = 0; x < packages[y].size(); x++){
				float low_servings = packages[y][x]/(1.1*required_quantity);
				float high_servings = packages[y][x]/(0.9*required_quantity);
			
				int low = ceil(low_servings);
				int high = floor(high_servings);

				if(low <= high)	
					servings_for_ingredients.push_back(pair<int, int>(low, high));
			}
			package_servings.push_back(servings_for_ingredients);
		}

		tr(package_servings, it){
			sort(it->begin(), it->end(), pair_sorter);
		}
		cout << "Case #" << case_num+1 << ": ";

		int empty = 0;
		tr(package_servings, it){
			if(it->size() == 0)
				empty = 1;
		}

		if(empty){
			cout << "0" << endl;
		}
		else{
			vector<int> index(N, 0);

			int number_of_packages = 0;
			while(true){
				int highest_low = 0;
				int lowest_high = 1000000;

				for(int z = 0; z < package_servings.size(); z++){
					if( (package_servings[z][index[z]]).first > highest_low)
						highest_low = (package_servings[z][index[z]]).first;
					if( (package_servings[z][index[z]]).second < lowest_high)
						lowest_high = (package_servings[z][index[z]]).second;
				}

				if(highest_low <= lowest_high){
					tr(index, it){
						*it = (*it)+1;
					}
					number_of_packages++;
				}
				else{
					int break_outer = 0;
					for(int z = 0; z < package_servings.size(); z++){
						if( (package_servings[z][index[z]]).second < highest_low)
							index[z]++;
					}
				}

				int to_break = 0;
				for(int z = 0; z < package_servings.size(); z++){
					if(index[z] >= package_servings[z].size())
						to_break = 1;
				}

				if(to_break)
					break;
			}
			cout << number_of_packages << endl;
		}
	}
    return 0;	
}

