#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool cek(int n){
string s = to_string(n);
string sx = s;
sort(s.begin(),s.end());
if(s == sx) return true;return false;
}
int main() {
	int t;
	long long n;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> n;
		bool sorted = false;
		if(n/10 == 0){
			cout <<"Case #"<<i<<": "<<n<<endl;
		}else{
			while(!sorted){
				if(!cek(n)){
					n--;
				}else sorted = true;
			}
			cout <<"Case #"<<i<<": "<<n<<endl;
		}
	}
	return 0;
}