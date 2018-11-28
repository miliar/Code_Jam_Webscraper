#include "iostream"

using namespace std;

int main(int argc, char const *argv[])
{
	int t,k,x;
	int failed = 0;
	string s;
	cin>>t;

	for( int i =0; i<t; i++){
		cout<<"Case #"<<i+1<<": ";
		int times = 0;
		size_t sz;
		cin>>s;
		cin>>k;
		failed = 0;
		sz = s.find('-');

		//While not solved
		while( sz != string::npos){
			x = sz;
			for( int m = x; m < (x+k); m++){
				try{
					s.at(m);
					s[m] = (s[m] == '-' ? '+' : '-');
				}catch( out_of_range error){
					cout<<"IMPOSSIBLE"<<endl;
					failed = 1;
					break;
				}
			}
			if( failed )
				break;
			sz = s.find('-');
			times++;
		}

		if( failed )
			continue;

		cout<<times<<endl;


	}
	return 0;
}