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

bool bin_comp(pair<int, int> left, int val){
	return left.first < val;
}

int main(){
	int test_cases;
	cin >> test_cases;

	for(int a = 0; a < test_cases; a++){
		long N;
		long K;

		cin >> N;
		cin >> K;

		vector< pair<int, int> > spaces;
		spaces.push_back( pair<int, int>(N, 1) );

		for(int i = 0; i < K; i++){
			pair<int, int> largest_space = spaces[spaces.size()-1];
			largest_space.second = largest_space.second-1;

			if(largest_space.second == 0)
				spaces.erase(spaces.end()-1);				
			else
				spaces[spaces.size()-1].second--;
			
			int size = largest_space.first;
			int left;
			int right;

			if(size % 2 == 0){
				left = (size/2)-1;
				right = size/2;
			}
			else{
				left = (size-1)/2;
				right = (size-1)/2;
			}

			if(left > 0){
				vector< pair<int, int> >::iterator left_it = lower_bound(spaces.begin(), spaces.end(), left, bin_comp);
				
				if(left_it == spaces.end())
					spaces.push_back(pair<int, int>(left, 1));
				else if(left_it->first == left){
					left_it->second += 1;
				}
				else{
					spaces.insert(left_it, pair<int, int>(left, 1));
				}
			}

			if(right > 0){
				vector< pair<int, int> >::iterator right_it = lower_bound(spaces.begin(), spaces.end(), right, bin_comp);
				if(right_it == spaces.end())
					spaces.push_back(pair<int, int>(right, 1));
				else if(right_it->first == right){
					right_it->second += 1;
				}
				else{
					spaces.insert(right_it, pair<int, int>(right, 1));
				}
			}
			
			if(i == K-1)
				cout << "Case #" << a+1 << ": " << max(left, right) << " " << min(left, right) << endl; 
		}
	}
    return 0;	
}

