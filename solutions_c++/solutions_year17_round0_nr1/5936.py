#include <bits/stdc++.h>

using namespace std;

int t,k;
string s;

ofstream haha;

int main()
{
	//haha.open("a-small.out");
	haha.open("a-large.out");
	cin >> t;
	for(int tc=1;tc<=t;tc++) {
		cin >> s >> k;
		int ans = 0;
		int len = s.length();
		int pos = 0;
		while(pos<=len-k) {
			//cout << s << endl;
			if(s[pos]=='-') {
				ans++;
				for(int i=pos;i<pos+k;i++) {
					if(s[i]=='-') s[i] = '+';
					else s[i] = '-';
				}
			}
			pos++;
		}
		bool stat = true;
		for(int i=0;i<len;i++) {
			if(s[i]=='-') {
				stat = false;
				break;
			}
		}
		//cout << s << endl;
		haha << "Case #" << tc << ": ";
		if(stat) haha << ans << "\n";
		else haha << "IMPOSSIBLE\n";
	}
	haha.close();
	return 0;
}