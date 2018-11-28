#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	int x=1;
	while (t--){
		string st;
		cin >> st;
		int r=-1;
		for (int i=st.size()-1;i>0;i--){
			if(st[i]<st[i-1]){
				st[i-1]=st[i-1]-1;
				r=i;
			}
		}
		cout << "Case #" << x << ": " ;
		if(r!=-1){
			for (int i=r;i<st.size();i++){
				st[i]='9';
			}
			if(st[0]=='0'){
				st=st.substr(1,st.size()-1);
			}
		}
		cout << st << endl;
		x++;
	}
}
