#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main(){
	cout<<"launching function main"<<endl;
	ifstream file("B-large.in");
	ofstream outputfile("myoutput.txt");
	int T, N, C, M, Pi, Bi;
	int ti[1000], tp[1000], tlp[1000];
	int y, z;
	file>>T;
	for(int t=0;t<T;t++){
//cout<<"Case #"<<(t+1)<<endl;
		y=0; z=0;
		//read input
		file>>N>>C>>M;
		for(int i=0; i<C; i++)
			ti[i]=0;
		for(int i=0; i<N; i++)
			tp[i]=0;
		for(int i=0; i<M; i++){
			file>>Pi>>Bi;
			ti[Bi-1]++; tp[Pi-1]++;
		}
		//solve
		tlp[0]=tp[0];
		for(int i=1; i<N; i++)
			tlp[i]=tlp[i-1]+tp[i];
		for(int i=0; i<C; i++)
			y=max(y, ti[i]);
		for(int i=0; i<N; i++)
			y=max(y, (tlp[i]+ i)/(i+1));
		for(int i=0; i<N; i++){
			z=z+max(0, tp[i]-y);
		}
		//write output
		outputfile<<"Case #"<<(t+1)<<": "<<y<<" "<<z<<endl;
	}
	file.close();
	outputfile.close();
}

