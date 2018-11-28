#include <bits/stdc++.h>

using namespace std;

int main() {
	int i,T,N,R,O,Y,G,B,V,b,l1,l2,j;
	char x,y,z,prev;
	cin>>T;
	for(i=1;i<=T;i++) {
		cin>>N>>R>>O>>Y>>G>>B>>V;
		cout<<"Case #"<<i<<": ";
		if(R>N/2 || O>N/2 || Y>N/2 || G>N/2 || B>N/2 || V>N/2) {
			cout<<"IMPOSSIBLE";
		}
		else {
			if(R>=Y && R>=B) {
				b = R;
				l1 = Y;
				l2 = B;
				x = 'R';
				y = 'Y';
				z = 'B';
			}
			else if(Y>=R && Y>=B) {
				b = Y;
				l1 = R;
				l2 = B;
				x = 'Y';
				y = 'R';
				z = 'B';
			}
			else {
				b = B;
				l1 = Y;
				l2 = R;
				x = 'B';
				y = 'Y';
				z = 'R';	
			}
			j = 0;
			prev = '0';
			while(j < N) {
				if(j%2 == 0 && b > 0) {
					cout<<x;
					b--;
					prev = x;
				}
				else {
					if(l1 >= l2 && prev != y) {
						cout<<y;
						l1--;
						prev = y;
					}
					else {
						cout<<z;
						l2--;
						prev = z;
					}
				}
				j++;
			}
		}
		cout<<"\n";
	}
	return 0;
}