#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

int main () {
	int t;
	scanf("%d", &t);
	for (int tc = 1 ; tc <= t; tc++){
		long long stalls, people;
		scanf("%lld %lld", &stalls, &people);
		map<long long,long long> freespace;
		freespace[stalls] = 1;
		for (long long p = 0; p < people - 1; p++){
			long long space = freespace.rbegin()-> first;
			long long num_of_space = freespace.rbegin()-> second;
			if (num_of_space == 1){
				freespace.erase(space);
			}
			else{
				freespace[space] = num_of_space - 1;
			}
			long long new_r = space / 2;
			long long new_l = space - new_r - 1;
			if (freespace.find(new_l) != freespace.end()){
				freespace[new_l] = freespace[new_l] + 1;
			}
			else freespace[new_l] = 1;
			if (freespace.find(new_r) != freespace.end()){
				freespace[new_r] = freespace[new_r] + 1;
			}
			else freespace[new_r] = 1;
		}
		long long space = freespace.rbegin()-> first;
		printf("Case #%d: %lld %lld\n", tc, space / 2 , space - (space / 2) - 1);

	}
}