#include<bits/stdc++.h>
using namespace std;
class cmp{
	public:
	bool operator()(pair<pair<int,int>,int> i,pair<pair<int,int> ,int> j){
		if(i.first.first!=j.first.first){
			return i.first.first<j.first.first;
			
		}if(i.first.second!=j.first.second){
			return i.first.second<j.first.second;
			
		}
		return i.second>j.second;
	}
};
int main (){
	 freopen("test.in","r",stdin);
    freopen("count.txt","w",stdout);
	int t;
	cin>>t;
	for(int w=1;w<=t;w++){
		int x,y;
		priority_queue<pair<pair<int,int> ,int> ,vector<pair<pair<int,int>,int> > ,cmp> q;
		pair<int,int> foo;
		pair<pair<int,int> ,int> bar;
		cin>>x>>y;
		if(x%2==1){
			foo=make_pair(x/2,x/2);
			bar=make_pair(foo,x/2+1);
			q.push(bar);
		}else{
			foo=make_pair(x/2-1,x/2);
			bar=make_pair(foo,x/2);
			q.push(bar);
			
		}
		for(int i=1;i<y;i++){
			int a=q.top().first.first;
			int b=q.top().first.second;
			int c=q.top().second;
			q.pop();
			if(a%2==1){
			foo=make_pair(a/2,a/2);
			bar=make_pair(foo,c-a/2-1);
			q.push(bar);
			}else{
			foo=make_pair(a/2-1,a/2);
			bar=make_pair(foo,c-a/2-1);
			q.push(bar);
			
			}if(b%2==1){
			foo=make_pair(b/2,b/2);
			bar=make_pair(foo,c+b/2+1);
			q.push(bar);
			}else{
			foo=make_pair(b/2-1,b/2);
			bar=make_pair(foo,c+b/2);
			q.push(bar);
			
			}
		}
		cout<<"Case #"<<w<<": "<<q.top().first.second<<" "<<q.top().first.first<<endl;;
		
	}
}
