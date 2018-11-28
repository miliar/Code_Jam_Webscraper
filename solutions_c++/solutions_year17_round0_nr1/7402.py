#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int testCases;
	cin>>testCases;
	for (int tc=1; tc<=testCases; tc++) {
		string panS;
		bool possible = true;
		int k, flips=0, cnt1, cnt2;
		cin>>panS>>k;
		for(cnt1=0; cnt1<=(panS.length()-k); cnt1++){
			if(panS[cnt1]=='-'){
				flips++;
				for(cnt2=cnt1; cnt2<cnt1+k; cnt2++){
					if(panS[cnt2]=='-'){
						panS[cnt2]='+';
					}
					else{
						panS[cnt2]='-';
					}
				}
			}
		}
		for(; cnt1<panS.length(); cnt1++){
			if(panS[cnt1]=='-'){
				possible = false;
				break;
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(!possible){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<flips<<endl;
		}
	}
	return 0;
}