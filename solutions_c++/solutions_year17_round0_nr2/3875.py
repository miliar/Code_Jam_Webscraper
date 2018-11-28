#include <algorithm>
#include <vector>
#include <limits.h> 
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <unordered_map>
#include <queue>
#include <sstream>


using namespace std;

void slove(int t, long long n) {
	string a = to_string(n);
	a.insert(a.begin(),'0');
	int num = a.size();
	int mark = -1;
	int carry = 0;
	for(int i=num-1;i>1;i--) {
		if((a[i] - '0') + carry < (a[i-1] - '0')) {
			mark = i;
			carry = -1;
		}else {
			carry = 0;
		}
	}
	if(mark != -1) {
		a[mark-1] = a[mark-1] - 1;
		for(int i = mark;i < num; i++) a[i] = '9';
	}
	int index = 1;
	cout<<"Case #"<<t<<": ";
	for(;index<num;index++) if(a[index] != '0') break;
	for(;index<num;index++) cout<<a[index];
	cout<<endl;
}
int main(int argc, char *argv[]) {
	if(argc >= 2) {
        freopen(argv[1], "r", stdin);
    }else{
        freopen("A.in", "r", stdin);    
    }
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		long long n;
		cin>>n;
		slove(i+1,n);
	}
	return 0;
}