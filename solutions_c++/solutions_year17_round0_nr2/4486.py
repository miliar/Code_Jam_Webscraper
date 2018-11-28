#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>

#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define F(i , a , b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define pb push_back
#define ll long long
#define E(a) cerr << #a << " = " << a << '\n'
#define X first
#define Y second
#define INF 10000000000000

const int MAX_N = 2000 + 10 , mod = 1000000007;
bool ex(string s){
	for(int i = 0 ; i<s.length() ; i++){
		if(s[i] == 'F') return true;
	}
	return false;
}

bool is_bigger(string s1, string s2){
	
	if(ex(s1) != 0) return false;
	if(ex(s2) != 0) return true;
	if(s1.length() < s2.length()) return false;
	if(s1.length() > s2.length()) return true;
	for(int i =0 ; i<s1.length() ; i++){
		if((s1[i]-'0') > (s2[i]-'0')) return true;
		else if((s1[i]-'0') < (s2[i]-'0')) return false;
	}
	return true;
}
string get(char c, int nines){
	string s = "";
	s += c;
	while(nines--) s+='9';
	return s;
}
string best(string s, int small){
	string s2 = "";
	string s1 = "0";
	s2 += s[0];
	if(s[0] == '0') return "F";
	if((s[0]-'0') < small) return "F";
	if(s.length() == 1) return s;
	if((s[0]-'0')-1 >= small){
		if(s[0] == '1') s1 = get('9' , s.length()-2);
		else s1 = get(((s[0]-'0')-1)+'0' , s.length()-1);
		
	}
	s2 += best(s.substr(1,s.length()-1) , max(small , (s[0]-'0')));
	if(is_bigger(s2,s1)) return s2;
	return s1;
}

void clr(){

}
void solve(){
	string s;
	cin >> s;
	cout << best(s , -1) << endl;
}


int32_t main(){
    
        freopen("input.txt" , "r" , stdin);
        freopen("output.txt" , "w" , stdout);
    //    cout << setprecision(10) << fixed;
    ios::sync_with_stdio(0); cin.tie() ; cout.tie();

    int T;
    cin >> T;
    for(int _ = 1 ; _ <= T ; _++){
    	clr();
    	cout << "Case #"<<_<<": ";
    	solve();
	}
        
    
    return 0;
}
