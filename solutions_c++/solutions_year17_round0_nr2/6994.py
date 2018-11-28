#include <bits/stdc++.h>

using namespace std;


ifstream in("1.in");
ofstream out("1.out");

int n=0;
int chk( string s){
	
	
	for( int i=0;i<n-1;i++)
		if( s[i] > s[i+1] ){
			return i+1;
		
		}
	return n;
}
string fix( string s , int a){
	/*
	cout << s << " " << a << endl;
	cout << s[a-1]  << " ";
	*/
	int ab = int(s[a-1]);
	ab--;
	s[a-1] = char(ab);
	//cout << s[a-1] << endl;
	for( int i=a;i<n;i++)
		s[i] = '9';
		
	return s;
}
int main(){
	
	int test_case;
	in >> test_case;
	int cou=1;
	
	while( test_case-- > 0 ){
		string s;
		in >> s;
		int er=-4;
		n = s.size();
		while( 1 == 1 ){
	//		cout << s << " " << n << endl;
			er = chk(s);
	//		cout << er << endl;
			if( er != n && (er != 1 || ( er == 1 && s[0] != '0'  ) ) ){
				s = fix(s,er);
			}	
			else 
				break;
		}
		//Case #1: 129
		out << "Case #" << cou++ << ": ";
		bool f=1;
		for( int i=0;i<n;i++){
			if( f == 1 and s[i] == '0' ) continue;
			if( s[i] != '0' ) f=0;
			out << s[i];
		}
		
		out << endl;
		
	}
	return 0;	
}
