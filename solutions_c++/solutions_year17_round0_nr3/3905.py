#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;




void testcase(int tcn){
	int n, k;
	cin >> n >> k;
	
	priority_queue<int, vector<int>, less<int> > q;

	q.push(n);
	int lst, a, b;
	REP(i, k){
		lst = q.top();
//		cerr << lst << endl;
		q.pop();
		a = (lst-1)/2, b = lst-1 -a;
		q.push(a); q.push(b);
	}

	cout << "Case #"<<tcn<<": "<< b <<" " << a << endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}