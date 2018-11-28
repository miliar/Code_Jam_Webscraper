#include<iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	int k;
	string s;
	
	for(int it = 0; it < t; it ++){
		cin >> s;
		cin >> k;
		
		int n = s.length();
		bool b[n];
		for(int i = 0; i < n; i ++){
			if(s[i] == '+')b[i] = 0;
			else b[i] = 1;
		}	
		
		int count = 0;
		int index = 0;
		
		while(index <= n - k){
			while(index <= n - k && b[index] == 0)index ++;
			if(index > n - k)break;
			count ++;
			for(int i = 0; i < k; i ++)b[index + i] = 1 - b[index + i];
			index ++;
		}
		
		int label = 0;
		for(int i = index; i < n; i ++){
			if(b[i] == 1){
				label = 1;
				break;
			}
		}
		
		cout << "Case #" << it + 1 << ": ";
		
		if(label == 1){
			cout << "IMPOSSIBLE" << endl;
		}
		else cout << count << endl;
	}
	return 0;
} 
