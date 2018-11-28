#include <iostream>
#include <fstream>
using namespace std;

int check_order(int n){
	int limit=n/2,a,b=n;
	//cout<<"limit "<<limit;
	if (n<10)
	return n;
	while (n >= limit ){
        a=n%10,b=n/10;
		while (b>9){
            if (a<b%10)
                {

                    break;
                }
            if (b<9)
                return n;
            a=b%10;
            b=b/10;

        }
        if (a>=b)
                return n;
        b--;
        n--;
		}
	return n;
	}
int main() {
  int t, n;
  //cout<<"Hello World \n";
  ifstream myfile("inp.in");
  ofstream outfile("out.txt");
  myfile>>t;
  //t=1;

  for (int i = 1; i <= t; i++) {
    myfile>> n ;
    //cin>>n;
    //n=110;
    //int output=check_order(n);
    //cout<<"Case #" << output  << endl;
    outfile<< "Case #" << i<<": "<<check_order(n)  << endl;
  }

}
