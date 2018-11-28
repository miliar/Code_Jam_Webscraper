#include <bits/stdc++.h>

using namespace std;

int main(){
	int N;
	cin >> N;
	int k=0;
	while(N--){
		priority_queue <double> pq;
		int d, n;
		cin >> d >> n;
		while(n--){
			int ki, si;
			cin >> ki >> si;
			pq.push((d-ki)/(double)si);
		}

		printf("Case #%d: %.6lf\n", ++k, d/pq.top());
	}
}