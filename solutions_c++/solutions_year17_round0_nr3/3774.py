#include <iostream>
#include <queue>

using namespace std;

#define Aman Jain

int main(){
	priority_queue <long long> pq;
	int testcase;
	long long number, ans1, ans2, person;
	cin >> testcase;
	for(int i=1;i<=testcase;i++){
		cin >> number >> person;
		pq.push(number);
		for(int j=0;j<person;j++){
			int k = pq.top();
			ans1 = k/2;
			ans2 = (k-1)/2;
			pq.pop();
			pq.push(k/2);
			pq.push((k-1)/2);
		}
		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
		while(!pq.empty())
			pq.pop();
	}
	return 0;
}