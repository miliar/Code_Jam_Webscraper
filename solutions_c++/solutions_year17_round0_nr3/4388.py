#include <iostream>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(){
	int TestNum=0;
	cin>>TestNum;
	for( int i=0; i<TestNum; i++ ){
		int N, K;
		cin>>N>>K;
		typedef map<int64_t,int64_t>::iterator itr_t;
		map<int64_t,int64_t> gaps;
		gaps[N]++;
		int64_t Ls=0, Rs=0;
		for( int j=0; j<K; j++ ){
			itr_t itr = --gaps.end();
			int64_t gapNum = itr->second;
			int64_t gapSz = itr->first;

			int64_t remain = gapSz-1;
			Ls = remain/2;
			Rs = remain/2+ (remain%2);
			//cout<<remain<<":"<<((*itr)%2)<<endl;
			itr->second--;
			if( itr->second==0 )
				gaps.erase(itr);
			gaps[Ls]++;
			gaps[Rs]++;
		}
		cout<<"Case #"<<i+1<<": "<< max(Ls,Rs)<<" "<<min(Ls,Rs)<<endl;
	}
}