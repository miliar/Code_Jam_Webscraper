#include <iostream>
using namespace std;
int main(){
	int zes;
	cin>>zes;
	for(int i = 1; i <= zes; i++){
		string s;
		cin>>s;
		int n = s.length();
		short T[n];
		for(int i = 0; i < n; i++){
			T[i] = (short)(s[i] - '0');
		}
		
		int last = 0;
		int it = 0;
		while(it != n){
			if(T[last] == T[it]){
				it++;
				continue;
			}
			if(T[last] < T[it]){
				last = it;
				it++;
				continue;
			}
			if(T[last] > T[it]){
				T[last] -= 1;
				for(int i = last + 1; i < n; i++){
					T[i] = 9;
				}
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		for(int i = 0; i < n; i++){	
		if(i != 0 || T[i] != 0)
			cout<<T[i];
		}
		cout<<endl;
	}
}
