/*input

*/
#include <iostream>
using namespace std;

int main() {
	int t,K;
	string s;
	cin>>t;
	for(int itr=1; itr<=t; ++itr){

		cin>>s>>K;
		cout<<"Case #"<<itr<<": ";
		int len = s.length();
		int min=-1, max=-1;
		int count = 0;
		bool check = false;
		for(int i=0; i<len;++i ) {
			if(s[i]=='-') {
				if(len - i < K) {
					// cout<<"  I ndex "<<i<<"  ";
					check = true;
					break;
				}
				// cout<<"  Index+ "<<i<<"  ";
				for(int j=i; j<i+K; ++j) {
					if(s[j]=='-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				++count;	
			}
		}
		if(check)
			cout<<"IMPOSSIBLE";
		else cout<<count;
		cout<<endl;
	}
}