#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#include <string>

string rev(string a){
	 int len = a.size();
	 if (len == 0) return a;
	 else if (a[0] == '+'){
	 	string m;
	 	m = rev(a.substr(1));
	 	string k;
	 	k = "-"+m;
	 	return k;
	 }
	 else {
	 	string m;
	 	m = rev(a.substr(1));
	 	string k;
	 	k = "+"+m;
	 	return k;
	 }
}

int baap(string s, int k){
	int len = s.size();
	//cout<<s<<k<<len;
	if (len < k) return -50000;
	else if (len == k) {
		size_t m= s.size();
		string idl(m,'+');
		string ids(m,'-');
		
		if (s == idl) return 0;
		else if (s == ids) return 1;
		else return -40000;
	}
	else {
		if (s[0]=='+'){
			int ans = baap(s.substr(1),k);
			return ans;
		}
		else{
			string nu;
			nu = rev(s.substr(1,k-1))+s.substr(k);
			//cout<<nu<<endl;
			int ans = baap(nu,k);
			return 1+ans;
		}
	}
}





int main() {
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    //cin >> n >> m;  // read n and then m.
    string sr;
    cin>> sr;
    int a;
    cin>> a;

    int res = baap(sr,a);
    //cout<<res<<endl;



if (res >= 0)


    cout << "Case #" << i << ": " << res<< endl;
else
	cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    

    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}