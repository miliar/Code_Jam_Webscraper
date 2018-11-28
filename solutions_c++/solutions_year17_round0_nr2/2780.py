#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	string s;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> s;
		int k = 1;
		while(k<s.length() && s[k]>=s[k-1]) k++;
		if (k<s.length()){
			do{
				k--;
				s[k]=s[k]-1;
			}while(k>0 && s[k]<s[k-1]);
			k++;
		}
		for (;k<s.length();k++) s[k] = '9';
		k = 0;
		while(s[k]=='0') k++;
		s = s.substr(k);
		cout << "Case #" << tc << ": ";	
		cout << s << endl;

	}

	return 0;
}