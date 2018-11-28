#include <iostream>
#include <string>
using namespace std;

int main()
{
	int N;
	cin >> N;
	for(int i=1;i<=N;i++){
		string str;
		cin >> str;
		for(int j=str.size()-2;j>=0;j--){
			if(str[j] > str[j+1]){
				str[j+1] = '9';
				for(int x=j+2;x<str.size();x++) str[x]='9';
				int k=j;
				while(k>=0){
					if(str[k]!='0'){
						str[k] = char(str[k])-1;
						break;
					}else{
						str[k]='9';
					}
					k--;
				}
			}
		}
		int zeros = 0;
		while(zeros<str.size()&&str[zeros]=='0') zeros++;
		cout << "Case #" << i << ": " << str.substr(zeros) << endl;
	}
}