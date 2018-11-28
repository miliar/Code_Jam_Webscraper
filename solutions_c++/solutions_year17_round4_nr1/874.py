#include <iostream>

using namespace std;

int main(){
	int testcase, number, piece, a[100], b[4]={0}, ans;
	cin >> testcase;
	for(int i=1;i<=testcase;i++){
		b[0] = b[1] = b[2] = b[3] = 0;
		cin >> number >> piece;
		for(int j=0;j<number;j++){
			cin >> a[j];
			b[a[j]%piece]++;
		}
		ans = b[0];
		if(piece==2){
			ans += (b[1]+1)/2;
		}
		else if(piece==3){
			if(b[1]<=b[2]){
				ans+=b[1]+(b[2]-b[1]+2)/3;
			}
			else{
				ans+=b[2]+(b[1]-b[2]+2)/3;
			}
		}
		else{
			if(b[1]<=b[3]){
				ans+=b[1]+(b[3]-b[1])/4;
				b[3]=(b[3]-b[1])%4;
				b[1]=0;
			}
			else{
				ans+=b[3]+(b[1]-b[3])/4;
				b[1]=(b[1]-b[3])%4;
				b[3]=0;
			}
			ans += b[2]/2;
			b[2]%=2;
			if(b[2]||b[3]||b[1])
				ans++;
			if((b[1]==3||b[3]==3)&&b[2]==1)
				ans++;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}