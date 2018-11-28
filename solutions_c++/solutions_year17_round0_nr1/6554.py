/*
	Copyright: razouq (c)
	Author: Anass BENDARSI
	Date: 08/04/2017 13:39:38
	flamers will **** you
*/
#include<bits/stdc++.h>
//#include<flamers.h>
#define ull unsigned long long
using namespace std;

int main(){
	freopen ("A-large.in","r",stdin);
	freopen ("myfile2.txt","w",stdout);
	string tt;
	int t;
	getline(cin,tt);
	t = stoi(tt);

	for(int m = 1; m <= t; m++){
		bool flag = true;
		string str;
		int k, c = 0;
		cin>>str;
		cin>>k;
		int n = str.size();
//		cout<<n<<"      "<<k<<endl;
		
		for(int i = 0; i < n-k+1; i++){
			if(str[i] == '-'){
//				cout<<"here"<<endl;
				c++;
				for(int j = 0; j < k; j++){
					if(str[j+i] == '-') str[j+i] = '+';
					else str[j+i] = '-';
				}
			}
		}
//		cout<<" cccccccc "<<c<<endl;
		int d = 0;
		if(n-k > 0) d = n-k;
		for(int i = n-k; i < n; i++){
			if(str[i] == '-') {
				flag = false;
				break;
			}
		}
		if(flag) cout<<"Case #"<<m<<": "<<c<<endl;
		else cout<<"Case #"<<m<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}

