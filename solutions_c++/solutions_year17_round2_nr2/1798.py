/*  Coder: Harsh Gupta
	Email: harshgupta.11dec@gmail.com
	Github: harshgupta11
	Linkedin: harshgupta11
	Problem Link: 
*/

#include "bits/stdc++.h"

using namespace std;

#define mp make_pair
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
void print(int O, char side, char important){
	if(O >= 1){
			cout << side;
	}
	for(int i = 0;i<O;++i){
		cout << important << side;
	}
}
void solve(){
	int N,R,O,Y,G,B,V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	if(B < O+1 && O != 0 && N != B+O){
		cout << "IMPOSSIBLE\n";
		return;
	}
	else if(R < G+1 && G != 0 && N != R+G){
		cout << "IMPOSSIBLE\n";
		return;
	}
	else if(Y < V+1 && V != 0 && N!= Y+V){
		cout << "IMPOSSIBLE\n";
		return;
	}
	if(N == B+O){
		if(B != O){
			cout << "IMPOSSIBLE\n";
			return;
		}
		for(int i = 0;i<B;++i){
			cout << "BO";
		}
		cout << '\n';
		return;
	}
	else if(N == R+G){
		if(R != G){
			cout << "IMPOSSIBLE\n";
			return;
		}
		for(int i = 0;i<R;++i){
			cout << "RG";
		}
		cout << '\n';
		return;
	}
	else if(N == Y+V){
		if(Y != V){
			cout << "IMPOSSIBLE\n";
			return;
		}
		for(int i = 0;i<Y;++i){
			cout << "YV";
		}
		cout << '\n';
		return;
	}
	int newR = R, newY = Y,newB=B;
	if(G!=0)
	 	newR = R-(G+1);
	if(V!=0)
		newY = Y-(V+1);
	if(O!=0)
		newB = B-(O+1);
	if(newR > newY+newB+1){
		cout << "IMPOSSIBLE\n";
		return;
	}
	else if(newY > newR+newB+1){
		cout << "IMPOSSIBLE\n";
		return;
	}
	else if(newB > newR + newY+1){
		cout << "IMPOSSIBLE\n";
		return;
	}
	char max1 = 'R', max2 = 'B', max3 = 'Y';
	int n1, n2, n3;
	if(newR >= newB && newR >= newY){
		max1 = 'R';
		n1 = newR;
		if(newY >= newB){
			max2 = 'Y';
			max3 = 'B';
			n2 = newY;
			n3 = newB;
		}
		else{
		   max2 = 'B';
		   max3 = 'Y';
		   n2 = newB;
		   n3 = newY;
		}
	}
	else if(newB >= newR && newB >= newY){
		max1 = 'B';
		n1 = newB;
		if(newY >= newR){
			max2 = 'Y';
			max3 = 'R';
			n2 = newY;
			n3 = newR;
		}
		else{
		    max2 = 'R';
		    max3 = 'Y';
		    n2 = newR;
		    n3 = newY;
		}
	}
	else if(newY >= newB && newY >= newR){
		max1 = 'Y';
		n1 = newY;
		if(newR >= newB){
			max2 = 'R';
			max3 = 'B';
			n2 = newR;
			n3 = newB;
		}
		else{
		    max2 = 'B';
		    max3 = 'R';
		    n2 = newB;
		    n3 = newR;
		}
	}
	if( O == 0 && G == 0 && V == 0){
		if(n1 > n2+n3){
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	if(max1 == 'R'){
		if(max2 == 'Y'){
	    	print(O,'B','O');
			print(G,'R','G');
			print(V,'Y','V');	
		}
		else {
			print(V,'Y','V');
			print(G,'R','G');
			print(O,'B','O');
		}
		
	}
	else if(max1 == 'B'){
		if(max2 == 'Y'){
		print(G,'R','G');
		print(O,'B','O');
		print(V,'Y','V');
		}
		else{
			print(V,'Y','V');
			print(O,'B','O');
			print(G,'R','G');
		}	
	}
	else if(max1 == 'Y'){
		if(max2 == 'B'){
		print(G,'R','G');
		print(V,'Y','V');
		print(O,'B','O');
		}
		else{
			print(O,'B','O');
			print(V,'Y','V');
			print(G,'R','G');	
		}
	}
	//cout << n1 << ' ' << n2 << ' ' << n3 << '\n';
	while(n1 > n2 && n3 > 0){
		cout << max1 << max3;
		--n1;
		--n3; 
	}
	while(n3 > 0){
		cout << max1 << max2 << max3;
		n1--;
		n2--;
		n3--;
	}
	while(n1 > 0 && n2 > 0){
		cout << max1 << max2;
		n1--;
		n2--;
	}
	while(n1 > 0){
		cout << max1;
		n1--;
	}	
	/*while(n1 > 0 && n2 > 0 && n3 > 0){
		cout << max1 << max2 << max3;
		n1--;
		n2--;
		n3--;
	}
	cout << n1 << ' ' << n2 << ' ' << n3 << '\n';

	while(n1 > 0 && n2 > 0){
		cout << max1 << max2;
		n1--;
		n2--;
	}
		cout << n1 << ' ' << n2 << ' ' << n3 << '\n';

	while(n1 > 0){
		cout << max1;
		n1--;
	}*/
	cout << '\n';
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int test = 1;test <=T;++test){
		cout << "Case #" << test << ": ";
		solve();
	}
    return 0;
}
