#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int test;
	cin >> test;
	for(int i=1;i<=test;i++) {
		string num;
		cin>>num;
		if(num.size()==1) cout << "Case #" << i << ": " << num << "\n";
		else {
			int len = num.size();
			string copy = num;
			int lastChecked = 0;
			while(lastChecked<len) {
				for(int j=len-1;j>=lastChecked+1;j--) {
					if(num[j]=='0' and num[j-1]=='0') {
						num[j] = '9';
					}
					else if(num[j]<num[j-1]) {
						num[j] = '9';
						num[j-1]--;
					}
				}
				for(int j=0;j<len-1;j++,lastChecked++) if(num[j]>num[j+1]) break;
			}
			if(num[0]=='0') num.erase(0,1);
			for(int j=0;j<len;j++) if(num[j]<'9') {
				num[j]++;
				if(num>copy) num[j]--;
			}
			cout << "Case #" << i << ": " << num << "\n";
		}
	}
}