#include<bits/stdc++.h>
using namespace std;
#define ll long long
string str;
ll n,k;
bool rec2(ll mask)
{
	ll i,j;
	string str2;
	str2 = str;
	for(i = 0;i < n;i++){
		if(mask&(1<<i)){
			if(i+k-1 >= n){
				return false;
			}
			for(j = 0;j < k;j++){
				if(str2[i+j] == '+'){
					str2[i+j] = '-';
				}
				else{
					str2[i+j] = '+';
				}
			}
		}
	}
	for(i = 0;i < n;i++){
		if(str2[i] == '-'){
			return false;
		}
	}
	return true;
}
bool rec(ll id)
{
	ll i,j,cnt;
	for(i = 0;i < (1<<n) ; i++){
		cnt = 0;
		for(j = 0;j < n;j++){
			if(i&(1<<j)){
				cnt++;
			}
		}
		if(cnt == id){
			if(rec2(i)){
				return true;
			}
		}
	}
	return false;
}
int main()
{
	ll i,j,l,m,t,flag;
	cin >> t;
	for(j = 1;j <= t;j++){
		cin >> str >> k;
		cout << "Case #" << j << ": ";
		n = str.length();
//		cout << str << endl;
		flag = 0;
		for(i = 0;i <= n;i++){
			if(rec(i)){
				flag = 1;
				break;
			}
		}
		if(flag == 0){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			cout << i << endl;
		}
	}
}

