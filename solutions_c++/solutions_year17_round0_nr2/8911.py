#include <bits/stdc++.h>
using namespace std;

long long int n;
string good(long long int x){
	string str=""; 
	while(x){
		char ch = (x%10)+'0';
		x/=10;
		str+=ch;
	}
	for(int i=0;i<str.size()/2; i++)
		swap(str[i], str[str.size()-i-1]);
	bool ok = true;
	while(ok){
		ok = false;
		for(unsigned i=0;i<str.size()-1;i++){
			if(str[i]>str[i+1]){
				if(i!=0)
					ok = true;
				str[i]--;
				for(int j=i+1;j<str.size();j++)
					str[j] = '9';
				break;
			}
		}
	}
	if(str[0] == '0')
		str.erase(0,1);
	return(str);
}
int main(){
	ifstream cin("B-large.in");
	ofstream cout("output.out");
	int t;
	cin >> t;
	for(int j=0;j<t;j++){
				cin >> n;
				//for(long long int i = n; i > 0; i--){
						string abb = good(n);
								cout << "Case #" << j+1 << ": " << abb << endl;
						//		break;
						
				//}
	}
	return(0);
}
