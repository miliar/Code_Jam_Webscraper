#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int T, R, C; string ar[26];
int main() {
    ifstream cin("s1in.txt");
    ofstream cout("s1out.txt");
	cin>>T;
	for (int t=1; t<=T; t++) {
		cin>>R>>C;
		memset(ar, 0, sizeof ar);
		for (int i=0; i<R; i++) {
			cin>>ar[i];
		}
		bool work=0; int last=-1;
		for (int i=0; i<R; i++) {
			char c='?';
			int last=-1;
			for (int j=0; j<C; j++) {
				if (ar[i][j]!='?') {
					if (c=='?') {
						for (int k=j-1; k>=0; k--) {
							ar[i][k]=ar[i][k+1];
						}
					}
					c=ar[i][j];
				}
				if (c=='?') {
					last=j;
				}
				if (ar[i][j]=='?'&&c!='?') ar[i][j]=c;
			}
			if (c=='?') {
				if (work) {
					for (int j=0; j<C; j++) {
						ar[i][j]=ar[i-1][j];
					}
				} else last=i;
			} else {
				work=1;
			}
		}
		for (int i=last; i>=0; i--) {
			for (int j=0; j<C; j++)
				ar[i][j]=ar[i+1][j];
		}
		cout<<"Case #"<<t<<":\n";
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				cout<<ar[i][j];
			}
			cout<<"\n";
		}
	}
}
/*
C?D?
?J?A
????
*/
