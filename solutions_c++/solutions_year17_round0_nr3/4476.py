#include <cstdio>
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

void solve() {
	int n,k,t;
	scanf("%d%d",&n,&k);

	priority_queue<int> slot;
	slot.push(n);
	for (int i=0;i<k-1;i++) {
		t = slot.top();
		slot.pop();
		slot.push((t-1)/2);
		slot.push(t-1-(t-1)/2);
	}
	t = slot.top();
	printf("%d ",t-1-(t-1)/2);
	printf("%d\n",(t-1)/2);
}

int main() {
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		solve();
	}

	return 0;
}