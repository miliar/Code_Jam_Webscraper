#include <iostream>
// #include <string>
// #include <map>
#include <vector>
// #include <list>
// #include <pair>
#include <tgmath.h>
#include <algorithm>
#include <queue>

using namespace std;
typedef vector<long>::iterator vec_it;

class comp
{
public:
	comp() {}
	bool operator() (const pair<long, long>& lhs, const pair<long, long>& rhs) const
	{
		long left_mid = (lhs.second + lhs.first) / 2;
		long left_Ls = left_mid - lhs.first ;
		long left_Rs = lhs.second - left_mid;
		long right_mid = (rhs.second + rhs.first) / 2;
		long right_Ls = right_mid - rhs.first;
		long right_Rs = rhs.second - right_mid;
		if (min(left_Ls, left_Rs) < min(right_Ls, right_Rs)) {
			return true;
		} else if(min(left_Ls, left_Rs) == min(right_Ls, right_Rs)) {
			if (max(left_Ls, left_Rs) < max(right_Ls, right_Rs)) {
				return true;
			} else if (max(left_Ls, left_Rs) == max(right_Ls, right_Rs)) {
				return left_Ls > right_Ls;
			}
		}
		return false;
	}
};
typedef std::priority_queue<pair<long, long>,std::vector<pair<long, long>>,comp> mypq_type;

pair<long,long> solve_C(long N, long K);
pair<long,long> solve_C_2(long N, long K);
pair<long,long> solve_C_3(long N, long K);
pair<long, long> find_longest_zeros(vector<long> arr, long *index);
pair<long, long> calc_final(vec_it it);
void solve_C_aux(long left, long right, long K);




int main() {
	int len;
	vector<pair<long,long> > in;
	
	cin >> len;
	for (int i = 1; i <= len; ++i) {
		long N,K;
		
		cin >> N >> K;
		in.push_back(pair<long,long>(N, K));
	}
	
	for (int i = 0; i < len; ++i) {
		pair<long,long> sol = solve_C_3(in[i].first, in[i].second);
		cout << "Case #" << i + 1 << ": " << sol.first << " " << sol.second;
		if(i != len - 1)
			cout << endl;
	}
	
	return 0;
}

pair<long,long> solve_C(long N, long K) {
	vector<long> arr;
	pair<long,long> sol;
	arr.push_back(-1);
	arr.push_back(N);
	
	long curr;
	long index;
	vec_it it;
	for (int i = 0; i < K; ++i) { 
		pair<long, long> zeros = find_longest_zeros(arr, &index);
		curr = (zeros.first + zeros.second) / 2;
		it = arr.begin() + index;
		it = arr.insert(it, curr);
	}
	sol = calc_final(it);
	return sol;
}

pair<long, long> find_longest_zeros(vector<long> arr, long *index) {
	long opt_start = arr[0], opt_finish = arr[1];
	*index = 1;
	long prev = arr[0];
	for(long i = 1, len = arr.size(); i < len; ++i) {
		if(arr[i] - prev > opt_finish - opt_start) {
			opt_finish = arr[i] ;
			opt_start = prev;
			*index = i;
		}
		prev = arr[i];
	}
	return pair<long, long>(opt_start + 1, opt_finish - 1);
}

pair<long, long> calc_final(vec_it it) {
	vec_it prev = it - 1;
	vec_it next = it + 1;
	long Ls = *it - *prev - 1;
	long Rs = *next - *it - 1;
	return pair<long, long>(max(Ls, Rs), min(Ls, Rs));
}

pair<long,long> solve_C_2(long N, long K) {
	int n0 = ceil(double(log2( double(double(K+1)/2) )) );
	long R = long(pow(2, n0+1)) - 1;
	if(R >= N)
		return pair<long,long>(0, 0);
	long num = long(( N - R ) / ( R + 1 ));
	// cout << "K: " << K << endl;
	// cout << "N: " << N << endl;
	// cout << "n0: " << n0 << endl;
	// cout << "R: " << R << endl;
	// cout << "num: " << num << end;
	return pair<long,long>(num, num);
}

pair<long,long> solve_C_3(long N, long K) {
	mypq_type q;
	q.push(pair<long, long>(0, N-1));
	while(!q.empty()) {
		pair<long,long> intr = q.top();
		q.pop();
		// cout << "K: " << K << endl;
		// cout << "intr.first: " << intr.first << endl;
		// cout << "intr.second: " << intr.second << endl;
		// cout << "gap: " << intr.second - intr.first << endl;
		long mid = (intr.second + intr.first) / 2;
		if(intr.first < mid)
			q.push(pair<long, long>(intr.first, mid - 1));
		if(mid < intr.second)
			q.push(pair<long, long>(mid + 1, intr.second));
		K -= 1;
		if (K == 0) {
			long Ls = mid - intr.first;
			long Rs = intr.second - mid;
			return pair<long, long>(max(Rs, Ls), min(Rs, Ls));
		}
	}
	return pair<long, long>(0, 0);
}


// pair<long, long> solve_C_aux(long left, long right, long &K) {
	// if(left > right)
		// return;
	// K--;
	// long mid = (left + right) / 2;
	
	// if(K == 0) {
		// long Ls = mid - left;
		// long Rs = right - mid;
		// sol = pair<long, long>(max(Ls, Rs), min(Ls, Rs));
		// return;
	// }
	
	// solve_C_aux(left, mid - 1, K);
	// solve_C_aux(mid + 1, right, K);
// }