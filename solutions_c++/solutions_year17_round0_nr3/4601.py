#include<bits/stdc++.h>

using namespace std;

set< pair<int, int>, std::greater< pair<int, int> > > listt;

int main()
{	
	int T, N, K;
	cin>>T;
	for(int t = 1; t <= T; t++){
		cin>>N>>K;
		listt.clear();
		listt.insert({N, 1});
		for(int i = 1; i < K; i++){
			pair<int, int> t = *(listt.begin());
			listt.erase(listt.begin());
			int val = t.first, loc = t.second;
			if(val%2 == 0){
				listt.insert({val/2-1, loc});
				listt.insert({val/2, loc+val/2});
			}
			else{
				listt.insert({val/2, loc});
				listt.insert({val/2, loc+val/2+1});	
			}
		}
		cout<<"Case #"<<t<<": "<<(listt.begin()->first/2)<<" "<<((listt.begin()->first-1)/2)<<endl;
	}
	return 0;
}