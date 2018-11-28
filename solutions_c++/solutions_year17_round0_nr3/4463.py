// Codejam_Sample.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <limits.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

//#define CONSOLE

#define IN		cin
#define OUT		cout

class Heap {
	pair<int, pair<int, int>> *arr;
	int size;

public:
	Heap() {
		arr = new pair<int, pair<int, int>>[1000000];
		size = 1;
	}

	int left(int cur) { return cur * 2; }
	int right(int cur) { return cur * 2 + 1; }

	void push(pair<int, pair<int, int>> data) {
		arr[size] = data;
		size++;
		upHeap(size - 1);
	}

	pair<int, pair<int, int>> top() {
		return arr[1];
	}

	void pop() {
		arr[1] = arr[size - 1];
		size--;
		Heapify(1);
	}

	void Heapify(int cur) {
		int l = left(cur);
		int r = right(cur);
		int largest = cur;

		if (l < size && arr[l] > arr[cur])
			largest = l;
		if (r < size && arr[r] > arr[largest])
			largest = r;
		if (largest != cur) {
			swap(arr[largest], arr[cur]);
			Heapify(largest);
		}
	}

	void upHeap(int p) {
		if (p <= 1)
			return;

		int a = arr[p].first;
		int b = arr[(int)ceil(p / 2)].first;

		if (arr[p].first > arr[(int)ceil(p / 2)].first)
		{
			swap(arr[p], arr[(int)ceil(p / 2)]);
			upHeap((int)ceil(p / 2));
		}
		else if (arr[p].first == arr[(int)ceil(p / 2)].first)
		{
			if (arr[p].second.first < arr[(int)ceil(p / 2)].second.first)
			{
				swap(arr[p], arr[(int)ceil(p / 2)]);
				upHeap((int)ceil(p / 2));
			}
		}
	}

	void printAll() {
		cout << endl;
		cout << "-------------------------------------------" << endl;
		cout << endl;
		for (int i = 1; i < size; i++) {
			cout << arr[i].first << "\t" << arr[i].second.first << "\t" << arr[i].second.second << endl;
		}

		cout << endl;
		cout << "-------------------------------------------" << endl;
		cout << endl;
	}
};


int main() {
#ifndef CONSOLE
	fstream IN, OUT;
	IN.open("inB.txt", ios::in);
	OUT.open("outB.txt", ios::out);
#endif

	/*
	*
	*	START CODE HERE
	*
	*/

	int T; IN >> T;
	for (int t = 0; t < T; t++) {		
		int N, K; 
		IN >> N >> K;

		if (N <= K) {
			OUT << "Case #" << t + 1 << ": " << 0 << " " << 0 << endl;
			continue;
		}

		/*priority_queue<pair<int, pair<int, int>>> pq;
		pq.push(make_pair(N, make_pair(1, N)));
		int y = INT_MIN, z = INT_MAX;
		for (int i = 0; i < K - 1; i++) {
			pair<int, pair<int, int>> t = pq.top(); pq.pop();

			int mid = (t.second.first + t.second.second) / 2;
			pq.push(make_pair(mid - t.second.first, make_pair(t.second.first, mid - 1)));
			pq.push(make_pair(t.second.second - mid, make_pair(mid + 1, t.second.second)));
		}

		pair<int, pair<int, int>> r = pq.top(); pq.pop();
		int mid = (r.second.first + r.second.second) / 2;
		y = max(mid - r.second.first, r.second.second - mid);
		z = min(mid - r.second.first, r.second.second - mid);*/
		
		Heap pq;
		pq.push(make_pair(N, make_pair(1, N)));
		int y = INT_MIN, z = INT_MAX;
		for (int i = 0; i < K - 1; i++) {
			pair<int, pair<int, int>> t = pq.top(); 
			pq.pop();
			int mid = (t.second.first + t.second.second) / 2;
			pq.push(make_pair(mid - t.second.first, make_pair(t.second.first, mid - 1)));
			pq.push(make_pair(t.second.second - mid, make_pair(mid + 1, t.second.second)));
		}

		pair<int, pair<int, int>> r = pq.top(); pq.pop();
		int mid = (r.second.first + r.second.second) / 2;
		y = max(mid - r.second.first, r.second.second - mid);
		z = min(mid - r.second.first, r.second.second - mid); 	
		OUT << "Case #" << t + 1 << ": " << y << " " << z << endl;
	}

#ifndef CONSOLE
	IN.close();
	OUT.close();
#endif

	return 0;
}

