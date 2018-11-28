#include<iostream>
#include<vector>
using namespace std;

string calc(string& n) {
	int len = n.length();
	if (len==1) {
		return n;
	}
	vector<int> vi;
	vi.push_back(0);
	for(auto x:n) {
		vi.push_back(x-'0');
	}
	int pos = 1;
	while(pos<len+1 && vi[pos]>=vi[pos-1]) {
		pos++;
	}
	if (pos == len+1) {
		return n;
	}
	pos--;
	while(pos>0 && vi[pos]==vi[pos-1]) {
		pos--;
	}
	vi[pos]--;
	for(int i=pos+1;i<len+1;i++) {
		vi[i] = 9;
	}
	string res;
	pos = 1;
	while(pos<len+1 && vi[pos] == 0) {
		pos++;
	}
	for(int i=pos;i<len+1;i++) {
		res += '0' + vi[i];
	}
	return res;
}

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		string n;
		cin>>n;
		cout<<"Case #"<<t<<": "<<calc(n)<<endl;
	}
	return 0;
}
