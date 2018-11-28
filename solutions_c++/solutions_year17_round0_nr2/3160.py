
#include <iostream>
#include <string>
using namespace std;
typedef long long ll;


int no_cases;

ll to_long_long(string str){
	ll ans=0;
	ll base=1;
	for (int i=str.size()-1; i>=0; i--){
		ans=ans+base*(str[i]-'0');
		base*=10;
	}
	return ans;
}

bool good(string s){
	for (int i=0; i+1<s.size(); i++){
		if (s[i]>s[i+1])
			return false;
	}
	return true;
}

ll solve(string s){
	ll number=to_long_long(s);
	string t="";

	for (int i=0; i<s.size(); i++){
		t+="1";
	}
	ll number_t=to_long_long(t);

	//cout<<s<<" "<<number<<" "<<t<<" "<<number_t<<endl;

	if (number_t==number){
		return to_long_long(s);
	}
	else if (number<number_t){
		string new_str="";
		for (int i=0; i+1<s.size(); i++)
			new_str+="9";
		return to_long_long(new_str);
	}
	else{
		for (int i=0; i+1<s.size(); i++){
			if (s[i+1]<s[i]){
				s[i]--;
				for (int k=i+1; k<s.size(); k++)
					s[k]='9';
				break;
			}
		}
		if (good(s))
			return to_long_long(s);
		else
			return solve(s);
	}
}

int main(){
	cin>>no_cases;
	for (int caseID=1; caseID<=no_cases; caseID++){
		string s;
		cin>>s;

		cout<<"Case #"<<caseID<<": "<<solve(s)<<endl;;
	}
}