#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int test;
	cin >> test;
	for(int ctr=1;ctr<=test;ctr++) {
		string in;
		int num,cnt = 0;
		cin >> in >> num;
		int start=0,len=in.size();
		while(true) {
			while(start<len and in[start]=='+') start++;
			if(start==len) break;
			if((start+num-1)>=len) {
				cout << "Case #" << ctr << ": IMPOSSIBLE\n";
				break;
			}
			for(int i=0;i<num;i++) {
				if(in[start+i]=='+') in[start+i] = '-';
				else in[start+i] = '+';
			}
			cnt++;
		}
		if(start==len) cout << "Case #" << ctr << ": " << cnt << "\n";
	}
	return 0;
}