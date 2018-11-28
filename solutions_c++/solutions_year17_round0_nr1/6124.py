#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<algorithm>
#include<map>
#include<string>
using namespace std;

typedef long long ll;

int main() {
	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		string s;
		cin>>s;
		int k;
		cin>>k;
		int i=0;

		//vector<int> v;
		//if(i != s.size()){
		//	char temp = s[i];
		//	int val = 0;
		//	while(i<s.size()){
		//		if(s[i] == temp){
		//			val++;
		//			i++;
		//		}
		//		else{
		//		v.push_back(val);
		//		val = 0;
		//		temp = s[i];
		//		}
		//	}

		//}

		//for(int

		int cnt = 0;
		bool np = false;	
		while(i<s.size()){
//			cout<<"start  -> "<<i<<endl<<endl;
			while(i<s.size() and s[i]=='+'){
				i++;
			}
			int j = 0;
			while(i<s.size() and s[i] == '-'){
				i++;
				j++;		
			}

			cnt += j/k;
			int ti = i;
			if(j%k!=0){
				if(i == s.size()){
					np = true;
					break;
				}
			while(i<s.size() and i<(ti + (k - j%k))){
			//	cout<<i<<"  inverted "<<s[i]<<"   ";
				s[i] = (s[i]=='-'?'+':'-');
			//	cout<<s[i]<<endl;
				
				i++;
			}
			cnt++;
			}	
			i = ti;
		}
		cout<<"Case #"<<++cas<<": ";
		if(np) cout<<"IMPOSSIBLE"<<endl;
		else cout<<cnt<<endl;
	}


return 0;
}
