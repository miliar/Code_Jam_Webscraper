#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T; 
	cin>>T;
	int n=1;
	while (T--){
		cout<<"Case #"<<n++<<": ";
		string s; 
		cin>>s;
		while (true){
			int x = -1;
			for (int i=0;i<s.size()-1;i++){
				if (s[i]>s[i + 1]){
					s[i]--;
					x = i + 1;
					break;
				}
			}
			if (x == -1)
				break;
			while (x < s.size())
				s[x++] = '9';
		}
		int y = upper_bound(s.begin(), s.end(), '0') - s.begin();
		while (y < s.size())
		cout<<s[y++];
		cout<<endl;
	}
	return 0;
}