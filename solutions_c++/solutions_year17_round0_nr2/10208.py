#include "iostream"
#include "algorithm"
#include "string"
using namespace std;

void inline resetAfter( string &s, int xt){
	for(int q=xt+1; q<s.size(); q++){
		s[q] = '9';
	}
}

int main(){

	int t,y,zs,x,i=0;
	cin>>t;
	string s,st;
	while( i++ < t ){
		cin>>s;
		cout<<"Case #"<<i<<": ";
		for( int z = s.size()-2; z >= 0; z--){
			if( s[z] > s[z+1] )
			{
				s[z] = to_string( stoi(s.substr(z,1) ) -1 )[0];
				resetAfter(s, z);
			}
		}
		x = s.find_last_of('0');
		if( x != string::npos )
			cout<<s.substr(x+1);
		else
			cout<<s;
		cout<<endl;
	}
}