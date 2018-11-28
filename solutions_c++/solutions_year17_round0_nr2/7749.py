#include <iostream>
#include <string>
using namespace std;


int main(){
	int T = 0;
	cin >> T;
	string str;
	for(int i =0; i < T; i ++ ){
		cin >> str;
		int x = 1;
		int k = str.size();
		while(x < k){
			if(str[x-1] <= str[x]){
				x++;
			} else{
				if(str[x-1] == '0' )
					str[x-1] = '9';
				else 
					str[x-1]--;
				k = x;
				for(int j = x; j < str.size(); j ++ ){
					str[j]='9';
				}
				if(x > 1)
					x--;
			}
		}
		k =0;
		while(str[k] == '0'){
			k++;
		}
		
		cout<<"Case #" << i+1 <<": "<<str.substr(k,str.size()-k)<<endl;
	}
	return 0;
}