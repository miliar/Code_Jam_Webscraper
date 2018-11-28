#include <iostream>
#include <map>
#include <set>

using namespace std;

int main(){

	int t;
	cin>>t;

	for(int test = 1; test <= t; test++){
		long long n, k;
		cin>>n>>k;
		set<long long> q;
		set<long long> :: reverse_iterator it;
		map<long long, long long> c;
		c[n] = 1;
		q.insert(n);

		long long tot = 0;
		long long a, b;
		long long r = 0;
		while (tot < k){
			it = q.rbegin();
			n = *it;
			r = c[n];
			tot += r;
			q.erase(n);
			n--;
			a = (n+1)/2;
			b = n/2;
			c[a] += r;
			c[b] += r;
			q.insert(a);
			q.insert(b);
		}

		cout<<"Case #"<<test<<": "<<a<<" "<<b<<endl;
	}

	return 0;
}