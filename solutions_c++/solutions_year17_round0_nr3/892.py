#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <map>
#include <random>


using namespace std;

struct Params {
	long long start;
	long long len;
};

bool operator<(const Params & p1, const Params & p2) {
	return p1.len < p2.len;
}

priority_queue<Params> recursiveCalls;
//vector<char> stalls;

void recursiveSolve(Params p) {
	if (p.len == 1) {
		//
		//stalls[p.start] = 'O';
		//
	}
	else if(p.len == 2) {
		//
		//stalls[p.start] = 'O';
		//
		Params p2{ p.start + 1, 1 };//right
		recursiveCalls.push(p2);
	}

	else if (p.len % 2 == 1) {
		//
		//stalls[p.start + p.len / 2] = 'O';
		//


		Params p1{ p.start, p.len / 2 };//left
		Params p2{ p.start + p.len / 2 + 1, p.len / 2 };//right
		recursiveCalls.push(p1);
		recursiveCalls.push(p2);
	}
	else {
		//
		//stalls[p.start + p.len / 2 - 1] = 'O';
		//
		Params p1{ p.start, p.len / 2 - 1 };//left
		Params p2{ p.start + p.len / 2, p.len / 2 };//right
		recursiveCalls.push(p2);
		recursiveCalls.push(p1);
	}
}

void printStalls(vector<char> stalls) {
	cout << 'X';
	for (char c : stalls)
		cout << c;
	cout << 'X';
	cout << endl;
}

pair<long long, long long> solveCase(long long stallsCount, long long people) {
	recursiveCalls = priority_queue<Params>();

	Params p{ 0, stallsCount };
	recursiveCalls.push(p);

	//
	//stalls = vector<char>(stallsCount);
	//for (int i = 0; i < stallsCount; i++) stalls[i] = '.';
	//

	for (long long i=people-1; i>0;i--) {
		recursiveSolve(recursiveCalls.top());
		recursiveCalls.pop();
		//printStalls(stalls);
	}

	Params last = recursiveCalls.top();

	long long min, max;
	if (last.len % 2 == 1) {
		min = max = last.len / 2;
	}
	else {
		max = last.len / 2;
		min = max - 1;
	}
	return make_pair(max, min);
}


//
//struct Data {
//	int pos, lDist, rDist;
//};
//
//ostream & operator<<(ostream & o, const Data & d){
//	o << "Pos: " << d.pos << " l: " << d.lDist << " r: " << d.rDist;
//	return o;
//}
//
//
//int dist(vector<bool> & stalls, int pos, bool left) {
//	for(int i=1;;i++) {
//		int shift = left ? -i : i;
//		if (stalls[pos + shift])
//			return i-1;
//	}
//}
//
//bool dataComp(const Data & d1, const Data & d2) {
//	if (min(d1.lDist, d1.rDist) == min(d2.lDist, d2.rDist)) {
//		if (max(d1.lDist, d1.rDist) == max(d2.lDist, d2.rDist)) {
//			return d1.pos < d2.pos;
//		}
//		return max(d1.lDist, d1.rDist) > max(d2.lDist, d2.rDist);
//	}
//	return min(d1.lDist, d1.rDist) > min(d2.lDist, d2.rDist);
//}
//
//void printStalls(vector<bool> s) {
//	for (bool b : s)
//		if (b) cout << 'O';  else cout << ".";
//	cout << endl;
//}
//
//pair<int, int> naiveSolve(int stallsCount, int people) {
//	vector<bool> stalls(stallsCount + 2);
//	stalls[0] = stalls[stalls.size() - 1] = true;
//	//printStalls(stalls);
//	while(true) {
//		vector<Data> datas;
//		for (int i = 1; i < stallsCount + 1; i++) {
//			if (stalls[i])
//				datas.push_back({ i, 0, 0 });
//			else
//				datas.push_back({ i, dist(stalls, i, true), dist(stalls, i, false) });
//			
//		}
//		
//		Data best = *min_element(datas.begin(), datas.end(), dataComp);
//		--people;
//		stalls[best.pos] = true;
//		//printStalls(stalls);
//		
//
//		if (people == 0) {
//			Data d1 = best;
//			//cout << max(d1.lDist, d1.rDist) << " " << min(d1.lDist, d1.rDist);
//			return make_pair(max(d1.lDist, d1.rDist), min(d1.lDist, d1.rDist));
//		}
//
//	}
//
//}

struct Size {
	int lenght;
	int positionsCount;
};





void addInterval(const long long size, const long long count, map<long long, long long> & map) {
	if (size <= 0 || count <= 0)
		return;

	if (map.count(size) == 0)
		map.insert(make_pair(size, count));
	else
		map[size] = map[size] + count;

}

pair<long long, long long> evenFasterShit(long long stalls, long long people) {
	map<long long, long long> sizes;
	sizes.insert(make_pair(stalls,(long long) 1));

	while (true) {
		long long intervalSize = sizes.rbegin()->first;
		long long intervalsCount = sizes.rbegin()->second;

		if (people - intervalsCount <= 0 ) {
			break;
		}

		if (intervalSize %2 == 1) {
			addInterval(intervalSize / 2, intervalsCount * 2, sizes);
		}
		else {
			addInterval(intervalSize / 2, intervalsCount, sizes);
			addInterval(intervalSize / 2 -1, intervalsCount, sizes);
		}

		people -= intervalsCount;
		sizes.erase(intervalSize);
	}

	long long intervalSize = sizes.rbegin()->first;
	long long min, max;
	if (intervalSize % 2 == 1) {
		min = max = intervalSize / 2;
	}
	else {
		max = intervalSize / 2;
		min = max - 1;
	}
	return make_pair(max, min);
}


void main() {
	int cases;
	cin >> cases;
	for (int i=0;i<cases;i++) {
		long long stalls, people;
		cin >> stalls >> people;
		cout << "Case #" << i + 1 << ": ";
		pair<long long, long long> solution = evenFasterShit(stalls, people);
		cout << solution.first << " " << solution.second;
		cout << endl;
	}

	//int tests = 10000;

	//random_device rd;
	//mt19937 eng(rd());
	//uniform_int_distribution<int> dist(1, 200000);

	//for (int i=0;i<tests;i++) {
	//	int stalls = dist(eng);
	//	uniform_int_distribution<int> dist1(1, stalls);
	//	int people = dist1(eng);
	//	//stalls = 6;
	//	//people = 3;

	//	pair<int, int> fast = solveCase(stalls, people);
	//	pair<int, int> naive = evenFasterShit(stalls, people);
	//	if (fast.first != naive.first || fast.second != naive.second)
	//	cout << "Problem with case stalls: " << stalls << " people " << people<< endl;
	//
	//}
	
}