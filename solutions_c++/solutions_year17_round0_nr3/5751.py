#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.in","r",stdin);
    freopen("gc_out5.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
	    int n,k;
	    cin >> n >> k;
	    vector<int> v;
	    v.push_back(n);
	    for (int j = 0; j < k-1; j++){
	        sort(v.begin(),v.end());
	        int big = v[v.size()-1];
	        v[v.size()-1] = big/2;
	        v.push_back((big-1)/2);
	    }
	    sort(v.begin(),v.end());
	    int big = v[v.size()-1];
	    cout << "Case #" << i << ": " << big-((big+1)/2) << " " << (big-1)/2 << "\n";
	}
}
