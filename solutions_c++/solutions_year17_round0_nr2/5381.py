#include <iostream>
#include <string>

using namespace std;

string str;

int check(){
	int size = str.size();
	for(int i =size-1; i>0; i--){
		if( str[i-1] > str[i] ){
			//cout << i << endl;
			return i;
		}
	}
	return -1;
}

void solve(){
	int size = str.size();
	int cnt = size-1;
	while( 1 ){
		int p = check();
		if( p == -1 ) break;
		str[cnt] = '9';
		str[cnt-1]--;
		cnt--;
	}
	bool sw = 0;
	for(int i = 0; i < size; i++){
		if( sw ) cout << str[i];
		else{
			if( str[i] >= '1' ){
				cout << str[i];
				sw = 1;
			}
		}
	}
	cout << endl;
}

int main(){
	//freopen("B-large.in", "rt", stdin);
	//freopen("output", "wt", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cin >> str;
		cout << "Case #" << i+1 << ": ";

		solve();
	}

	return 0;
}