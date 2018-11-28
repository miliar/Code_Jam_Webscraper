#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include <queue>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		int N,K,t1,t2;
		priority_queue<int> Q;
		cin>>N>>K;
		Q.push(N);
		for(i=0;i<K;i++) {
			k=Q.top();
			Q.pop();
			if(k%2)t1=t2=k/2;
			else {
				t1=k/2;
				t2=t1-1;
			}
			if(t1>0){
				Q.push(t1);
				Q.push(t2);
			}
		}
		cout<<"Case #"<<cs<<": ";
		cout<<t1<<" "<<t2<<endl;
	}
	return 0;
}
