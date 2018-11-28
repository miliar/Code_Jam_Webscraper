#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	int x=1;
	while(t--){
		string st;
		int k;
		cin >> st >> k;
		int S[st.size()+1];
		for (int i=0;i<=st.size();i++){
			S[i]=0;
		}
		int y=0;
		for (int i=0;i<(int)st.size()-k+1;i++){
			S[i+1]+=S[i];
			bool isTrue=true;
			if(st[i]=='-'){
				isTrue=false;
			}
			if(S[i+1]&1){
				isTrue=!isTrue;
			}
			if(!isTrue){
				y++;
				S[i+1]++;
				S[i+k+1]--;
			}
		}
		bool ans=true;
		for (int i=(int)st.size()-k+1;i<st.size();i++){
			S[i+1]+=S[i];
			bool isTrue=true;
			if(st[i]=='-'){
				isTrue=false;
			}
			if(S[i+1]&1){
				isTrue=!isTrue;
			}
			if(!isTrue){
				ans=false;
			}
		}
		if(ans){
			cout << "Case #" << x << ": " << y << endl;
		} else {
			cout << "Case #" << x << ": IMPOSSIBLE" << endl;
		}
		x++;
	}
}
