#include <bits/stdc++.h>

using namespace std;

int main() {
	stack<int> st;
	long long n, tst;
	cin>>tst;
	for (int t = 0; t < tst; t++) {
		cin>>n;
		int x, last = 9;
		bool lzero = false;
		while (n){
			x = n%10;
			n = n/10;
			if ((x && lzero) || x > last) {
				x--;
				st.top() = 9;
				lzero = false;
			}
			else if (!x) {
				lzero = true;
				x = 9;
			}
		
			last = x;
			st.push(x);
		}
	
		string s;
		while (!st.empty()) {
			x = st.top();
			st.pop();
			if(x)
				s += x + '0';
		}
		int len = s.size();
		bool nine = false;
		for(int i = 0; i < len; i++) {
			if (s[i] == '9')
				nine = true;
			else if (nine)
				s[i] = '9';
		}
	
		cout<<"Case #"<<t+1<<": "<<s<<endl;
	}

	return 0;

}

