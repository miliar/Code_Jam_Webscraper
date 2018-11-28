#include<iostream>
#include<vector>
using namespace std;

string vector2String(vector<int> v){
	string result = "";
	for( int i=0; i<v.size(); i++ ){
		if( result == "" && v[i]==0 ) continue;
		result += to_string(v[i]);
	}
	return result;
}

string getTidyNum(string s){

	if ( s == "" || s == "0") return "0";

	vector<int> inputV;
	vector<int> resultV;
	for(int i=0; i<s.size(); i++ ){
		inputV.push_back((int)s[i]-48);
	}

	int curr, next;
	for( int i=0; i<inputV.size(); i++ ){
		
		if( i == inputV.size()-1 ) {
			resultV.push_back(inputV[i]);
		} else {
			curr = i;
			next = i+1;
			while( next<inputV.size()-1 && inputV[curr] == inputV[next] ){
				next++;
			}

			if( inputV[curr] > inputV[next] ){
				
				resultV.push_back(inputV[curr]-1);
				for( int j=curr+1; j<inputV.size(); j++){
					resultV.push_back(9);
				}
				return vector2String(resultV);
			}

			resultV.push_back(inputV[curr]);
		}
	}

	return vector2String(resultV);
}



int main(){

	int numCase;
	cin >> numCase;

	string numStr;
	string result = "";

	for( int i=0; i<numCase; i++ ){
		
		cin>>numStr;
		
		result = getTidyNum(numStr);
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	}

}