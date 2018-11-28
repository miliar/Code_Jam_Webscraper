#include<iostream>
#include<string>
using namespace std;

string flipCake(string, int, int);
int flips = 0;
int main(){
    int n = 0, k = 0;
    cin >> n;
    string cakeString;

    for(int i = 0; i < n; i++){
	cin>>cakeString;
	cin >> k;
	int length = cakeString.length();
	size_t foundNegative = cakeString.find('-');
	if (!(foundNegative != std::string::npos)){cout<<"Case #"<<i+1<<": "<<0<<endl; continue;}
	else if ((foundNegative != std::string::npos) && (k > length)){cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl; continue;}
	else{
		for(int j = 0; j < length; j++){
		    if((cakeString[j] == '-') && (j + k -1 < length)){
//cout<<j<<" ";
			cakeString = flipCake(cakeString, j, k);
		    }
		}
	}
	foundNegative = cakeString.find('-');
	if ((foundNegative != std::string::npos)){cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;}
	else {cout<<"Case #"<<i+1<<": "<<flips<<endl;}
	flips = 0;
    }
}


string flipCake(string cakeString, int index, int k){
    for(int i = index; i < index + k; i++){
	cakeString[i] = (cakeString[i] == '-')? '+' : '-';
    }
flips++;
return cakeString;
}
