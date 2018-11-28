#include<fstream>
#include<vector>
using namespace std;

string s;

ifstream cin ("A-large.in");
ofstream cout ("ax.out");

int lplin(){
	for(int i=0;i<s.size();i++){
		if(s[i]=='-'){
			return i;
		}
	}	
	return -1;
}

void fixer(int l, int n){
	for(int i=0;i<n;i++){
		if(s[i+l]=='+'){
			s[i+l]='-';
		}
		else{
			s[i+l]='+';
		}
	}
}

int main(){
	int t;
	cin>>t;
	int ca=0;
	while(t--){
		ca++;
		int n;
		int cou=0;
		cin>>s>>n;
		while((lplin()<=s.size()-n)&&(lplin()!=-1)){
			fixer(lplin(),n);
			cou++;
		}
		if(lplin()==-1){
			cout<<"Case #"<<ca<<": "<<cou<<endl;
		}
		else{
			cout<<"Case #"<<ca<<": "<<"IMPOSSIBLE"<<endl;
		}	
	}
}
