#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int sum = '+'+'-',k;
	string s;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> s >> k;
		int i,res = 0;
		for (i=0;i<s.length()-k+1;i++)
			if (s[i]=='-'){
				res++;
				for (int j=i;j<i+k;j++)
					s[j] = sum-s[j];
			}
		bool find = false;
		for (;i<s.length();i++)
			if (s[i]=='-'){
				find = true;
				break;
			}
		cout << "Case #" << tc << ": ";
		if (!find) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;

	}

	return 0;
}