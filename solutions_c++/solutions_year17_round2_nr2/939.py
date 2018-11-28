#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("B-large.in");
	ofstream outputfile("myoutput.txt");
	int T, N, R, O, Y, G, B, V, r, y, b, ns[3], op[3], previous=0, other1, other2;
	char c[3]={'R','Y','B'}, co[3]={'G','V','O'};
	bool solvable, f[3], particular;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		file>>N>>R>>O>>Y>>G>>B>>V;
		//solve
		r=R-G; y=Y-V; b=B-O;
		solvable=(O<B+(O+B==N || O+B==0)?1:0)&&(G<R+(G+R==N || G+R==0)?1:0)&&(V<Y+(V+Y==N || V+Y==0)?1:0)&&(r<=y+b)&&(y<=b+r)&&(b<=r+y);
		particular=(O+B==N)||(G+R==N)||(V+Y==N);
		//write output
		outputfile<<"Case #"<<(t+1)<<": ";
		if(!solvable)
			outputfile<<"IMPOSSIBLE";
		else{
			if(particular){
				if(O>0)
					for(int i=0; i<O; i++)
						outputfile<<"OB";
				if(G>0)
					for(int i=0; i<G; i++)
						outputfile<<"GR";
				if(V>0)
					for(int i=0; i<V; i++)
						outputfile<<"VY";
			}else{
			f[0]=true; f[1]=true; f[2]=true;
			ns[0]=r; ns[1]=y; ns[2]=b;
			op[0]=G; op[1]=V; op[2]=O;
			previous=0;
			for (int i=0; i<3; i++)
				if(ns[i]>ns[previous])
					previous=i;
			while(ns[0]>0 || ns[1]>0 || ns[2]>0){
				other1=(previous+1)%3;
				other2=(previous+2)%3;
				if(ns[other2]>ns[other1])
					other1=other2;
				previous=other1;
				if(f[other1]){
					f[other1]=false;
					for(int i=0; i<op[other1]; i++)
						outputfile<<c[other1]<<co[other1];
				}
				outputfile<<c[other1];
				ns[other1]--;
			}
			}
		}
		outputfile<<endl;
	}
	file.close();
	outputfile.close();
}

