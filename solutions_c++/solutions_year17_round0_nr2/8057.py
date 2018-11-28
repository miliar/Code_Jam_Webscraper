//============================================================================
// Name        : GCJ.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
int T;
int main() {
	cin>>T;
	for(int i=1;i<T+1;++i){
		long long n;
		cin>>n;
		int d[20]={};
		for(int j=0;j<20;++j){
			d[j]=n%10;
			n=n/10;
		}
		int flg=1;
		while(flg>0){
			flg=0;
			for(int j=19;j>0;--j){
				if(flg>0){
				d[j]=9;
				}else{
					if(d[j]>d[j-1]){
						d[j]--;
						flg=1;
					}
				}
			}
			if(flg>0)d[0]=9;
		}
		n=0;
		for(int j=19;j>0;--j)n=(n+d[j])*10;
		n+=d[0];
		cout << "Case #" << i<<": "<<n<<endl;
	}
	return 0;
}
