#include <iostream>
#include <sstream>
#include <cstring>
using namespace std;

char arr[30];
int lo = 0;

void dec(int x){
	int borrow = -1;
	for(int i=x;i>=lo;i--){
		if (arr[i] == '0'){
			arr[i] = '9';
		}
		else{
			arr[i]-=1;
			borrow = 0;
			if (i==lo && arr[i]=='0'){
				lo++;
			}
		}
		if (borrow == 0) break;
	}
}

void foo(int x){
	if (x==lo){
		return;
	}
	int i;
	for(i=lo+1;i<=x;i++){
		if (arr[i]<arr[i-1]){
			break;
		}
	}
	if (i<=x){
		dec(i-1);
		for(int j=i;j<=x;j++){
			arr[j] = '9';
		}
		foo(i-1);
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	int test;
	cin>>test;
	int testnum = 0;
	stringstream ss;
	while(++testnum<=test){
		cin>>arr;
		lo = 0;
		int len = strlen(arr);
		foo(len-1);
		ss<<"Case #"<<testnum<<": "<<arr+lo<<"\n";
	}
	cout<<ss.str();
}