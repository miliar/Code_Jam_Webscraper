#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main(){
	cout<<"launching function main"<<endl;
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	int T, N, G, P, g[4];
	int best, a, b;
	file>>T;
	for(int t=0;t<T;t++){
		for(int i=0; i<4; i++)
			g[i]=0;
		//read input
		file>>N>>P;
		for(int i=0;i<N;i++){
			file>>G;
			g[G%P]++;
		}
		//solve
		switch(P){
			case 2:
				best=g[0]+(g[1]+1)/2;
				break;
			case 3:
				a=min(g[1],g[2]);
				b=max(g[1],g[2]);
				best=g[0]+a+(b-a+2)/3;
				break;
			case 4:
				a=min(g[1],g[3]);
				b=max(g[1],g[3]);
				best=g[0]+a+(g[2]+1)/2+(b-a+3-2*(g[2]%2))/4;
				break;
			default:
				cout<<"ERROR: unexpected P = "<<P<<endl;
		}
		//write output
		outputfile<<"Case #"<<(t+1)<<": "<<best<<endl;
	}
	file.close();
	outputfile.close();
}

