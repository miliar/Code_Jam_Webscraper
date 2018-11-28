#include <iostream>
#include <string>
using namespace std;

void func(){
	char a = getchar(), b = getchar();
	bool first = true;
	if (b == 10){
		cout << a-'0';
		return;
	}
	int count = 0;
	while (a <= b){
		if (a == b) count++;
		else{
			for (int i=0; i<count; i++) cout << a-'0';
			count = 0;
			cout << a-'0';
			first = false;
		}
		a = b;
		b = getchar();
		if (b == 10){
			cout << a-'0';
			for (int i=0; i<count; i++) cout << a-'0';
			return;
		}
	}
	if (first && a == '1'){}
	else cout << a-'0'-1;
	for (int i=0; i<count; i++) cout << "9";
	while (b != 10){
		cout << "9";
		b = getchar();
	}
	return;
}

int main(){
	int T; cin >> T;
	getchar();
	for (int i=0; i<T; i++){
		cout << "Case #" << i+1 << ": "; 
		func();
		cout << endl;
	}
}