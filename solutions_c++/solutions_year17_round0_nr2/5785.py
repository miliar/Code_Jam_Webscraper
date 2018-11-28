#include <iostream>
using namespace std;

#define LL long long
#define IKUZO ios_base::sync_with_stdio(0);cin.tie(NULL)

int tt;
LL x;

LL rek(LL a){
	//cout << a << endl;
	if(a < 10) return a;
	if ((a%10 < (a/10)%10) || (a%10==0 && (a/10)%10 == 0)) {
		//cout << a/10 - 1 << endl;
		a = rek(a/10 - 1);
		a = a*10 + 9;
	} else {
		LL temp = rek(a/10);
		//cout << temp << endl;
		if(temp != a/10){
			a = temp*10 + 9;
		} else {
			a = temp*10 + a%10;
			//cout << a << endl;
		}
	}
	return a;
}

int main(){
	IKUZO;
	cin >> tt;
	for(int tc = 1; tc <= tt; tc++){
		cin >> x;
		x = rek(x);
		cout << "Case #" << tc << ": " << x << "\n";
	}
}