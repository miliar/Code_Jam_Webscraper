#include <iostream>
#include <string>
using namespace std;


int main() {
  int t;
  unsigned long long R,C;
  cin >> t;
  int empty='?';
  for (int i = 1; i <= t; ++i) {
    cin >> R >> C;
  	int** a = new int*[R];
	string s;
  	for(int row=0;row<R;row++){
  		cin>>s;
  		a[row]=new int[C];
  		for(int col=0;col<C;col++){
			a[row][col]=s[col];
  		}
  	}

  	for(int row=0;row<R;row++){
  		int c = a[row][0];
	  	//L->R
  		for(int col=0;col<C;col++){
  			if(a[row][col] == empty){
				a[row][col] = c;
  			}
  			else{
  				c = a[row][col];
  			}
  		}
	  	//R->L
	  	c = a[row][C-1];
  		for(int col=C-1;col>=0;col--){
  			if(a[row][col] == empty){
				a[row][col] = c;
  			}
  			else{
  				c = a[row][col];
  			}
  		}
  	}

  	for(int col=0;col<C;col++){
  		//T->B
  		int c = a[0][col];
  		for(int row=0;row<R;row++){
  			if(a[row][col] == empty){
				a[row][col] = c;
  			}
  			else{
  				c = a[row][col];
  			}
  		}
  		//B->T
  		c= a[R-1][col];
  		for(int row=R-1;row>=0;row--){
  			if(a[row][col] == empty){
				a[row][col] = c;
  			}
  			else{
  				c = a[row][col];
  			}
  		}
  	}
    cout << "Case #" << i << ":" << endl;
  	for(int row=0;row<R;row++){
  		for(int col=0;col<C;col++){
  			cout<<(char)a[row][col];
  		}
  		cout<<endl;
  	}

  	for(int row=0;row<R;row++){
  		delete[] a[row];
  	}
  	delete[] a;
  }

  return 0;
}