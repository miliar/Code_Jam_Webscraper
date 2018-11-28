#include <iostream>
#include <vector>
#include <queue>
#include <fstream>


using namespace std;

typedef long long big_t;

class Layout{
public:
	Layout() : size(0), number(0) {};
	Layout(big_t _size, big_t _number) : size(_size), number(_number) {};


	big_t size;
	big_t number;
};

class LayoutComparison{
public:
	bool operator()(Layout & l, Layout & r){
		return l.size < r.size;
	}
};

typedef struct minmax {
	big_t min;
	big_t max;
} MinMax;

Layout getAllLargest(priority_queue<Layout, vector<Layout>, LayoutComparison> & pq){
	big_t biggestSize = pq.top().size;
	big_t biggestNumber = 0;
	while (pq.top().size == biggestSize){
		biggestNumber += pq.top().number;
		pq.pop();
		if (pq.empty())
			break;
	}
	return Layout(biggestSize, biggestNumber);
}

big_t getLastSplitSeg(big_t stalls, big_t people){
	priority_queue<Layout, vector<Layout>, LayoutComparison> pq;

	big_t remainingPeople = people;
	pq.push(Layout(stalls,1));

	while (!pq.empty()){
		Layout toSplits = getAllLargest(pq);

		if (remainingPeople <= toSplits.number){
			return toSplits.size;
		}
		remainingPeople -= toSplits.number;

		if (toSplits.size % 2 == 1){
			Layout bothSides((toSplits.size-1)/2, toSplits.number*2);
			pq.push(bothSides);
		}
		else {
			Layout left((toSplits.size-1)/2, toSplits.number);
			Layout right(toSplits.size/2, toSplits.number);
			pq.push(left);
			pq.push(right);
		}
	}

	return -1; //never gonna be used anyway given our limits
}

MinMax getLastSplitMinMax(big_t stalls, big_t people){
	big_t lastSplit = getLastSplitSeg(stalls, people);
	big_t min = (lastSplit - 1) / 2;
	big_t max = lastSplit / 2;

	MinMax ret;
	ret.min = min;
	ret.max = max;

	return ret;
}

int main(){

	ifstream infile;
	infile.open("C-large.in");

	int numLines;
	infile>>numLines;

	big_t stalls;
	big_t people;

	vector<big_t> stallsArr;
	vector<big_t> peopleArr;

	for (int i=0; i<numLines; i++){
		infile>>stalls;
		stallsArr.push_back(stalls);
		infile>>people;
		peopleArr.push_back(people);
	}

	infile.close();

	ofstream outfile;

	outfile.open("C-large.out");

	for (int i=0; i<numLines; i++){
		MinMax result = getLastSplitMinMax(stallsArr[i], peopleArr[i]);
		outfile<<"Case #"<<(i+1)<<": ";
		outfile<<result.max<<" "<<result.min;
		outfile<<endl;
	}

	outfile.close();

	return 0;
}