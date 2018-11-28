#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

typedef long long LL;

LL tw[70],bas[70];
void get(){
	LL i = 1,k = 1;
	memset(bas,0,sizeof(bas));
	memset(tw,0,sizeof(tw));
	bas[0] = 1;
	while(k < 62){
		tw[k] = tw[k-1] + i;
		i*=2;
		bas[k] = i;
		k++;
	}
	//cout << tw[61] <<endl;
}

int main(){
	ifstream fin("C-large.in");
	ofstream fout("Cout.out");
	LL n,k;
	get();
	int T, tt = 1;
	fin >> T;
	while(T--){
		fin >> n >> k;
		LL i,a,idx;
		for(idx = 61; idx >= 0; --idx){
			if(tw[idx] < k) break;
		}
		//cout <<idx<<endl;
		k -= tw[idx];
		n -= tw[idx];
		LL mod = n%bas[idx];
		n /= bas[idx];
		fout <<"Case #" << tt++ <<": ";
		if(k > mod) n--;
		fout << n-n/2 <<" " <<n/2 <<endl;
	}
	return 0;
}