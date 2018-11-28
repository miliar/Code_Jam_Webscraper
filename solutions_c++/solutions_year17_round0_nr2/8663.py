#include <bits/stdc++.h>

using namespace std;

int ns;

bool check(string s) {
	for(int i = 0; i < ns-1; ++i) {
		if(s[i] > s[i+1]) {
			return false;
		}
	}
	return true;
}

bool allonezero(string s) {
	for(int i = 0; i < ns; ++i) {
		if(s[i] != '0' && s[i] != '1') {
			return false;
		}
	}
	return true;
}

int main(void) {

	ios_base::sync_with_stdio(false);

	ifstream fin;
	fin.open("B-small-attempt1.in");

	ofstream fout;
	fout.open("output.out");

	int t;
	fin>>t;
	for(int tt = 1; tt <= t; ++tt) {
		vector<char> ans;
		string s;
		fin>>s;
		ns = s.size();
		if(check(s)) {
			fout<<"Case #"<<tt<<": "<<s<<"\n";
			continue;
		}

		if(allonezero(s)) {
			//fout<<"Case #"<<tt<<": ";
			for(int i = 0; i < ns-1; ++i)
				ans.push_back('9');
			for(int i = 0; i < ans.size(); ++i)
				s[i] = ans[i];
			ns = ans.size();
			//fout<<"ans size1 "<<ns<<"\n";
			ans.clear();
			//fout<<"ans size2 "<<ans.size()<<"\n";
			fout<<"Case #"<<tt<<": ";
			for(int i = 0; i < ns; ++i)
				fout<<s[i];

			fout<<"\n";

			continue;
		}

		while(!check(s)) {
			

			for(int i = 0; i < ns-1; ++i) {
				if(s[i] <= s[i+1])	{
					ans.push_back(s[i]);
					continue;
				}
				if(s[i] == '1') {
					for(int j = i; j < ns-1; ++j)
						ans.push_back('9');
					break;
				}
				char x = '0' + (s[i] - '0' - 1);
				ans.push_back(x);

				for(int j = i; j < ns-1; ++j)
						ans.push_back('9');
				
				break;
			}
			for(int i = 0; i < ans.size(); ++i)
				s[i] = ans[i];
			ns = ans.size();
			ans.clear();
		}

		fout<<"Case #"<<tt<<": ";
		for(int i = 0; i < ns; ++i)
			fout<<s[i];

		fout<<"\n";

	}

	return 0;

}