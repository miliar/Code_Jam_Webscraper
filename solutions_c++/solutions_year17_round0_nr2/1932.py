#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int tc; cin >>tc;
	for(int j=1;j<=tc;j++){
		string st; cin >>st;
		int len=st.length();
		int index=0;
		while(1){
			if(index==st.length()-1){
				break;
			}
			if(st[index+1] < st[index]){
				break;
			}
			index++;
		}
		if(index < st.length()-1){
			while(st[index]==st[index-1]){
				index--;
			}
			st[index]--;
		}
		for(int i=index+1;i<st.length();i++){
			st[i]='9';
		}

		cout <<"Case #"<<j<<": ";
		int ze=0;
		while(st[ze]=='0'){
			ze++;
		}
		for(int i=ze;i<st.length();i++){
			cout << st[i];
		}
		cout << endl;
		}


	return 0;
}
