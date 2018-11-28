#include <bits/stdc++.h>
using namespace std;

string ull2str(unsigned long long inter){
	stringstream num_str;
	num_str << inter;
	return num_str.str();
}

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i){
		unsigned long long n;
		cin>>n;
		bool flag = true;
		while(flag){
			string s = ull2str(n);
			string s1 = s;
			sort(s1.begin(), s1.end());
			if(s1 == s){
				cout<<"Case #"<<i+1<<": "<<n<<endl;
				flag = false;
			}
			else{
				int x;
				for(int j = s.length()-1; j > 0 ; j--){
					if(s[j] == 0){
						x = s.length() - 1 - j;
					}
					if(s[j] < s[j-1]){
						x = s.length() - 1 - j;
					}
				}
				unsigned long long ten = 1;
				for(int j = 0; j < x; ++j){
					ten = ten * 10;
				}
				n = n - (n%ten+1);
			}
		}
	}
	return 0;
}