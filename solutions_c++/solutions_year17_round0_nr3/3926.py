#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <unordered_map>
#include <string>
#include <utility>
#include <unordered_set>
using namespace std;

pair <long long, long long> makeLine(long long n) {
	if (n <= 1)
		return make_pair(0,0);
	else if (n % 2 == 0)
		return make_pair(n/2,n/2-1);
	else
		return make_pair(n/2,n/2);
}

pair <long long, long long> getNextLine(long long n,pair <long long, long long> currentLine) {
	if (n % 2 == 0)
		return makeLine(currentLine.second);
	else
		return makeLine(currentLine.first);
}

pair <long long, long long> getDistances(long long n, long long k) {
	pair <long long, long long> firstLine;
	firstLine = makeLine(n);
	vector < long long > elements;
	vector <long long > linesToSearch;
	long long search = k-1;
	if (search == 0)
		return firstLine;
	else {
		elements.push_back(firstLine.first);
		elements.push_back(firstLine.second);
		long long nextElem;
		make_heap(elements.begin(),elements.end());
		for (long long i=0; i < search; i++) {
			nextElem = elements.front();
			pair <long long, long long> line = makeLine(nextElem);
			pop_heap(elements.begin(),elements.end());
			elements.pop_back();
			elements.push_back(line.first);
			push_heap(elements.begin(),elements.end());
			elements.push_back(line.second);
			push_heap(elements.begin(),elements.end());
		}
		return makeLine(nextElem);
	}
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i < t; i++) {
		long long n,k;
		cin >> n >> k;
	pair <long long, long long> ret = getDistances(n,k);
		
  		cout << "Case #" << i+1 << ": " << ret.first << " " << ret.second << endl;
	}

	return 0;
}