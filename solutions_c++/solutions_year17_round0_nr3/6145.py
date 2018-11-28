#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
using namespace std;

struct data {
	long long left;
	long long right;
	long long length;
	bool operator<(const data &rhs) const {
		if (length > rhs.length) {
			return false;
		}
		else if (length == rhs.length) {
			return left > rhs.left;
		}
		else return true;
	}
};

int main() {
	int t;
	scanf("%d",&t);

	long long N, P;
	for (int i=0; i<t; i++) {
		scanf("%lld %lld",&N, &P);

		bool array[N+2];
		memset(array, false, sizeof(array));
		array[0] = true;
		array[N+1] = true;
		long long last_insertion = -1;

		long long l = 1;
		long long r = N;
		data d;
		d.left = l;
		d.right = r;
		d.length = r - l + 1;
		priority_queue<data> pq;
		pq.push(d);


		for (long long j=1; j<=P; j++) {
			data current_data = pq.top();
			pq.pop();
			// cout << "TAKE " << current_data.left << " " << current_data.right << " " << current_data.length << endl;

			long long median = (current_data.left+current_data.right)/2;
			array[median] = true;
			
			//make 2 partitions
			data p1;
			p1.left = current_data.left;
			p1.right = median-1;
			p1.length = p1.right - p1.left + 1;

			data p2;
			p2.left = median + 1;
			p2.right = current_data.right;
			p2.length = p2.right - p2.left + 1;
			pq.push(p2);
			pq.push(p1);

			// cout << "INSERT at " << median << endl;
			// cout << "p1 " << p1.left << " " << p1.right << " " << p1.length << endl;
			// cout << "p2 " << p2.left << " " << p2.right << " " << p2.length << endl;
			// cout << endl;
			if (j==P) {
				last_insertion = median;
			}
		}

		long long left_most = -1;
		for (long long k=last_insertion-1; k>=0; k--) {
			if (array[k]) {
				left_most = k;
				break;
			}
		}

		long long right_most = -1;
		for (long long k=last_insertion+1; k<=N+1; k++) {
			if (array[k]) {
				right_most = k;
				break;
			}
		}	

		long long Ls = last_insertion - left_most - 1;
		long long Rs = right_most - last_insertion - 1;
		printf("Case #%d: %lld %lld\n",i+1,max(Ls, Rs), min(Ls, Rs));
	}
	return 0;
}