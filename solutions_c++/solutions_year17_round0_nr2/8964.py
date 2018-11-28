#include<iostream>
#include<string>
using namespace std;
int main() {
	int T;
	cin >> T;
	for(int t = 1;t<=T;t++) {
		string n;
		cin >> n;
		int length = n.length();
		string out =n;
		cout <<"Case #"<<t<<": ";
		if(length==1) {
			cout <<n<<endl;
		}
		else {
			for(int i=0;i<length-1;i++) {
				if(n[i]-n[i+1]<=0) {
					//do nothing I think.
				} else {
					int j = i;
					while(j>=0&&n[j]>n[j+1]) {
						n[j]-=1;
						--j;
					}
					for(int k=j+2;k<length;k++){
						n[k]='9';
					}
				}
			}
			cout << (n[0]<='0'?n.substr(1):n) << endl;
		}
	}
}
