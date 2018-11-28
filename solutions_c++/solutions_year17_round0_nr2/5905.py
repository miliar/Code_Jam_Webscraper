#include <bits/stdc++.h>

using namespace std;

int t;
string s;
ofstream haha;

int main()
{
	//haha.open("b-small.out");
	haha.open("b-large.out");
	cin >> t;
	for(int tc=1;tc<=t;tc++)
	{
		cin >> s;
		string stemp = "0";
		stemp+=s;
		s=stemp;
		int len = s.length();
		int pos,rem;
		char num;
		bool stat = false;
		for(int i=1;i<len;i++) {
			if(s[i-1]>s[i]) {
				rem = i-1;
				num = s[i-1];
				stat = true;
				break;
			}
		}
		
		if(stat) {
			pos = rem;
			while(pos>0&&s[pos]==num) {
				pos--;
			}
			pos++;
			s[pos]--;
			for(int i=pos+1;i<len;i++) s[i] = '9';
		}
		haha << "Case #" << tc << ": ";
		pos = 0;
		while(s[pos]=='0') pos++;
		for(int i=pos;i<len;i++) haha << s[i];
		haha << "\n";
	}
	haha.close();
	return 0;
}