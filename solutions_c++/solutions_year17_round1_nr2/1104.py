#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <climits>
#include <string>
#include <algorithm>

using namespace std;

int r[55];

void remove(vector<int> &a){
	vector<int> b;
	for(size_t i = 1; i < a.size(); i++){
		b.push_back(a[i]);
	}
	a = b;
}

bool canForm(vector<vector<int> > &a, int n){
	int mini[n], maxi[n];
	for(int i = 0; i < n; i++){
		mini[i] = ceil(((double)a[i][0])/(1.1*r[i]));
		maxi[i] = floor(((double)a[i][0])/(0.9*r[i]));
	}
	int minim = INT_MIN, maxim = INT_MAX;
	for(int i = 0; i < n; i++){
		minim = max(minim, mini[i]);
		maxim = min(maxim, maxi[i]);
	}
	if(minim > maxim){
		return false;
	}
	return true;
}

int index(vector<vector<int> > &a, int n){
	int mini[n];
	int j = 0;
	for(int i = 0; i < n; i++){
		mini[i] = ((double)a[i][0]/(1.1*r[i]));
	}
	for(int i = 1; i < n; i++){
		if(mini[j] > mini[i]){
			j = i;
		}
	}
	return j;
}

void perform(vector<vector<int> > &a, int &ans, int n){
	for(int i = 0; i < n; i++){
		if(a[i].size() == 0){
			return;
		}
	}
	if(canForm(a, n)){
		ans++;
		for(int i = 0; i < n; i++){
			remove(a[i]);
		}
	}else{
		int i = index(a, n);
		remove(a[i]);
	}
	perform(a, ans, n);
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int q = 1; q <= t; q++){
		int n,p,x;
		cin>>n>>p;
		for(int i = 0; i < n; i++){
			cin>>r[i];
		}
		vector<vector<int> >a(n);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < p; j++){
				cin>>x;
				a[i].push_back(x);
			}
			sort(a[i].begin(), a[i].end());
		}
		int ans = 0;
		perform(a, ans, n);
		cout<<"Case #"<<q<<": "<<ans<<endl;
	}
}