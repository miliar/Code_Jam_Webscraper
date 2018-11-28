#include <iostream>
#include <stack>
#include <vector>
using namespace std;
typedef long long ll;

int t;
ll n;
bool check(ll n) {
	int c = 10;
	while(n) {
		int d = n % 10;
		n /= 10;
		if(d > c)
			return 0;
		c = d;
	}
	return 1;
}

void bf(ll n) {
	while(!check(n)) {
		n--;
	}
	cout << n << '\n';
}
/**
Super dandy relaxat - viata e frumoasa
*/
ll nonBF(ll n) 
{
	if(check(n)) {
		return n;
	}
	stack<int> s;
	vector<int> a;
	ll newN = n;
	while(n) {
		int d = n % 10;
		n /= 10;
		s.push(d);
	}
	while(!s.empty()) {
		a.push_back(s.top());
		s.pop();
	}

	while(!check(newN)) {
		for(int i = a.size() - 1; i > 0; i--) {
			int nr = a[i] + 10 * a[i - 1];
			bool ok = 1;
			while(!check(nr)) {
				nr--;
				ok = 0;
			}
			if(ok == 0 /*&& i != a.size() - 1*/)
				for(int j = i; j < a.size(); j++) 
					a[j] = 9;
			a[i] = nr % 10;
			a[i - 1] = nr / 10;
		}
		newN = 0;
		for(int i = 0; i < a.size(); i++) {
			newN *= 10;
			newN += a[i];
		}
	}
	return newN;
}
int main() 
{
	freopen("f.txt","r",stdin);
	freopen("fout.txt","w",stdout);
	cin >> t;
	int c = 1,c2 = 1;
	while(t--) {
		cin >> n;
//		cout << "Case #" << c++ << ": ";
	//	bf(n);
		cout << "Case #" << c2++ << ": " << nonBF(n) << '\n';

	}

	return 0;
}