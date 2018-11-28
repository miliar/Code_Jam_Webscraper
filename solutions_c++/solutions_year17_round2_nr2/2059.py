#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;
int main() {
	ifstream fin;
	ofstream fout;
	vector <char> a;
	fin.open("sample.txt");
	fout.open("answers.txt");
	int t, i, T, n, r, o, y, g, b, v;
	double j;
	char ch;
	fin>>t;
	for(T=1;T<=t;T++) {
		fout<<"Case #"<<T<<": ";
		fin>>n>>r>>o>>y>>g>>b>>v;
		if(o==0&&g==0&&v==0) {
			if(r+y>=b&&r+b>=y&&b+y>=r) {
				if( y >= b && y >= r ) {
					for(i=0;i< y ;i++)
						a.push_back( 'Y' );
					if( b >= r ) {
						for(i=0;i< b ;i++)
							a.insert(a.begin()+(2*i), 'B');
						for(i;i< y ;i++) {
							r--;
							a.insert(a.begin()+(2*i), 'R');
						}
						for(i=0;i< r ;i++)
							a.insert(a.begin()+(3*i), 'R');	
					}
					else {
						for(i=0;i< r ;i++)
							a.insert(a.begin()+(2*i), 'R');
						for(i;i< y ;i++) {
							b--;
							a.insert(a.begin()+(2*i), 'B');
						}
						for(i=0;i< b ;i++)
							a.insert(a.begin()+(3*i), 'B');	
					}
					for(i=0;i<a.size();i++)
						fout<<a[i];
				}
				else if( b >= r && b >= y ) {
					for(i=0;i< b ;i++)
						a.push_back( 'B' );
					if( r >= y ) {
						for(i=0;i< r ;i++)
							a.insert(a.begin()+(2*i), 'R');
						for(i;i< b ;i++) {
							y--;
							a.insert(a.begin()+(2*i), 'Y');
						}
						for(i=0;i< y ;i++)
							a.insert(a.begin()+(3*i), 'Y');	
					}
					else {
						for(i=0;i< y ;i++)
							a.insert(a.begin()+(2*i), 'Y');
						for(i;i< b ;i++) {
							r--;
							a.insert(a.begin()+(2*i), 'R');
						}
						for(i=0;i< r ;i++)
							a.insert(a.begin()+(3*i), 'R');	
					}
					for(i=0;i<a.size();i++)
						fout<<a[i];
				}
				else {
					for(i=0;i< r ;i++)
						a.push_back( 'R' );
					if( y >= b ) {
						for(i=0;i< y ;i++)
							a.insert(a.begin()+(2*i), 'Y');
						for(i;i< r ;i++) {
							b--;
							a.insert(a.begin()+(2*i), 'B');
						}
						for(i=0;i< b ;i++)
							a.insert(a.begin()+(3*i), 'B');	
					}
					else {
						for(i=0;i< b ;i++)
							a.insert(a.begin()+(2*i), 'B');
						for(i;i< r ;i++) {
							y--;
							a.insert(a.begin()+(2*i), 'Y');
						}
						for(i=0;i< y ;i++)
							a.insert(a.begin()+(3*i), 'Y');	
					}
					for(i=0;i<a.size();i++)
						fout<<a[i];
				}
				fout<<endl;
			}
			else
				fout<<"IMPOSSIBLE\n";
		}
		else {
			//insert code here
		}
		a.clear();
	}
	return 0;
}