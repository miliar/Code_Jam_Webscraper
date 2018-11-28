#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<int> vint;

int main(int argc, char const *argv[])
{
	int T; cin >> T;
	for(int a0=1; a0<=T; a0++){
		int N,K; cin >> N >> K;

		int max=0,min=0;
		vint heap;
		heap.push_back(N);
		make_heap(heap.begin(),heap.end());
		
		for(int a1=0; a1<K; a1++){
			pop_heap(heap.begin(),heap.end());
			int next = heap.back();
			heap.pop_back();
			max = next/2;
			min = next-1-max;
			heap.push_back(max);
			push_heap(heap.begin(),heap.end());
			heap.push_back(min);
			push_heap(heap.begin(),heap.end());
		}

		printf("Case #%d: %d %d\n",a0,max,min);
	}
	return 0;
}