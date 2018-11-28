#include <bits/stdc++.h>

using namespace std;
typedef long long LL;
int ntest;
string s;

void solve(int test){	
	cout << "Case #" << test+1 << ": ";
	
	cin.ignore();
	
	cin >> s;	
	while(true){	
		bool flag = false;
		for(int i=1; s[i]; i++){
			if( s[i] < s[i-1] ){		
				s[i-1]--;
				for(int j=i; s[j]; j++) s[j] = '9';
				flag=true;
			}				
		}
		if(!flag) break;
	}
	cout << strtoll( s.c_str() ,NULL, 10) << endl;
}


int main(){
	freopen("B-large.in","r",stdin);
	freopen("test.out","w",stdout);	
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
