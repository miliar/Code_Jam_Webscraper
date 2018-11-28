//============================================================================
// Name        : G17_A1_A.cpp
// Author      : Yul Obraz
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;
struct data1{
    char v;
	int x;
	int y;
	int x1;
	int y1;
	int x2;
	int y2;
};
void calc(char** target, int R, int C){
	vector<data1> info;
	for(int i =0; i<R; i++){
		for(int j =0; j<C; j++){
			if(target[i][j]!='?'){
				data1 d;
				d.v = target[i][j];
				d.x = i;
				d.y = j;
				info.push_back(d);
			}
		}
	}
	info[0].x1=0;
	info[0].x2=R-1;
	info[0].y1=0;
	info[0].y2=C-1;
	for(int i=1; i<(int)info.size(); i++){
		for(int j=0; j<i; j++){

			if(info[i].x>=info[j].x1 && info[i].x<=info[j].x2
			&&info[i].y>=info[j].y1 && info[i].y<=info[j].y2){
				cerr<<"i="<<i<<" j="<<j<<endl;
				//devide between two
				if(info[i].x==info[j].x){
					info[i].x1 = info[j].x1;
					info[i].x2 = info[j].x2;
					if(info[i].y>info[j].y){
						info[i].y1 = info[i].y;
						info[i].y2 = info[j].y2;
						info[j].y2 = info[i].y - 1;
					}else{
						info[i].y1 = info[j].y1;
						info[i].y2 = info[j].y - 1;
						info[j].y1 = info[j].y;
					}
				} else {
					info[i].y1 = info[j].y1;
					info[i].y2 = info[j].y2;

					if(info[i].x>info[j].x){
						info[i].x1 = info[i].x;
						info[i].x2 = info[j].x2;
						info[j].x2 = info[i].x - 1;
					}else{
						info[i].x1 = info[j].x;
						info[i].x2 = info[j].x2;
						info[j].x2 = info[j].x - 1;
					}
				}
			cerr <<"j"<<info[j].v<<" "<<info[j].x<<" "<<info[j].y<<" "<<info[j].x1<<" "<<info[j].x2<<" "<<info[j].y1<<" "<<info[j].y2<<" "<<endl;
			cerr <<"i"<<info[i].v<<" "<<info[i].x<<" "<<info[i].y<<" "<<info[i].x1<<" "<<info[i].x2<<" "<<info[i].y1<<" "<<info[i].y2<<" "<<endl;
			}
		}
	}
	for(int t=0; t<(int)info.size(); t++){
		data1 &it= info[t];
		for(int i=it.x1; i<=it.x2; i++){
			for(int j=it.y1; j<=it.y2; j++){
				target[i][j]=it.v;
			}
		}
	}
	for(int i=0; i<R; i++){
		for(int j=0; j<C; j++){
			cout << target[i][j];
		}
		cout << endl;
	}
}
int main(int argc,char *argv[]) {
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		cout << "Case #"<< (i+1)<<":"<< endl;
		int R, C;
		cin >>R >>C;
		char ** target = new char*[R];
		for(int j=0; j<R; j++){
			string t;
			cin>>t;
			target[j]= new char[C];
			std::copy(t.begin(), t.end(), target[j]);
		}
		calc(target, R, C);
		for(int j=0; j<R; j++){
			delete target[j];
		}
		delete target;
	}
	return 0;
}
