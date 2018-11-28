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


//void solve(string str,int size,int& case1){
//	int cnt=0;
//	int index=0;
//	int len=str.length();
//	while(index<len){
//		int ind=find(str,index,'-');
//		if(ind==-1)
//			break;
//		cnt++;
//		if(ind+size>len){
//			cout<<"Case #"+to_string(case1)+": "+"IMPOSSIBLE"<<endl;
//			return;
//		}
//		for(int i=ind;i<ind+size;++i)
//			str[i]=str[i]=='+'?'-':'+';
//		index=ind+1;
//	}
//	int xx=find(str,0,'-');
//	if(xx!=-1){
//		cout<<"Case #"+to_string(case1)+": "+"IMPOSSIBLE"<<endl;
//	}else
//		cout<<"Case #"+to_string(case1)+": "+to_string(cnt)<<endl;
//
//}
//
//
//struct Interval{
//	int start;
//	int length;
//	bool operator<(const Interval& rhs) const
//	{
//		return length==rhs.length?start>rhs.start:length<rhs.length;
//	}
//};
//void bath(int n,int k,int&case1){
//	if(n==k){
//		cout<<"Case #"+to_string(case1)+": "+"0 0"<<endl;
//		return;
//	}else{
//		priority_queue<Interval>pq;
//		pq.push({1,n});
//		int minvalue=2147483647;
//		int maxvalue=0;
//		for(int z=0;z<k;++z){
//			Interval top=pq.top();
//			pq.pop();
//			if(top.length%2!=0){
//				if(z==k-1){
//					minvalue=min(minvalue,top.length/2);
//					maxvalue=max(maxvalue,top.length/2);
//				}
//				if(top.length/2>0){
//					pq.push({top.start,top.length/2});
//					pq.push({top.start+top.length/2+1,top.length/2});
//				}
//			}else{
//				if(z==k-1){
//					minvalue=min(minvalue,top.length/2-1);
//					maxvalue=max(maxvalue,top.length/2);
//				}
//				if(top.length/2>1)
//					pq.push({top.start,top.length/2-1});
//				if(top.length/2>0)
//				pq.push({top.start+top.length/2,top.length/2});
//			}
//		}
//		cout<<"Case #"+to_string(case1)+": "+to_string(maxvalue)+" "+to_string(minvalue)<<endl;
//		return;
//
//	}
//}

void solve(vector<int>speeds,vector<int>positions,int Destion,int& case1){
	int n=speeds.size();
	double time=0.0;
	for(int i=0;i<n;++i){
		double tmp=(Destion-positions[i])*1.0/speeds[i];
		if(time<tmp)
			time=tmp;
	}
	double sp=Destion*1.0/time;
	printf("Case #%d: %.6f\n", case1, sp);
}

bool impossible;

string construct(queue<string> &a, queue<string> &b, queue<string> &c) {
	impossible = false;
	if (!(a.size() >= b.size() && a.size() >= c.size())) {
		if (b.size() > c.size()) {
			return construct(b, a, c);
		} else {
			return construct(c, a, b);
		}
	}
	string ret = string("");
	if (a.size() > b.size() + c.size()) {
		impossible = true;
		return ret;
	}
	while (!a.empty()) {
		ret += a.front();
		if (!b.empty()) {
			ret += b.front();
			b.pop();
		}
		if (c.size() == a.size()) {
			ret += c.front();
			c.pop();
		}
		a.pop();
	}
	return ret;
}


void pack(queue<string> &a, queue<string> &b) {
	while (!b.empty() && a.size() > 1) {
		string temp = string();
		temp+=b.front();
		b.pop();
		 temp = a.front() + temp;
		a.pop();
		temp = temp + a.front();
		a.pop();
		a.push(temp);
	}
}

string special_ans;

bool special(queue<string> &a, queue<string> &b, queue<string> &c, queue<string> &d, queue<string> &e, queue<string> &f) {
	if (a.size() + b.size() + c.size() + d.size() + e.size() + f.size() != 2) {
		return false;
	}
	if (a.size() == 1 && b.size() == 1) {
		special_ans = string(a.front() + b.front());
		return true;
	}
	if (c.size() == 1 && d.size() == 1) {
		special_ans = string(c.front() + d.front());
		return true;
	}
	if (e.size() == 1 && f.size() == 1) {
		special_ans = string(e.front() + f.front());
		return true;
	}
	return false;
}





int main() {
	//freopen("/Users/tao/CLionProjects/CodeJam/B-small-attempt1.in","r",stdin);
	freopen("/Users/tao/CLionProjects/CodeJam/B-large.in","r",stdin);
	freopen("/Users/tao/CLionProjects/CodeJam/outputB.in","w",stdout);
	int T;
	cin>>T;
	int case1=1;
	while(case1<=T){
//		int Destination;
//		int horses;
//		cin>>Destination;
//		cin>>horses;
//		vector<int>speeds;
//		vector<int>positions;
//		while(horses>0){
//			int posi;
//			int speed;
//			cin>>posi;
//			cin>>speed;
//			speeds.push_back(speed);
//			positions.push_back(posi);
//			horses--;
//		}
//		solve(speeds,positions,Destination,case1);
		queue<string>red;
		queue<string>yellow;
		queue<string>blue;
		queue<string>orange;
		queue<string>green;
		queue<string>v;
		int N;
		int R, O, Y, G, B,V;
		cin>>N;
		cin>>R;
		cin>>O;
		cin>>Y;
		cin>>G;
		cin>>B;
		cin>>V;
		for(int i=0;i<R;++i)
			red.push("R");
		for(int i=0;i<Y;++i)
			yellow.push("Y");
		for(int i=0;i<B;++i)
			blue.push("B");
		for(int i=0;i<O;++i)
			orange.push("O");
		for(int i=0;i<G;++i)
			green.push("G");
		for(int i=0;i<V;++i)
			v.push("V");

		pack(red,green);
		pack(blue,orange);
		pack(yellow,v);
		bool isSpecial=special(red,green,blue, orange,yellow,v);
		if(isSpecial){
			cout<<"Case #"+to_string(case1)+": "+special_ans<<endl;
			case1++;
			continue;
		}
		if(green.size() + v.size() + orange.size() != 0){
			cout<<"Case #"+to_string(case1)+": IMPOSSIBLE"<<endl;
			case1++;
			continue;
		}

		impossible=false;
		string res=construct(red,yellow,blue);
		if(impossible)
			cout<<"Case #"+to_string(case1)+": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"+to_string(case1)+": "+res<<endl;
		case1++;
	}
	return 0;
}