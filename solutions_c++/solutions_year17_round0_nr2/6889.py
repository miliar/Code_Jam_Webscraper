#include<iostream>
using namespace std;
int main()
{
	int t,i;
	long long int l,c,x;
	cin>>t;
	for( i=1; i<=t; ++i ){
		cin >> l;
		for( ; l>0 ; --l){
			for( c=l, x=(c%10); c>0; c/=10 )
				if ( x<(c%10) )
					break;
				else
					x=c%10;
			if( c == 0)
				break;
		}
			cout<<"Case #"<<i<<": "<<l<<endl;
	}
	return 0;
}
				
