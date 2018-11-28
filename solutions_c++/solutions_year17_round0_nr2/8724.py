#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

int T;
long long N;
long long TEN[18];
ofstream fout("fout.txt");

long long Solve(int index){
    int i,ln,n,flag = 1;
    long long K = N,P;
    //cout<<index<"\t";
    while(K){
        P = K;
        ln = n = 0;
        flag = 1;
        for( i = index ; i ; i-- ){
            ln = n;
            n = P/TEN[i];
            if( n < ln ){
                flag = 0;
                break;
            }
            //cout<<n<<"\t";
            P %= TEN[i];
        }
        //cout<<P<<endl<<endl;
        if( P < n )
            flag = 0;
        if( flag )
            return K;
        --K;
    }
    return 9;
}

int main(){
	int t;
	int i;
	int j,l,r;

	TEN[0] = 1;
    for( i = 1 ; i < 18 ; i++ ){
        TEN[i] = TEN[i-1]*10;
    }
	cin>>T;
	for( j = 1; j<=T ; j++){
		cin>>N;
		for( i = 17; i >= 0 ; i--){
            if( N >= TEN[i] )
                break;//the biggest number with base 10
		}
		fout<<"Case #"<<j<<": "<<Solve(i)<<endl;
	}
	return 0;
}
