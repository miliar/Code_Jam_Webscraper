#include <iostream>
#include <string>

using namespace std;

string strMinOne(char x){
	if(x == '1') return "0";
	else if(x == '2') return "1";
	else if(x == '3') return "2";
	else if(x == '4') return "3";
	else if(x == '5') return "4";
	else if(x == '6') return "5";
	else if(x == '7') return "6";
	else if(x == '8') return "7";
	else return "8";
}

int main(){
	int T;
	string s;
	cin>>T;
	for(int i=0; i<T; i++){
		cin>>s;
		char lastCC;
		int firstOne = -1;
		string result = "";
		bool same = true;
		char sameNum = '0';
		for(int j=0; j<s.length(); j++){
			if(firstOne == -1 && s[j] == '1'){
				firstOne = j;
			}

			if(j > 0){
				lastCC = s[j-1];
				sameNum = lastCC;

				//case XXXXXXX1000 when X <= 1
				if(same && sameNum > s[j]){
					if(sameNum > '1')
						result += strMinOne(sameNum);

					for(int k=0; k<s.length()-1; k++){
						result += "9";
					}
					break;
				} else{
					if(lastCC == '1' && s[j] == '0'){
						result = s.substr(0, j-1);
						for(int k=0; k<s.length()-j; k++){
							result += "9";
						}
						break;
					} else if(lastCC != '1' && lastCC > s[j]){
						result = s.substr(0, j-1);
						result += strMinOne(lastCC);
						for(int k=0; k<s.length()-j; k++){
							result += "9";
						}
						break;
					}
				}

				if(lastCC != s[j]){
					same = false;
				}
			}
		}

		cout<<"Case #"<<(i+1)<<": ";
		if(s.length() == 1){
			cout<<s<<endl;
		} else if(result != ""){
			cout<<result<<endl;
		} else{
			cout<<s<<endl;
		}
	}
	return 0;
}