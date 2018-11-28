#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

string to_string(int num){
	int i, rem, len = 0, n;
 	string str;
    n = num;
    while (n != 0)
    {
        len++;
        n /= 10;
    }
    for (i = 0; i < len; i++)
    {
        rem = num % 10;
        num = num / 10;
        char c = rem + '0';
        str = c + str;
    }
    return str;
}

bool is_tidy(string s){
	int l = s.length();
	bool b = true;
	for (int i=0; i<l-1; i++){
		if (s[i+1]-s[i]<0) b=false; 
	}
	return b;
}


int tidy_num_before(int x){
	if (is_tidy(to_string(x))) return x;
	else return tidy_num_before(x-1);
}



int main(){
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin>>tt;

	for(int ttt=0; ttt<tt; ttt++){
		int n;
		cin>>n;
		//cout<<is_tidy("81");
		cout<<"Case #"<<ttt+1<<": "<<tidy_num_before(n)<<endl;
	}
}