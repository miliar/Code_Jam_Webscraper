#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int, int> mii;
typedef map<string, int> msi;

#define zero(arr) memset((arr), 0, sizeof (arr))
#define init(arr) memset((arr), -1, sizeof (arr))

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	
	cin>>t;
	
	for(int cs = 1; cs <= t; cs++) {
		string s;
		cin>>s;
		
		int size = s.length();
		
		
		for(int i = size-2; i >= 0; i--) {
			if(s[i+1] < s[i]) {
				s[i] = s[i] - 1;
				for(int j = i+1; j < size; j++)
					s[j] = '9';
			}
			
		}
		//cout<<s<<endl;
		int st = 0;
		while(st < size && s[st] == '0') st++;

		cout<<"Case #"<<cs<<": ";
		
		if(st == size)
			cout<<0;
		else {
			for(int i = st; i < size; i++)
				cout<<s[i];
		}
		
		cout<<endl;
		
	}
		
	return 0;
}

