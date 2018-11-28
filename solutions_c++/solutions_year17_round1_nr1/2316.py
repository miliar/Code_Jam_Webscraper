#include <iostream>
#include <vector>
#include <cassert>

using namespace std;
int T,R,C;
vector< vector < char> > cake;

bool my_is_empty(int a, int b , int c , int d){
	for(int i =a ; i < b; i ++){
		for(int j = c; j < d ; j ++){
			if( cake[i][j] != '?')
				return false;
		}
	}
	return true;
}
char has_one(int a,int b, int c , int d ){
	bool one = false;
	char ch= '?';
	for(int i =a ; i < b; i ++){
		for(int j = c; j < d; j ++ ){
			if(cake[i][j] != '?' && one )
				return '?';
			
			if( cake[i][j] != '?'){
				one = true;
				ch = cake[i][j];
			}
			
		}
	}
	if( one )
		return ch;
	return '?';
}
void fill(int a, int b , int c , int d , char ch){
	for(int i =a ; i < b; i ++){
		for(int j = c; j < d ; j ++){
			cake[i][j] = ch;
		}
	}
}
void dump(int a, int b, int c, int d){
	for(int i =a ; i < b; i ++){
		for(int j = c; j < d ; j ++){
			cout << cake [i][j];
		}
		cout <<endl;
	}
}

void function(int a, int b , int c , int d){
	int i=0;
	char ch;
	//cout<<" function "  << a << " " << b << " "<< c << " " << d << endl;
	//dump(a,b,c,d);
	if((ch = has_one(a,b,c,d)) != '?' ){
		//cout << " has_onde"<<endl;
		fill(a,b,c,d,ch);
		return;
	}
	for( i = a ; i < b ; i ++){
		if (!my_is_empty(a,i,c,d) && !my_is_empty(i,b,c,d) ) {
			break;
		}
	}
	if( i < b){
		function(a,i,c,d);
		function(i,b,c,d);
		return;
	}
	i = 0 ;
	for( i = c  ; i < d; i ++){
		if(!my_is_empty(a,b,c,i) && !my_is_empty(a,b,i,d) )
			break;
	}
	if ( i < d){
		function(a,b,c,i);
		function(a,b,i,d);
		return;
	}
	//assert(false);
	
	
}

int main(){
	cin >> T;
	for(int i=0; i< T; i ++){
		cin >> R;
		cin >> C;
		cake.resize(R);
		for(int j =0; j < R; j ++){
			cake[j].resize(C);
			for(int z =0 ; z < C ; z ++){
				cin >> cake[j][z];
			}
		}
		function(0,R,0,C);
		cout<<"Case #" << i + 1 << ":"<<endl;
		for(int j =0; j < R; j ++){
			for(int z =0 ; z < C ; z ++){
				cout << cake[j][z];
			}
			cout << endl;
		}
		
	}
	return 0;
}