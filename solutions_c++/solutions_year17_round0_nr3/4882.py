#include <iostream>
#include <fstream>
#include<queue>
#include<string>
#include<stack>
#include<unordered_map>
#include<unordered_set>
#include<functional>
#include<algorithm>
using namespace std;


bool cotains(string str,char c){
	for(int i=0;i<str.length();++i){
		if(str[i]==c)
			return true;
	}
	return false;
}

int find(string str,int start,char c){
	int len=str.length();
	for(int i=start;i<len;++i){
		if(str[i]==c)
			return i;
	}
	return -1;
}


void solve(string str,int size,int& case1){
	int cnt=0;
	int index=0;
	int len=str.length();
	while(index<len){
		int ind=find(str,index,'-');
		if(ind==-1)
			break;
		cnt++;
		if(ind+size>len){
			cout<<"Case #"+to_string(case1)+": "+"IMPOSSIBLE"<<endl;
			return;
		}
		for(int i=ind;i<ind+size;++i)
			str[i]=str[i]=='+'?'-':'+';
		index=ind+1;
	}
	int xx=find(str,0,'-');
	if(xx!=-1){
		cout<<"Case #"+to_string(case1)+": "+"IMPOSSIBLE"<<endl;
	}else
		cout<<"Case #"+to_string(case1)+": "+to_string(cnt)<<endl;

}


struct Interval{
	int start;
	int length;
	bool operator<(const Interval& rhs) const
	{
		return length==rhs.length?start>rhs.start:length<rhs.length;
	}
};
void bath(int n,int k,int&case1){
	if(n==k){
		cout<<"Case #"+to_string(case1)+": "+"0 0"<<endl;
		return;
	}else{
		priority_queue<Interval>pq;
		pq.push({1,n});
		int minvalue=2147483647;
		int maxvalue=0;
		for(int z=0;z<k;++z){
			Interval top=pq.top();
			pq.pop();
			if(top.length%2!=0){
				if(z==k-1){
					minvalue=min(minvalue,top.length/2);
					maxvalue=max(maxvalue,top.length/2);
				}
				if(top.length/2>0){
					pq.push({top.start,top.length/2});
					pq.push({top.start+top.length/2+1,top.length/2});
				}
			}else{
				if(z==k-1){
					minvalue=min(minvalue,top.length/2-1);
					maxvalue=max(maxvalue,top.length/2);
				}
				if(top.length/2>1)
					pq.push({top.start,top.length/2-1});
				if(top.length/2>0)
				pq.push({top.start+top.length/2,top.length/2});
			}
		}
		cout<<"Case #"+to_string(case1)+": "+to_string(maxvalue)+" "+to_string(minvalue)<<endl;
		return;

	}
}



int main() {
	freopen("/Users/tao/CLionProjects/CodeJam/input.in","r",stdin);
	freopen("/Users/tao/CLionProjects/CodeJam/output.in","w",stdout);
	int T;
	cin>>T;
	int case1=1;
	while(case1<=T){
		int n;
		int k;
		cin>>n;
		cin>>k;
		bath(n,k,case1);
		case1++;
	}
	return 0;
}