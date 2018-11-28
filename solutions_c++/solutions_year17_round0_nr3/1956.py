#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>

#define ODD(x) x % 2 != 0
using namespace std;

struct RangeStruct{
	long long int Range;
	long long int Count = 1;
};

bool RangeCompare(const RangeStruct r1, const RangeStruct r2){
	return(r1.Range > r2.Range);
}

set<RangeStruct, bool(*) (const RangeStruct r1, const RangeStruct r2)> RangeSet(&RangeCompare);

void SafeInsert(RangeStruct temp){
	if (RangeSet.find(temp) != RangeSet.end()) {
		temp.Count += RangeSet.find(temp)->Count;
		RangeSet.erase(temp);
	}
	RangeSet.insert(temp);
}

int main(){
	//FILE *f = fopen("input.txt", "r");
	int NumberOfTestCases, i;
	RangeStruct temp, curr;
	long long int BathroomStalls, People, CurrPow2;
	pair<long long int, long long int> CurrDist;

	fscanf(stdin, "%d", &NumberOfTestCases);

	for (i = 1; i <= NumberOfTestCases; i++) {
		RangeSet.clear();
		fscanf(stdin, "%lld %lld", &BathroomStalls, &People);
		temp.Range = BathroomStalls;
		temp.Count = 1;
		RangeSet.insert(temp);
		while (People > 0) {
			curr = *RangeSet.begin();
			RangeSet.erase(RangeSet.begin());
			if (ODD(curr.Range)) {
				People -= curr.Count;
				CurrDist = make_pair(curr.Range / 2, curr.Range / 2);
				temp.Range = curr.Range / 2;
				temp.Count = curr.Count * 2;
				SafeInsert(temp);
			} else {
				People -= curr.Count;
				CurrDist = make_pair(curr.Range / 2, max(curr.Range / 2 - 1, 0LL));
				temp.Range = curr.Range / 2;
				temp.Count = curr.Count;
				SafeInsert(temp);
				temp.Range = max(temp.Range - 1, 0LL);
				SafeInsert(temp);
			}

		}
		printf("Case #%d: %lld %lld\n", i, CurrDist.first, CurrDist.second);
	}

	return 0;
}