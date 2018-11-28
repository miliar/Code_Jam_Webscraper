#include <iostream>
#include <fstream>
#include<queue>
#include<string>
#include<stack>
#include<unordered_map>
#include<unordered_set>
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
int main() {
	freopen("/Users/tao/CLionProjects/CodeJam/input.in","r",stdin);
	freopen("/Users/tao/CLionProjects/CodeJam/output.in","w",stdout);
	int T;
	cin>>T;
	int case1=1;
	while(case1<=T){
		string str;
		int size;
		cin>>str;
		cin>>size;
		solve(str,size,case1);
		case1++;
	}
	return 0;
}