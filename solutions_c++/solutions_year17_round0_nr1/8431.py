#include<bits/stdc++.h>
using namespace std;
unordered_map<string, int>flipper;
int length = 0;
string res("");
void flip_pancakes(string str, int score, int flip_length){
	//cout<<"current "<<str<<endl;
	if(flipper.find(str) != flipper.end()){
	if(flipper[str] <= score)
		return;
	else{
			if(flipper.find(res) == flipper.end())
				return;
		}
	}
	flipper[str] = score;
	string temp;
	for(int i=0; i<=length - flip_length; i++){
		temp = str;
		for(int j=i; j<i+flip_length; j++){
		if(str[j] == '-')
			temp[j] = '+';
		else
			temp[j] = '-';
		}
		//cout<<"modify "<<str<<endl;
		flip_pancakes(temp,score+1,flip_length);
	}
}

int main(){
//freopen("input.in","r",stdin);
//freopen("output.in","w",stdout);
int test,t,flip_length;
string str;
cin>>test;
t=test;
while(test--){
		res.clear();
		flipper.clear();
		cin>>str;
		cin>>flip_length;
		length = str.length();
		for(int i=0; i<length; i++)
			res.push_back('+');
		flip_pancakes(str,0,flip_length);
		//cout<<res<<endl;
		if(flipper.find(res) != flipper.end())
		cout<<"Case #"<<t-test<<": "<<flipper[res]<<endl;
		else
		cout<<"Case #"<<t-test<<": IMPOSSIBLE"<<endl;
}
}
