#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <stack>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

const int MaxN = 1e6;
int n, k;
struct BinaryHeap{
	int heap[MaxN + 5], reheap[MaxN + 5], tot_heap;
	bool SmallCompare(int x, int y) {return x > y;}
	bool BigCompare(int x, int y) {return x < y;}
	void Swap(int x, int y)
	{
		int temp;
		temp = heap[x]; heap[x] = heap[y]; heap[y] = temp;
		reheap[heap[x]] = x; reheap[heap[y]] = y;
	}
	void Up(int x)
	{
		int p = x;
		while((p > 1) && SmallCompare(heap[p],  heap[p >> 1]))
		{
			Swap(p, p >> 1);
			p >>= 1;
		}
	}
	void Down(int x)
	{
		int p = x, q = p << 1;
		while(q <= tot_heap) 
		{
			if((q < tot_heap) && SmallCompare(heap[q + 1], heap[q])) q++;
			if(!BigCompare(heap[p], heap[q])) return;
			Swap(p, q); p = q; q = p << 1;
		}
	}
	void Insert(int x)
	{
		heap[++tot_heap] = x;
		reheap[x] = tot_heap;
		Up(tot_heap);
	}
	void Delete(int x)
	{
		Swap(x, tot_heap);
		tot_heap--;
		Up(x);  Down(x);
	}
}P;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--) {
		P.tot_heap = 0;
		scanf("%d%d", &n, &k);
		P.Insert(n);
		int ans1, ans2;
		for(int i = 1; i <= k; i++) {
			int x = P.heap[1];
			P.Delete(1);
			int t = (x - 1) / 2;
			P.Insert(t);
			P.Insert((x - 1) - t);
			if(i == k) {
				ans1 = (x - 1) - t;
				ans2 = t;
			}
		}
		printf("Case #%d: ", ++cas);
		printf("%d %d\n", ans1, ans2);
	}
	fclose(stdin);
	fclose(stdout);
}
