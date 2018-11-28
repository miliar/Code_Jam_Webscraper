#include<iostream>
#include<string>
#include<vector>
#include <queue>
#include<fstream>
using namespace std;

string decr_string(string st){
	int i=st.length()-1;
	//bool borrow=false;
	string result;
	if(st[i]>'0'){
		st[i]=st[i]-1;
	//	cout<<"true\n";
		return st;
	}
	else{
	//	st[i]='9';
		string result=decr_string(st.substr(0,st.length()-1));
		while(result[0]=='0'){
			result=result.substr(1,result.length()-1);
		}	
		result+='9';
		return result;
	}

}
string find_sorted(string st,bool & ch){
	ch=false;
	for(int i=1;i<st.length();i++){
		if(st[i]<st[i-1]) {
			string temp=st.substr(0,i);
			temp=decr_string(temp);
			while(temp[0]=='0'){
				temp=temp.substr(1,temp.length()-1);
			}
			while(i<st.length()){
				temp+='9';
				i++;
			}
//			cout<<temp<<endl;
			ch=true;
			return temp;
		}
	}
	return st;
}
bool check_sorted(string & st){
	for(int i=1;i<st.length();i++){
		if(st[i]<st[i-1]) return false;
	}
	return true;
}



int main(){
	ifstream ifs("a1l.in");
	ofstream ofs("b1.out");
	if(ifs.is_open() && ofs.is_open()){
		int tc=0;
		ifs>>tc;
		for(int t1=0;t1<tc;t1++){
			string st="";
			ifs>>st;
		//	st=decr_string(st);
			bool flag=false;
			string result=find_sorted(st,flag);
			while(flag){
				result=find_sorted(result,flag);
			}
			ofs<<"Case #"<<t1+1<<": "<<result<<endl;
			cout<<"Case #"<<t1+1<<": "<<result<<endl;
			
		}
		
		//cout<<decr_string("11110");
		
	}
	
//	string st="1195";
//	cout<<find_sorted(st);
			
	return 0;
}
