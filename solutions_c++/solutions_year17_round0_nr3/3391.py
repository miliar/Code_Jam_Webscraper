#include<iostream>
#include<queue>
using namespace std;

pair<int, int> help(int n){
	int a = (n - 1) / 2;
	int b = n - 1 - a;
	return make_pair(a, b);
}

int main(){
	int t;
	cin >> t;
	int n, k;
	
	for(int it = 0; it < t; it ++){
		cin >> n >> k;
		
		
		
		cout << "Case #" << it + 1 << ": ";
		
		if(k == 1){
			cout << help(n).second << " " << help(n).first << endl;
		}
		
		else{
			priority_queue<int> q;
			q.push(n);
			for(int i = 0; i < k - 1; i ++){
				int temp = q.top();
				pair<int, int> p = help(temp);
				q.pop();
				q.push(p.first);
				q.push(p.second);
			}
			
			int r = q.top();
			cout << help(r).second << " " << help(r).first << endl;
		}
	}
	return 0;
} 
