#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <climits>
#include <string>

using namespace std;

bool fill(string &a){
	bool ans = true;
	for(size_t i = 0; i < a.size(); i++){
		if(a[i] != '?'){
			ans = false;
			break;
		}
	}
	if(ans){
		return true;
	}
	size_t i = 0;
	while(a[i] == '?' && i < a.size()){
		i++;
	}
	string b;
	for(size_t j = 0; j < i; j++){
		b = b + a[i];
	}
	while(i < a.size()){
		if(a[i] != '?'){
			b = b + a[i];
			char c = a[i];
			i++;
			while(a[i] == '?' && i < a.size()){
				b = b + c;
				i++;
			}
		}
	}
	a = b;
	return false;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int q = 1; q <= t; q++){
		int r,c;
		cin>>r>>c;
		cout<<"Case #"<<q<<":"<<endl;
		string a[r];
		for(int i = 0; i < r; i++){
			cin>>a[i];
		}
		bool emp[r];
		for(int i = 0; i < r; i++){
			emp[i] = fill(a[i]);
		}
		int i = 0, j = 0;
		while(i < r){
			while(j < r && emp[j]){
				j++;
			}
			if(j == i){
				j++;
				i++;
				continue;
			}
			if(j == r)break;
			for(int k = i; k < j; k++){
				a[k] = a[j];
				emp[k] = true;
			}
			i = j;
			j = i;
		}
		if(i != j){
			for(int k = i; k < r; k++){
				a[k] = a[i-1];
			}
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				cout<<a[i][j];
			}
			cout<<endl;
		}
	}
}