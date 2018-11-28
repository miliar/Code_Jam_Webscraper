#include<iostream>
#include<queue>
using namespace std;
bool a[1001];
int n;
string s;
int main(){
	ios::sync_with_stdio(false);
	//freopen("infile2.in","r",stdin);
	//freopen("outfile.txt","w",stdout);
	int t;
	cin >> t;
	for(int r=1; r<=t ;r++){
		cin >> s;
		int last=0;
		for(int i=1; i<s.size() ;i++){
			if(i==s.size()-1 && s[i]>=s[i-1]) last=i+1;
			else if(s[i]>s[i-1]) last=i;
			else if(s[i]<s[i-1]) break;
		}
		cout << "Case #" << r << ": ";
		if(s.size()==1){
			cout << s << '\n';
			continue;
		}
		if(last!=0) cout << s[0];
		else if(s[0]!='1') cout << (char)(s[0]-1);
		for(int i=1; i<s.size() ;i++){
			if(i<last) cout << s[i];
			else if(i==last) cout << (char)(s[i]-1);
			else cout << 9;
		}
		cout << '\n';
	}
}
