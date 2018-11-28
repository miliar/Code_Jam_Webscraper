#include <iostream>
using namespace std;

int T;

int main(){
	char str[20];
	cin>>T;
	for(int cs = 1; cs <= T; ++cs){
		int i;
		char* res;
		cin>>str;
		for(i = 1; str[i]; ++i){
			if (str[i] < str[i-1]){
				while(i-2 >=0 && str[i-1] == str[i-2])
					--i;
				--str[i-1];
				break;
			}
		}
		while(str[i])
			str[i++] = '9';
		res = str;
		while(res[0] == '0')
			++res;
		if(!res[0])
			--res;
		cout<<"Case #"<<cs<<": "<<res<<endl;
	}
	return 0;
}
