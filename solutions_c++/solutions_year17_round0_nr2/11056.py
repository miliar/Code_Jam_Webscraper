/*
#include <bits/stdc++.h>

using namespace std;
inline bool checkDecreasing(string s) {
	int prev;
	prev=s[0];
	for(int i=0; i<s.length(); i++) {
		if(s[i]<prev) return false;
		prev=s[i];
	}
	return true;
}
void decrement(string &s, int index) {
	int ds=s[i]-'0';
	if(ds>1) {
		ds--;
		s[i]=ds+'0';
	}


}
int main() {
	int t; cin>>t;
	for(int i=0; i<t; i++) {
		long long n; cin>>n;
		string s = to_string(n);
		vector<long long> numbers;
		for(int j=0; j<s.length(); j++) {
			numbers.push_back(s[j]-'0');
		}
		for(int j=0; j<numbers.size(); j++) {
			if(numbers[j]==min_element(numbers.begin()+j, numbers.end())) {
				//all done
			} else 
		}
	}
}

*/

#include <bits/stdc++.h>

using namespace std;
inline bool checkDecreasing(string s) {
	int prev;
	prev=s[0];
	for(int i=0; i<s.length(); i++) {
		if(s[i]<prev) return false;
		prev=s[i];
	}
	return true;
}

int main() {
	int t; cin>>t;
	for(int i=0; i<t; i++) {
		long long n; cin>>n;
		string s = to_string(n);

		do {
			if(checkDecreasing(to_string(n))) {
				cout<<"Case #"<<i+1<<": "<<n<<endl;
				break;
			}
		} while(n--);
	}


};
