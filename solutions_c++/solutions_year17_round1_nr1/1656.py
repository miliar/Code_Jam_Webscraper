#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int t,r,c,x,y;
	string tmp;
	cin >> t;
	for(int i=1;i<=t; ++i){
		cin >> r >> c;
		vector<string> v,ans;
		for(int j=0;j<r;j++){
			cin >>tmp;
			v.push_back(tmp);
		}
		string p;
		for(int j=0;j<c;j++){
			p+='?';
		}
		x = 0;
		while(1){
			if(v[x]!=p)break;
			x+=1;
		}
		for(int j=x;j<r;j++){
			if(v[j]==p){
				ans.push_back(ans[j-x-1]);
			}else{
				string q;
				y = 0;
				while(1){
					if(v[j][y]!='?')break;
					y+=1;
				}
				for(int l=0;l<=y;l++){
					q.push_back(v[j][y]);
				}
				for(int l=y+1;l<c;l++){
					if(v[j][l]!='?'){
						q.push_back(v[j][l]);
					}else{
						q.push_back(q[l-1]);
					}
				}
				ans.push_back(q);
			}
		}
		cout << "Case #" << i << ":" <<endl;
		for(int i=0;i<=x;i++){
			cout << ans[0] <<endl;
		}
		for(int i=1;i<ans.size();i++){
			cout << ans[i] <<endl;
		}
	}
	return 0;
}