#include <bits/stdc++.h>

using namespace std;


// permutation
int main(){
//	string s = "-+-+-";
//	int k = 4;
	ifstream in("A-large.in");
	ofstream out("ofile");
	int q;
	in >> q;
//	cout << q << endl;
	for(int p=1;p<=q;p++){
		string s;
		in >> s;
		int k;
		in >> k;
	//	cout << p << " " << k << endl;

		int count = 0;
		for(int i=0;i<s.length()-k+1;i++){
			if(s[i]!='+'){
				for(int j=i;j<i+k;j++){
					if(s[j]!='+'){
						s[j]='+';
					}else{
						s[j]='-';
					}
				}
				count++;
			}

//			cout << p << " " << s << endl;
		}

		bool flag = false;
		int n = s.length()-k;
	//	cout << n << endl;
	//	cout <<  << endl;
		for(int i=s.length()-1;i>n;i--){
			if(s[i]!='+'){
		//		cout << s << endl;
				flag = true;
				out << "Case #" << p << ": " << "IMPOSSIBLE" << endl;
				break;
			}
		}

		if(!flag){
			out << "Case #" << p << ": " << count << endl;
		}

	}
}
