#include <iostream>
#include <cstdio>
#define ull unsigned long long 
using namespace std;
bool checkinc(unsigned long long num){
	int curnum = 9;
	while(num){
		if(num%10 <= curnum) curnum = num%10;
		else return false;
		num /= 10;
	}
	return true;
}

ull getans(ull lower, ull upper){
	if(upper - lower <= 1){
		if(checkinc(upper) == true) return upper;
		if(checkinc(lower) == true) return lower;
		return 0;
	}
	if(checkinc(lower + (upper - lower)/2 + 1) == true){
		return getans(lower + (upper - lower)/2 + 1, upper);	
	}
	ull lans = getans(lower, lower + (upper - lower)/2);
	ull uans =getans(lower + (upper - lower)/2 + 1, upper);
	return lans>uans ? lans : uans;

}



int main(){
	int t; cin >> t;
	int t1 = t;
	while(t--){
		unsigned long long num;
		cin >> num;
		if(checkinc(num) == true){
			cout << "Case #"<< t1 - t << ": "<< num << endl;
			continue;
		}
		int len_num = 0;
		ull temp = num;
		while(temp){
			len_num++;
			temp /= 10;
		}
		ull ans = 0;
		for(int i = 0; i < len_num; ++i){
			ans = ans*10 + 1;
		}
		if(ans > num){
			ans = ans - ans/10 - 1;
			cout << "Case #"<< t1 - t << ": "<< ans << endl;
			continue;
		}
		ans = getans(ans, num);
		cout << "Case #"<< t1 - t << ": "<< ans << endl;
	}

}