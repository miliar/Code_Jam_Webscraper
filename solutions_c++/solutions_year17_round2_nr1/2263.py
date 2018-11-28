#include <vector>
#include <sstream>
#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cstdio>
#include <limits>
using namespace std;


void main2(){
	long long D,N;
	cin>>D>>N;
    vector<long long> K(N), S(N);
    for(int n=0;n<N;n++){
        cin>>K[n]>>S[n];
    }
    int last_arrival=0;
	for(int n=1;n<N;n++){
        if( (D-K[n])*S[last_arrival] > (D-K[last_arrival])*S[n] )
            last_arrival = n; 
//        last_arrival=max(last_arrival, double(D-S[n])/double(K[n]));
    }
    double max_speed=double(D*S[last_arrival])/(D-K[last_arrival]);
    cout.precision(numeric_limits<double>::digits10 + 1);
    cout << fixed <<  max_speed;
}

int main(){

    freopen ( "A-large.in", "r", stdin );
    freopen ( "A-large.out", "w", stdout );

	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		main2();
		cout<<endl;
	}
    fclose (stdin);
    fclose (stdout);
}