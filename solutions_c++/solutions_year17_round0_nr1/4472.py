#include<bits/stdc++.h>

using namespace std;

deque<int> que;
int K;

int getAns(){
	int ans = 0;
	while(!que.empty()){
		if(que.front() == 0){
			if((int)que.size() < K){
				return -1;
			}
			for(int i = 0; i < K; i++){
				que[i] = (que[i] == 0) ? 1 : 0;
			}
			ans++;
		}
		else{
			que.pop_front();
		}
	}
	return ans;
}

int main()
{	
	int T;
	string str;
	cin>>T;
	for(int t = 1; t <= T; t++){
		cin>>str>>K;
		que.clear();
		for(char ch : str){
			if(ch == '+'){
				que.push_back(1);
			}
			else{
				que.push_back(0);
			}
		}
		int res = getAns();
		if(res < 0){
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<t<<": "<<res<<endl;	
		}
	}
	return 0;
}