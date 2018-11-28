#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int nTests;
int n, k;

struct HeapNode {
	int MIN, MAX, position;
	int left, right;

	HeapNode() {
	}

	HeapNode(int left_, int right_) {
		left = left_;
		right = right_;
		position = (left + right) / 2;
		MIN = min(position - left, right - position);
		MAX = max(position - left, right - position);
	}

	bool operator < (HeapNode &another) const {
		if (MIN > another.MIN) {
			return true;
		}
		if (MIN < another.MIN) {
			return false;
		}
		if (MAX > another.MAX) {
			return true;
		}
		if (MAX < another.MAX) {
			return false;
		}
		if (position < another.position) {
			return true;
		}
		return false;
	}
};

int nHeaps;
HeapNode heap[3000000];

void up(int node) {
	int parent = node / 2;
	while (parent >= 1) {
		if (heap[node] < heap[parent]) {
			swap(heap[node], heap[parent]);
			node = parent;
			parent = node / 2;
		} else {
			break;
		}
	}
}

void down(int node) {
	int child = 2 * node;
	while (child <= nHeaps) {
		if ((child + 1 <= nHeaps) && (heap[child + 1] < heap[child])) {
			++child;
		}
		if (heap[child] < heap[node]) {
			swap(heap[child], heap[node]);
			node = child;
			child = 2 * node;
		} else {
			break;
		}
	}
}

void push(HeapNode node) {
	++nHeaps;
	heap[nHeaps] = node;
	up(nHeaps);
}

HeapNode pop(int node) {
	HeapNode ret = heap[node];
	heap[node] = heap[nHeaps];
	--nHeaps;
	up(node);
	down(node);
	return ret;
}

pair<int, int> process() {
	nHeaps = 0;
	push(HeapNode(1, n));
	int MIN;
	int MAX;
	for (int i = 1; i <= k; ++i) {
		HeapNode node = pop(1);
		if (i == k) {
			MIN = node.MIN;
			MAX = node.MAX;
		}
		if (node.right > node.position) {
			push(HeapNode(node.position + 1, node.right));
		}
		if (node.position > node.left) {
			push(HeapNode(node.left, node.position - 1));
		}
	}
	return make_pair(MIN, MAX);
}

int main(int argc, char **argv) {
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		cin >> n >> k;
		pair<int, int> res = process();
		cout << "Case #" << test << ": " << res.second << " " << res.first << endl;
	}
	return 0;
}