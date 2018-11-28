#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("b.txt","w",stdout);
	int t;
	cin >> t;
	for( int i = 1; i <= t; i++ ){
		int s;
		int k;
		cin >> s >> k;
		//printf("Case #%d: ", i);
		priority_queue<int > q;
		q.push(s);
		int current;
		for( int j = 1; j <= k; j++ ){
			current = q.top();
		//	cout << current << endl;
			q.pop();
			if( current % 2 ){
			//	cout << current / 2 << " " << current / 2 << endl; 
				q.push(current / 2);
				q.push( current / 2);
			}
			else{
				//cout << current / 2 - 1 << " " << current / 2 << endl;
				q.push( current / 2 );
				q.push( current / 2 - 1);
			}
		}
		printf("Case #%d: ", i);
		if( current % 2 ){
			cout << current / 2 << " " << current / 2 << endl;
		}
		else{
			cout << current / 2 << " " << current / 2 - 1 << endl;
		}
	}
}