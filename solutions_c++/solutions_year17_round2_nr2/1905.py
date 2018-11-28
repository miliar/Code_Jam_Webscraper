#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B_small2","w",stdout);


	int t;
	cin >> t;
	for(int p=1;p<=t;p++){
		int n,r,o,y,g,b,v;
 		vector<char> col;
 		col.push_back('R');
 		col.push_back('Y');
 		col.push_back('B');
 		vector<int> num;
		cin >> n >> r >> o >> y >> g >> b >> v;
		num.push_back(r);
		num.push_back(y);
		num.push_back(b);

		char a[n];
		memset(a,'w',sizeof(a));
		for(int i=0;i<3;i++){
			for(int j=1;j<3;j++){
				if(num[j]<num[j-1]){
					swap(num[j],num[j-1]);
					swap(col[j],col[j-1]);
				}
			}
		}
		if(num[2]>n/2){
			cout << "Case #" << p << ": IMPOSSIBLE" << endl;
		}
		else{
			int bp = -1;
			for(int i=0;i<n;i+=2){
				a[i] = col[2];
				num[2]--;
				if(num[2]==0){
					bp = i;
					break;
				}
			}
			int rem = n-bp-1;
			//cout << num[1] << " " << num[0] << endl;
			if(rem%2==0){
				if(num[0]<rem/2){
					cout << "Case #" << p << ": IMPOSSIBLE" << endl;
				}
				else{
					for(int i=bp+1;i<n;i+=2){
						a[i] = col[0];
						num[0]--;
					}
					for(int i=bp+2;i<n;i+=2){
						a[i] = col[1];
						num[1]--;
					}
					string ans = "";
					for(int i=0;i<n;i++){
						if(a[i]=='w'){
							if(num[0]==0){
								ans = ans + col[1];
							}
							else{
								ans = ans + col[0];
								num[0]--;
							}
						}
						else{
							ans = ans + a[i];
						}
					}
					cout << "Case #" << p << ": " << ans << endl;
				}
				 
			}
			else{
				if(num[0]>=rem/2){
					for(int i=bp+1;i<n;i+=2){
						a[i] = col[1];
						num[1]--;
					}
					for(int i=bp+2;i<n;i+=2){
						a[i] = col[0];
						num[0]--;
					}
					string ans = "";
					for(int i=0;i<n;i++){
						if(a[i]=='w'){
							if(num[0]==0){
								ans = ans + col[1];
							}
							else{
								ans = ans + col[0];
								num[0]--;
							}
						}
						else{
							ans = ans + a[i];
						}
					}
					cout << "Case #" << p << ": " << ans << endl;
				}
				else{
					cout << "Case #" << p << ": IMPOSSIBLE" << endl;
				}
			}

		}




		//cout << "Case #" << p << ": " << fixed << aux_ans << endl;

	}

	return 0;
}