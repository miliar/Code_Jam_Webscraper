# include <iostream>
# include <string.h>
using namespace std;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	
	for (int i = 1; i <= t; i++){
		string a;
		int k;
		int flips = 0;
		int flag = 0;
		cin>>a>>k;
		int l = a.size();
		for (int j = 0; j < l; j++){
			if (a[j] == '-'){
				if (l-j < k){
					flag = 1;
					break;
				}
				for (int q = j, w = k; w > 0; w--,q++){
					if (a[q] == '-'){
						a[q] = '+';
					}else{
						a[q] = '-';
					}
				}
				flips++;
			}
		}
		if (flag == 1){
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<i<<": "<<flips<<endl;
		}
	}
	return 0;
}
