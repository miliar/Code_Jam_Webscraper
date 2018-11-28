#include <iostream>
using namespace std;
int main(){
	int zes;
	cin>>zes;
	for(int k = 1; k <= zes; k++){
		string s;
		int size;
		cin>>s;
		cin>>size;
		bool T[s.length()];
		for(unsigned int i = 0; i <s.length(); i++){
			T[i] = s[i] == '+';
		}
		int result = 0;
		for(int i = 0; i <= s.length() - size; i++){
			if(T[i] == 0){
				for(int j = i;j < i + size; j++){
					T[j] = ! T[j];
				}
				result++;
			}
		}
		
		
		bool ok = 1;
		for(int i = 0; i < s.length(); i++){
			if(T[i] == 0){
				ok = 0;
				break;
			}
		}
		
		cout<<"Case #"<<k<<": ";
		if(ok) cout<<result<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}
