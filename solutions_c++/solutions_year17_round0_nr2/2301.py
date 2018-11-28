#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>

using namespace std;

int t;
string s;

void read_input(){
    cin >> t;
    for(int i = 0 ; i  < t; ++i){
	cin >> s;

	int lastPos = s.size() ;
	for(int j = 1 ; j < s.size() ; ++j){
	    int k = j;
	    while(k>0 && s[k] < s[k-1]){
		//cout << k << endl;
		s[k-1]--;
		lastPos = k  ;
		--k;
	    }
	    if(k != j)
		break;
	}
	cout << "Case #" << i+1 << ": "; 
	if(s[0] == '0'){
	    for(int j = 0 ; j < s.size()-1;++j)
		cout << "9";
	}
	else{
	    for(int j = 0 ; j < lastPos ; ++j)
		cout << s[j];
	    for(int j = lastPos ; j < s.size() ; ++j)
		cout << "9";
	}
	cout << endl;
    }
}

int main(){
    read_input();
    return 0;
}
