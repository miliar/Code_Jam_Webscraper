#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
	int l = 0;
	cin>>l;
	for(int t = 1; t <= l; t++){
		string s = "";
		cin>>s;
		int k = 0;
		cin>>k;
		int cnt = 0;
		int n = s.size();
		for(int i = 0; i <= n-k; i++){
			if(s[i] == '-'){
				for(int j = 0; j < k; j++){
					if(s[i+j] == '-')
						s[i+j] = '+';
					else
						s[i+j] = '-'; 
				}
				cnt++;
			}
		}
		if(s.find('-') == string::npos)
			cout<<"Case #"<<t<<": "<<cnt<<endl;
		else
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}