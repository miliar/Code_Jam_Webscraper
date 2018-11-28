#include <iostream>
using namespace std;
string work() {
	int num[22];
	string s;
	cin>>s;
	int len= s.length();
	for(int i = 0; i < s.length(); i++) {
		num[s.length() - i - 1] = s[i] - '0';
	}
	int cur = 9;                                                                                                                          
	for(int i =0; i< s.length()-1; i++){
		if(num[i] < num[i+1] || num[i] == 0) {
			if(num[i] < cur || cur < num[i+1]) {
				i = i+1;
				while(num[i] -1 < 0) {
					num[i] = cur;
					i++;
				}
				i--;
				int kk = i;
				while(num[kk] < 9 || kk >=0) {
					num[kk] = 9;
					kk--;
				}
				cur =9;
				num[i+1]--;
			}
			if(cur > num[i+1] )
				num[i] = cur;
		}
		else {
			cur = num[i];
		}
	}
	while(num[len -1] == 0) len--;
	string ans = "";
	for (int i = 0; i < len; ++i)
	{
		ans += (num[len -i-1] + '0');
	}
	return ans;
}
int main(){
	int t;
	int i=1;
	cin>>t;
	while(t){
		cout<<"Case #"<<i<<": "<<work()<<endl; 
		t--;
		i++;
	}
}