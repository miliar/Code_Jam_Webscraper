#include <bits/stdc++.h>

using namespace std;

bool isTidy(string a){

	for(int i=1;i<a.size();i++){
		if(a[i] < a[i-1]) return false;
	}

	return true;
}


std::string to_string(unsigned long long i)
{
    std::stringstream ss;
    ss << i;
    return ss.str();
}

int main(){
int t;
cin>>t;


	for(int xx =1;xx<=t;xx++){
		unsigned long long  n;
		cin>>n;
		////n=111111111111111110;
        string str;
		bool found = false;
		while(found == false && n >= 1){
             str = to_string(n);
            //cout<<str<<endl;
			found = isTidy(str);
			n= n-1;
		}

		cout<<"Case #"<<xx<<": "<<str<<endl;

	}
}
