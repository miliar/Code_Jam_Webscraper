#include <iostream>
#include <string>
#include <fstream>
#define endl '\n'
#define jizz cin.tie(0);ios_base::sync_with_stdio(0);
using namespace std;
ofstream file("0.txt");
struct Ken{
	int val,pos;
};
int main(){jizz
	int T,t = 0;cin >> T;
	while(T--){
		string s;cin >> s;
		bool flag = 1;
		while(flag){
			flag = 0;
			Ken tmp = (Ken){s[0] - '0',0};
			for(int i = 1; i < s.length() ; i++){
				if(s[i] - '0' < tmp.val){
					flag = 1;
					break;
				}
				tmp.val = s[i]-'0';
				tmp.pos = i;
			}
			if(flag){
				for(int i = tmp.pos+1 ; i < s.length() ; i++){
					s[i] = '9';
				}
				s[tmp.pos] = (char)(s[tmp.pos] - '0' - 1 + '0');
			}
		}
		file << "Case #"<<++t << ": ";
		if(s[0] != '0')file << s[0];
		for(int i = 1; i < s.length() ; i++){
			file << s[i];
		}file << endl;	
	} 
}