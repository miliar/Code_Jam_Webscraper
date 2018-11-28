#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
#include <ctime>


typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;
using namespace std;

vector<int> cmp (vector<int> tmp1, vector<int> tmp2, int mark) {
	vector<int> tmp;
	//cout << tmp1[0] << " " << tmp1[1] << " " << tmp2[0] << "  cp " << tmp2[1] << endl;
	if (tmp1[0] == -1) {
		return tmp2;
	} 
	if (tmp2[0] == -1) {
		return tmp1;
	}

	//if (tmp1[0] != -1 && tmp2[0] != -1) {

	//}
	if (tmp1[1] < tmp2[1]) {
        tmp = tmp1;
    } else if (tmp1[1] == tmp2[1]){
    	if (tmp1[0] <= tmp2[0]) {
    		tmp = tmp1;	
    	} else {
    		tmp = tmp2;
    	}
    } else {
    	tmp = tmp2;
    }

    if (mark) {
    	if (tmp == tmp1) {
    		tmp = tmp2;
    	} 
    	if (tmp == tmp2) {
    		tmp = tmp1;
    	}
    }

    return tmp;
}

vector<int> dfs(int l, int k) {
	//cout << l << " " << k << endl;
    vector<int> res;
    if (l < k || k == 0) {
    	res.push_back(-1);
    	res.push_back(-1);
    	return res;
    }

    if (k == 1) {
        if (l % 2 == 0) {
            res.push_back(l / 2);
            res.push_back(l / 2 - 1);
        } else {
            res.push_back(l / 2);
            res.push_back(l / 2);
        }
        return res;
    }

    int left, right;
    if (l % 2 == 0) {
        left = l / 2 - 1;
        right = l / 2;
    } else {
    	left = l / 2;
    	right = l / 2;
    } 

    vector<int> tmp, tmp0, tmp1, tmp2, tmp3, tmp4;
    if (k % 2 == 0) {
        tmp1 = dfs(left, (k - 1) / 2);
        tmp2 = dfs(right, (k - 1) / 2 + 1);
        tmp3 = dfs(left, (k - 1) / 2 + 1);
        tmp4 = dfs(right, (k - 1) / 2);
        tmp = cmp(tmp1, tmp2, 0);
        tmp0 = cmp(tmp3, tmp4, 0);
        res = cmp(tmp, tmp0, 1);
        return res;
    } else {
        tmp1 = dfs(left, (k - 1) / 2);
        tmp2 = dfs(right, (k - 1) / 2);
        res = cmp(tmp1, tmp2, 1);
        return res;
    }

} 


int main() {
	
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	//freopen_s(&stream, "C-small1.in", "r", stdin);
	//freopen_s(&stream, "C-small1.out", "w", stdout);
	//freopen_s(&stream, "C-large.in", "r", stdin);
	//freopen_s(&stream, "C-large.out", "w", stdout);
	int T;
	int n, k;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n >> k;
		cout << "Case #" << (i + 1) << ": ";
		if (k >= n) {
			cout << 0 << " " << 0 << endl;
			continue;
		}
		
		vector<int> res;
		res = dfs(n, k);
		cout << res[0] << " " << res[1] << endl;
	}

	return 0;
}
