#include <bits/stdc++.h>

using namespace std;


int isTidy(int n){
	int i,j,k;
	int num[20]; k = 0;

	while(n > 0){
		num[k++] = n%10;
		n /= 10;
	}

	if(k ==1){return true;}

	for(i = 0; i < k-1; i++){
		if(num[i] < num[i+1]){return false;}
	}

	return true;
}


int main(){
	
	ifstream fin("B-small-attempt0.in");
	ofstream fout("gcjb.txt");
	int t,l;
	fin >> t;
	for(l = 1; l <= t; l++ ){
		int n,i,j;
		fin >> n;
		i = n;
		while(n>0){
			if(isTidy(n) == 1){fout<<"Case #"<<l<<": "<<n<<endl; break;}
			n--;

		}
	}
}