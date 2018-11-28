#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cmath>
#include <queue>
using namespace std;


struct Interval {
	int Left;
	int Right;
	int Val = abs(Right - Left);
	bool operator<(const Interval& v)const {
		return Val < v.Val;
	}
	Interval(int left, int right) :Left(left), Right(right) {};
};


int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	#endif // ONLINE_JUDGE
	int T;
	int index = 1;
	cin >> T;
	while (T) {
		int N, K;
		cin >> N >> K;
		priority_queue<Interval> maxHeap;
		maxHeap.push(Interval(0, N + 1));
		for (int i = 0; i < K; i++) {
			Interval v = maxHeap.top();
			maxHeap.pop();
			int Middle = (v.Left + v.Right) / 2;
			if (i == K - 1) {
				if (Middle != v.Left) {
					cout << "Case #" << index << ": " << max(abs(v.Left - Middle), abs(v.Right - Middle)) - 1 << " ";
					cout << min(abs(v.Left - Middle), abs(v.Right - Middle)) - 1 << endl;
				}
				else {
					cout << "Case #" << index << ": " << max(abs(v.Left - Middle), abs(v.Right - Middle)) << " ";
					cout << min(abs(v.Left - Middle), abs(v.Right - Middle)) << endl;
				}
			}
			maxHeap.push(Interval(v.Left, Middle));
			maxHeap.push(Interval(Middle, v.Right));
		}
		T--;
		++index;
	}
}