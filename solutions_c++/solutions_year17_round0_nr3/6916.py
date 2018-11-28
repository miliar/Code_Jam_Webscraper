#include <iostream>
#include <algorithm>    // std::find
#include <string>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>     /* atoi */

using namespace std;

int main()
{
	int cases, n, k, index;
	pair<int, int> cur_pair;
	string s;
	cin >> cases;
	for (int c = 0; c < cases; ++c)
	{	
		cin >> n >> k;

		pair<int, int> stalls[n];
		bool taken[n];

		for(int i = 0; i < n; i++) {
			stalls[i].first = i; 
			stalls[i].second = n - i - 1;
			taken[i] = false;
		}

		for(int x = 0; x < k; x++) {
			for(int i = 0; i < n; i++) {
				if(!taken[i]) {	
					cur_pair = stalls[i];
					index = i;
					break;
				}
			}			
			for(int i = 0; i < n; i++) {
				if(!taken[i]) {					
					if(min(stalls[i].first, stalls[i].second) > min(cur_pair.first, cur_pair.second)) {
						cur_pair = stalls[i];
						index = i;
					} else if (min(stalls[i].first, stalls[i].second) == min(cur_pair.first, cur_pair.second)) {
						if ((max(stalls[i].first, stalls[i].second) > max(cur_pair.first, cur_pair.second))) {
							cur_pair = stalls[i];
							index = i;
						} 
					}
					//cout << i << ": " << stalls[i].first << " " << stalls[i].second << " ";
					//cout << "; cur " << index << ": " << stalls[index].first << " " << stalls[index].second << endl;
				}				
			}
			//cout << "Chosen " << index << ": " << stalls[index].first << " " << stalls[index].second << endl;
			for(int i = index - 1; i >= 0; i--) {
				stalls[i].second = min(index - 1 - i, stalls[i].second);
			} 
			for(int i = index + 1; i < n; i++) {
				stalls[i].first = min(i - (index + 1), stalls[i].first);
			}
			taken[index] = true;
		}

		cout << "Case #" << c + 1 << ": " << max(cur_pair.first, cur_pair.second) << " " << min(cur_pair.first, cur_pair.second) << endl;
	}
	return 0;
}