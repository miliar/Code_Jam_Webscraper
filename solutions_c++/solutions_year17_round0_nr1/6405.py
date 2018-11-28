#include<iostream>
#include<vector>
using namespace std;

int main() {
	int number_of_tests;
	cin>>number_of_tests;
	for(int test=1;test<=number_of_tests;test++) {
		string s;
		int minimum_flips;
		bool flip = false;
		int final_count = 0;
		unsigned int i=0;
		cin>>s>>minimum_flips;
		vector < bool > change_state(s.size(),false);
		for(i=0;i<s.size();i++) {
			if(change_state[i])
				flip=!flip;
			if(flip) {
				s[i]=(s[i]=='-'?'+':'-');
			}
			if(s[i]=='-' && i+minimum_flips<=s.size()) {
				flip = !flip;
				if(i+minimum_flips<s.size())
					change_state[i+minimum_flips]=true;
				s[i]='+';
				final_count++;
			}
		}
		cout<<"Case #"<<test<<": ";
		if(s.find('-')!=string::npos)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<final_count<<"\n";
	}
	return 0;
}
