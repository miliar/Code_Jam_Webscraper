#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("D-large.in");
	ofstream outputfile("myoutput.txt");
	int T, N, M, row_c, col_c, d1, style;
	bool line[100], col[100], diag1[199], diag2[199], plus, times, ans_plus[100][100], ans_times[100][100], in_p[100][100], in_t[100][100];
	vector<int> x_p, x_t, x_o, y_p, y_t, y_o;
	char c;
	file>>T;
	for(int t=0;t<T;t++){
//cout<<"Case "<<(t+1)<<endl;
		//read input
		file>>N>>M;
		style=0;
		x_p.clear(); x_t.clear(); x_o.clear(); y_p.clear(); y_t.clear(); y_o.clear();
		for(int i=0; i<N; i++){
			line[i]=true; col[i]=true; diag1[i]=true; diag1[N+i-1]=true; diag2[i]=true; diag2[N+i-1]=true;
			for(int j=0; j<N; j++){
				ans_plus[i][j]=false; ans_times[i][j]=false; in_p[i][j]=false; in_t[i][j]=false;
			}
		}
		//keep reading
		for(int i=0; i<M; i++){
			file>>c>>row_c>>col_c;
			row_c--; col_c--;
			switch(c){
				case 'o': plus=true; times=true; break;
				case '+': plus=true; times=false; break;
				case 'x': plus=false; times=true; break;
				case '.': plus=false; times=false; break;
				default: cout<<"unrecognized character"<<endl;
			}
			if(plus){
				diag1[row_c+col_c]=false; diag2[N-1+row_c-col_c]=false; style++; in_p[row_c][col_c]=true;
			}
			if(times){
				line[row_c]=false; col[col_c]=false; style++; in_t[row_c][col_c]=true;
			}
		}
		//solve times
		row_c=0; col_c=0;
		while(row_c<N){
			if(line[row_c]){
				while(col_c<N){
					if(col[col_c]){
						col[col_c]=false; line[row_c]=false; ans_times[row_c][col_c]=true; break;
					}
					col_c++;
				}
			}
			row_c++;
		}
		//solve plus
		for(int i=0; i<N; i++){
			for(int eps=0; eps<2; eps++){
				d1=i+eps*(2*N-2-2*i);
				if(diag1[d1]){
					for(int d2=N-1-i; d2<=N-1+i; d2+=2){
						if(diag2[d2]){
							ans_plus[(d1+d2-N+1)/2][(d1-d2+N-1)/2]=true;
							diag1[d1]=false; diag2[d2]=false; break;
						}
					}
				}
			}
		}
		//join
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++){
				if(ans_plus[i][j]){
					style++;
					if(ans_times[i][j] || in_t[i][j]){
						x_o.push_back(i); y_o.push_back(j);
						if(ans_times[i][j])
							style++;
					}else{
						x_p.push_back(i); y_p.push_back(j);
					}
				}else{
					if(ans_times[i][j]){
						style++;
						if(in_p[i][j]){
							x_o.push_back(i); y_o.push_back(j);
						}else{
							x_t.push_back(i); y_t.push_back(j);
						}
					}
				}
			}
		//write output
		outputfile<<"Case #"<<(t+1)<<": "<<style<<" "<<(x_o.size()+x_p.size()+x_t.size())<<endl;
		for(int i=0; i<x_o.size(); i++)
			outputfile<<"o "<<(x_o[i]+1)<<" "<<(y_o[i]+1)<<endl;
		for(int i=0; i<x_t.size(); i++)
			outputfile<<"x "<<(x_t[i]+1)<<" "<<(y_t[i]+1)<<endl;
		for(int i=0; i<x_p.size(); i++)
			outputfile<<"+ "<<(x_p[i]+1)<<" "<<(y_p[i]+1)<<endl;
//cout<<endl;
	}
	file.close();
	outputfile.close();
}

