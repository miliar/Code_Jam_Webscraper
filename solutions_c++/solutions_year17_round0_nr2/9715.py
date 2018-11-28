#include <iostream>
#include <fstream>
using namespace std;

int isTidy(long long a){
	int lD, pD;
	lD = a % 10;
	a = a/10;
	while(a > 0){
		pD = a % 10;
		if(pD > lD){
			return 0;
		}
		lD = pD;
		a = a/10;
	}	
	return 1;
}

int main(){
	ifstream f("file.in");
	int t, t2 = 1;
	long long n;
	//f >> t;
	cin >> t;
	while(t > 0){
		//f>> n;
		cin >> n;
		while(isTidy(n--) == 0){
			continue;
		}
		cout << "Case #" << t2 << ": " << (n+1) << "\n";
        t2++;
		t--;
	}
}
