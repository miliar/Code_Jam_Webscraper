#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>

using namespace std;

int t,k;
string s;

void read_input(){
    cin >> t;

    for(int i = 0 ; i < t; ++i){
	cin >> s >> k ;

	int res = 0 ;
	for(int i = 0 ; i <= s.size() - k ; ++i){
//	    cout << (s[i]=='-') << " ::: " ;
	    if(s[i] == '-'){
		res ++;
		for(int j = i ; j < i+k ; ++j){
		    if(s[j] == '-')
			s[j] = '+';
		    else
			s[j] = '-';
		}
//		cout <<  i << ": " << s << endl;
	    }
	}
	if(s.find("-") == string::npos)
	    cout << "Case #" << i+1 << ": " << res << endl;
	else
	    cout << "Case #" << i+1 << ": IMPOSSIBLE"<< endl;
    }
}

void calc(){
}

int main(){
    read_input();
    calc();
    return 0;
}
