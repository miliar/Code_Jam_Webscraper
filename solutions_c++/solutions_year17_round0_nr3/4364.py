#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef unsigned long long ulong;



ulong get_y(ulong n) {
    return n/2;
}

ulong get_z(ulong n) {
    if (n % 2 == 0) return n/2 - 1;
    else return n/2;
}


void gen_succ(ulong n,vector<ulong> &v, ulong &count) {
    if (n == 2) {
        v.push_back(1);
        count += 1;
    }
    else {
        if (n % 2 == 0) {
            v.push_back(n/2);
            v.push_back(n/2 - 1);
        }
        else {
            v.push_back(n/2);
            v.push_back(n/2);
        }
        count += 2;
    }
}



ulong get_kth_interval(ulong n, ulong k) {
    if (k == 1) return n;
    vector<ulong> v;
    v.push_back(n);
    ulong count_past = 1;
    ulong count_current = 0;
    while(count_past + count_current < k) {
        count_past += count_current;
        count_current = 0;
        vector<ulong> aux;
        for (int i = 0; i < v.size(); ++i) {
            gen_succ(v[i],aux,count_current);
        }
        v = aux;
    }
    sort(v.begin(), v.end(), greater<int>());
    return v[k-count_past-1]; 
}



int main() {
	int t;
    ulong n,k;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		cin >> n;
        cin >> k;
        ulong interval = get_kth_interval(n,k);
        cout << get_y(interval) << " ";
        cout << get_z(interval) << endl;
	}
}
