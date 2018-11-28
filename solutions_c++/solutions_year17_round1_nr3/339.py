#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int T;

int Hd,Ad,Hk,Ak,B,D;

int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.txt","w",stdout);
	cin >> T;
	int cas = 0;
	
	while(T--){
		int ans = 1e9;
		cas++;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		for(int i = 0;i <= 100;i++){
			for(int j = 0;j <= 100;j++){
				int hd = Hd,ad = Ad,hk = Hk,ak = Ak,b = B,d = D;
				int n1 = i;
				int n2 = j;
				int pre = -1;
				int T = 0;
				bool flag = true;
				while(hk > 0 && hd > 0){
					T++;
					//if(i == 1 && j == 1) cout << T << endl,cout << pre << endl;
					//if(i == 1 && j == 1) cout << hk << " " << hd << endl;
					if(hk <= ad){
						hk -= ad;
						pre = 0;
						break;
					}
					if((n1 == 0 && hd <= ak) || (n1 > 0 && hd <= ak - d)){
						hd = Hd;
						if(pre == 2){
							flag = false;
							break;
						}else{
							pre = 2;
						}
					}else{
						if(n1 > 0){
							ak -= d;
							pre = 3;
							if(ak < 0) ak = 0;
							n1--;
						}else{
							if(n2 > 0){
								ad += b;
								pre = 1;
								n2--;
							}else{
								hk -= ad;
								pre = 0;
								if(hk <= 0) break;
							}
						}
					}
					hd -= ak;
					if(hd <= 0){
						flag = false;
						break;
					}
					//if(i == 1 && j == 1) cout << T << endl,cout << pre << endl;
					//if(i == 1 && j == 1) cout << hk << " " << hd << endl;
					//if(i == 0 && j == 0) cout << T << endl;
					//cout << T << endl;
				}
				if(flag) ans = min(ans,T);		
			}
		}
		printf("Case #%d: ",cas);
		if(ans == 1e9) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
