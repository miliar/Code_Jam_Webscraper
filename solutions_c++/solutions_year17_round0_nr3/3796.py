#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
void insert(long long int N, map<long long int, int>& Map_container) {
    long long int left, right;
    left = (N-1)/2;
    right = N - left - 1;
    auto iter = Map_container.find(left);
    if (iter==Map_container.end()) Map_container.insert(make_pair(left,0));
    if (left!=0) insert(left, Map_container);

    iter = Map_container.find(right);
    if (iter==Map_container.end()) Map_container.insert(make_pair(right,0));
    if (right!=0) insert(right, Map_container);
}
int main() {
    int T;
    int ans;
    cin >> T;
    for (int t = 0 ; t < T; ++t) {
	long long int N, K;
	long long int Max, Min;
	cin >> N >> K;
	map <long long int, int> Map_container;
	if (N==K) {
	    cout << "Case #" << (t+1) << ": 0 0" << endl;
	    continue;
	}
	Map_container.insert(make_pair(N,1));
	insert(N, Map_container);

#if 0
	for (auto iter = Map_container.begin(); iter!=Map_container.end(); iter++) {
	    cout << iter->first << endl;
	}
#endif
	Map_container[N] = 1;
	for (auto iter=Map_container.rbegin(); iter!=Map_container.rend();++iter) {
	    if (K==0) break;
	    if (iter->second < K) {
		long long int left, right;
		left = (iter->first-1)/2;
		right = iter->first - left - 1;
		Map_container[left]  += iter->second;
		Map_container[right] += iter->second;
		K -=iter->second;
		iter->second = 0;
	    }
	    else { // iter->second >=K)
		long long int left, right;
		left = (iter->first-1)/2;
		right = iter->first - left - 1;
		Map_container[left]  += K;
		Map_container[right] += K;
		iter->second -= K;
		K = 0;
		Max = right;
		Min = left;
	    }
	}
	cout << "Case #" << (t+1) << ": " << Max << " " << Min<< endl;
    }

    return 0;
}
