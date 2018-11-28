#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

void find_sub(priority_queue<long long int> &max_heap){

	long long int maxval = max_heap.top();
	long long int i = 1, j = 0;

	max_heap.pop();

	if(maxval % 2){

		max_heap.push(maxval >> 1);
		max_heap.push(maxval >> 1);
	}else{
		max_heap.push(maxval >> 1);
		max_heap.push((maxval >> 1) - 1);
	}
}

vector<long long int> sol(vector<long long int>& a, long long int b){
	if(a[0] == b) return {0, 0};

	priority_queue<long long int>max_heap;
	max_heap.push(a[0]);

	for(long long int i = 0; i < b - 1; ++i){
		find_sub(max_heap);

	}

	long long int maxv = max_heap.top();

	if(maxv % 2){
		return {maxv >> 1, maxv >> 1};
	}else return {maxv >> 1, (maxv >> 1) - 1};
}

int main(){
	int t;
	cin >> t;
	
	long long int a;
	long long int b; 
	for(int i = 0; i < t; ++i){
		cin >> a >> b;
		vector<long long int> tt;
		tt.push_back(a);
		vector<long long int> ans = sol(tt, b);
		int c = ans[0], d = ans[1];
		cout << "Case #" << i+1 << ": " << c << " " << d << endl;
	}
}