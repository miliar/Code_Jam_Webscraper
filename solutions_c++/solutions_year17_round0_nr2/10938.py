#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char * argv[]){
	int t,i,j;
//	scanf("%d",&t);
	ofstream outfile ("output.txt");
	std::fstream infile("/media/light/State Library/Pro-storage/C++-codesources(mostly)/GCJ/B-small-attempt1.in", std::ios_base::in);
	infile >> t;
	for(i=0;i<t;i++){
		int n;
//		scanf("%d",&n);
		infile >> n;	
			for(j=n;j>=0;j--){
				
				int a,b,c;
				
				c=j%10;
				b=(j%100-c)/10;
				a=(j-j%100)/100;
				
				if(c>=b&&b>=a){
					//printf("%d",j);
					outfile << "Case #"<<i+1<<": "<<j;
					if(i!=t-1) outfile << endl;
					break;
				}
			}
		
	}
	return 0;
}