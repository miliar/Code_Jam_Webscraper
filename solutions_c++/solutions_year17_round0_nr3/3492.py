
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

void printVec(vector<long long> v) {
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i] << " ";
	}
	cout << endl;
}


vector<long long> findStalls(long long N, long long K) {
	
	long long pre = N;
	priority_queue<long long> q;
	q.push(N);
	for (long long i = 0; i < K; ++i) {
		long long t = q.top(); q.pop();
		q.push(t / 2);
		if (t % 2 == 0) {
			q.push(t / 2 - 1);
		} else {
			q.push(t / 2);
		}
		pre = t;
	}
	if (pre % 2 == 0) return {pre / 2, pre / 2 - 1};
	else return {pre / 2, pre / 2};
}



int main() {
	
	ifstream in("C-small-2-attempt0.in");
	ofstream out("C-small-2-attempt0.out");
	
	int n;
	long long N, K;
	in >> n;
	
	
	for (int i = 1; i <= n; ++i) {
		in >> N >> K;
		vector<long long> res = findStalls(N, K);
		out << "Case #" << i << ": " << res[0] << " " << res[1] << endl;
	}
	
	
	printVec(findStalls(4, 2));
	printVec(findStalls(5, 2));
	printVec(findStalls(6, 2));
	printVec(findStalls(1000, 1000));
	printVec(findStalls(1000, 1));
}





