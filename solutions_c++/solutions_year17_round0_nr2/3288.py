#include<iostream>
#include<math.h>
using namespace std;

bool isTidy(long long n){
	int a = n / 1000;
	int b = (n / 100) % 10;
	int c = (n / 10) % 10;
	int d = n % 10;
	if(a > b || b > c || c > d)return false;
	else return true;
}

long long help(long long n){
	if(n < 10)return n;
	int a[20];
	for(int i = 0; i < 20; i ++){
		a[i] = (n % (long long)(pow(10, i + 1))) / (long long)pow(10, i);
		//cout << a[i] << endl;
	}
	
	int t = 19;
	while(a[t] == 0)t --;
	
	int i = t;
	while(i > 0 && a[i] <= a[i - 1])i --;
	if(i == 0)return n;
	int sindex;
	for(int j = i; j <= t; j ++){
		if(a[j] > a[j - 1]){
			a[j] --;
			sindex = j;
		}
	}
	for(int j = sindex - 1; j >= 0; j --)a[j] = 9;
	
	long long ans = 0;
	for(int j = 0; j <= t; j ++)ans += a[j] * (long long)pow(10, j);
	
	return ans;
}

int main(){
	int t;
	cin >> t;
	long long n;
	//cout << help(440) << endl;
	
	for(int it = 0; it < t; it ++){
		cin >> n;
		//int origin = n;
		//if(it == 3)cout << n << endl;
		
		long long ans = help(n);
		
		/*cout << ans << " ";
		while(n > 0){
			if(isTidy(n)){
				cout << n << endl;
				break;
			}
			else n --;
		}
		if(ans != n)cout << origin << "!!!" << endl;
		*/
		cout << "Case #" << it + 1 << ": " << ans << endl;
		
		
	}
	return 0;
} 
