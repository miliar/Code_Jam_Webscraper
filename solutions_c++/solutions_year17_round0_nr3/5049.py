#include <iostream>
#include <queue>

struct interval {
	int LS;
	int RS;
	int left;
	int right;
	int posS;
	
	interval(int left, int right) {
		this->left = left;
		this->right = right;
		this->posS = (right + left) / 2;
		this->LS = this->posS - this->left;
		this->RS = this->right - this->posS;
	}
};

bool operator < (interval A, interval B) {
	bool result;
	if(A.LS < B.LS) result = true;
	if(A.LS > B.LS) result = false;
	if(A.LS == B.LS) {
		if(A.RS < B.RS) result = true;
		if(A.RS > B.RS) result = false;
		if(A.RS == B.RS) {
			if(A.posS < B.posS) {
				result = true;
			} else {
				result = false;
			}
		}
	}
	return result;
}

using namespace std;

int main() {
	int z;
	cin >> z;
	
	for(int ii = 1; ii <= z; ii++) { 
		int N, K;
		cin >> N >> K;
		
		priority_queue <interval> queue;
		
		interval I(1, N);
		queue.push(I);
		
		int l, r;
		
		for(int i = 1; i <= K; i++) {
			interval tmp = queue.top();
			queue.pop();
			
			l = tmp.LS;
			r = tmp.RS;
			
			interval tmp1(tmp.left, tmp.posS - 1);
			interval tmp2(tmp.posS + 1, tmp.right);
			
			queue.push(tmp1);
			queue.push(tmp2);
		}
		
		cout << "Case #" << ii << ": " << r << " " << l << endl;
	}
	
	return 0;
}
