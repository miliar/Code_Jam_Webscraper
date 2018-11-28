#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <limits>
#include <cmath>
#include <functional>
#include <list>
#include <numeric>
#include <string.h>
#include <queue>

using namespace std;

#define ll	long long
#define ld	long double
#define vi	vector<int>
#define rep(i,a,b)	for(int i=a;i<b;i++)

class Heap {
public:
	Heap(int c)
		:capacity(c) {
		heap = new int[Heap::capacity];
	}
	~Heap() {
		delete[] heap;
	}
	void Insert(int data) {
		int usedPos = usedsize;
		int parantPos = (int)((usedPos - 1) / 2);
		if (usedsize == capacity) {
			cout << "FULL" << endl;
			return;
		}
		heap[usedsize] = data;
		while (usedPos > 0 && heap[usedPos] > heap[parantPos]) {
			Swap(&heap[usedPos], &heap[parantPos]);
			usedPos = parantPos;
			parantPos = (int)((usedPos - 1) / 2);
		}
		usedsize++;
	}
	void Swap(int * a, int * b) {
		int t = *a;
		*a = *b;
		*b = t;
	}
	int extractMax() {
		if (usedsize == 0)
			return -1;
		int parentPos = 0, leftPos = 1, rightPos = 2;
		int ret = heap[0];
		heap[0] = NULL;
		usedsize--;
		Swap(&heap[0], &heap[usedsize]);
		while (true) {
			int selectChild = 0;
			if (leftPos >= usedsize)
				break;
			else if (rightPos >= usedsize)
				selectChild = leftPos;
			else {
				if (heap[leftPos] < heap[rightPos])
					selectChild = rightPos;
				else
					selectChild = leftPos;
			}

			if (heap[selectChild] > heap[parentPos]) {
				Swap(&heap[parentPos], &heap[selectChild]);
				parentPos = selectChild;
			}
			else
				break;
			leftPos = 2 * parentPos + 1;
			rightPos = leftPos + 1;

		}
		return ret;
	}
private:
	int capacity;
	int * heap;
	int usedsize;
};

int main()
{
	int T;	cin >> T;
	for (int t = 0; t < T; t++) {
		int K, N; cin >> N >> K;
		Heap H(N);
		H.Insert(N);
		for (int k = 0; k < K - 1; k++) {
			int max = H.extractMax() - 1;			
			H.Insert(max / 2);
			H.Insert(max - max / 2);
		}
		int max = H.extractMax() - 1;
		

		cout << "Case #" << t + 1 << ": "<<max-max/2<<' '<<max/2<<endl;
	}
	return 0;
}