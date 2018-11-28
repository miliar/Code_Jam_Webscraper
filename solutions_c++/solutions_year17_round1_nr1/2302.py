#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;
int main()
{
	int ttt;
	cin >> ttt;
	for (int i=0;i<ttt;i++){
		int r, c;
		cin >> r >> c;
		char s[25][25];
		for (int j=0;j<r;j++){
			string ss;
			cin >> ss;
			for (int k =0;k<(int)ss.size();++k){
				s[j][k]= ss[k];
			}
		}
		for (int rr=0;rr<r;rr++){
			char ch = '?';
			char t = '?';
			for(int cc=0;cc<c;cc++){
				if(s[rr][cc]=='?'){
					s[rr][cc] = ch;
				}else{
					ch=s[rr][cc];
					if(t=='?'){
						t=ch;
					}
				}
			}
			for(int cc=0;cc<c;cc++){
				if(s[rr][cc]=='?'){
					s[rr][cc]=t;
				}
			}
		}
		char ch[25];
		ch[0]='?';
		char t[25];
		t[0]='?';
		for (int rr=0;rr<r;rr++){
			if(s[rr][0] != '?'){
				for(int cc=0;cc<c;cc++){
					ch[cc]=s[rr][cc];
				}
				if(t[0]=='?'){
					for(int cc=0;cc<c;cc++){
						t[cc]=ch[cc];
					}
				}
			}else{
				if(ch[0]!='?'){
					for(int cc=0;cc<c;cc++){
						s[rr][cc] = ch[cc];
					}
				}
			}
		}
		for (int rr=0;rr<r;rr++){
			if(s[rr][0] == '?'){
				for(int cc=0;cc<c;cc++){
					s[rr][cc]=t[cc];
				}
			}
		}
		cout << "Case #" << i+1 <<":" << endl;
		for (int rr=0;rr<r;rr++){
			for(int cc=0;cc<c;cc++){
				cout << s[rr][cc];
			}
			cout << endl;
		}
		cout << endl;
		
	}
}

