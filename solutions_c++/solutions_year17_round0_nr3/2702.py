#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
    	cout << "Case #" << i << ": ";
    	long long n, k;
    	cin >> n >> k;
    	priority_queue<long long> q;
    	q.push(n);

    	unordered_map<long long, long long> m;
    	m[n] = 1;

    	unordered_set<long long> in_queue;
    	in_queue.insert(n);

		long long tmp;
    	long long ks = 0;
    	do{
    		tmp = q.top();
    		q.pop();
    		ks += m[tmp];
    		
    		m[tmp/2] += m[tmp];
    		m[(tmp-1)/2] += m[tmp];
    		if(!in_queue.count(tmp/2)){
    			q.push(tmp/2);
    			in_queue.insert(tmp/2);
    		}
    		if(!in_queue.count((tmp-1)/2)){
    			q.push((tmp-1)/2);
    			in_queue.insert((tmp-1)/2);
    		}
    	}while(ks < k);
    	cout << tmp/2 << " " << (tmp-1)/2 << endl;
	}
    return 0;
}

