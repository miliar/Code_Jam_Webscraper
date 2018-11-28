#include <iostream>
#include <string.h>
#include <list>
using namespace std;

//me cago en los putos indices de los cojones

struct dpoint{
	int x1;
	int x2;
	int y1;
	int y2;
	char meleon;
};

void rellenar(char a[25][25], dpoint p){
	for(int ii=p.y1;ii<=p.y2;ii++){
		for(int jj=p.x1;jj<=p.x2;jj++){
			a[ii][jj] = p.meleon;
		}
	}
}

void print_tarta(char a[25][25], int R, int C, int i){
	cout << "Case #" << i+1 << ":" << endl;
	for(int ii=0;ii<R;ii++){
		for(int jj=0;jj<C;jj++){
			cout << a[ii][jj];
		}
		cout << endl;
	}
}

int main(){
	int T, R, C;
	char tarta[25][25];
	char mander;
	list<dpoint> derecha;
	list<dpoint> abajo;
	
	cin >> T;
	for(int i=0;i<T;i++){
		cin >> R >> C;
		for(int ii=0;ii<R;ii++){
			for(int jj=0;jj<C;jj++){
				cin >> tarta[ii][jj];
			}
		}
		dpoint point;
		point.x1=0;
		point.y1=0;
		point.x2=0;
		point.y2=0;
		for(int ii=0;ii<R;ii++){
			//borrar lista derecha
			derecha.clear();
			for(int jj=0;jj<C;jj++){
				if(tarta[ii][jj]!='?'){
					//si lista derecha empty borrar lista abajo
					if(derecha.empty()){
						abajo.clear();
					}
					//borrar lista derecha
					derecha.clear();
					mander = tarta[ii][jj];
					point.x2=jj;
					point.y2=ii;
					point.meleon = mander;
					//rellenar espacio entre con mander
					rellenar(tarta, point);
					//añadir a lista derecha
					derecha.push_back(point);
					//añadir a lista abajo
					abajo.push_back(point);
					//cambiar x1 e y1
					point.x1 = point.x2+1;
					if(point.x1>=C){
						point.x1 = 0;
						point.y1 = point.y2+1;
					}
				}
				/*
				cout << ii << " " << jj <<endl;
				cout << point.x1 << " " << point.y1 <<endl;
				cout << point.x2 << " " << point.y2 <<endl;
				print_tarta(tarta, R, C, i);
				cin.ignore();
				cin.get();
				*/
			}
			//si lista derecha no empy
			  //ejecutar lista derecha
			  //borrar el último de lista abajo
			  //añadir el punto de lista derecha a lista abajo
			if(!derecha.empty()){
				dpoint paux = derecha.front();
				paux.x2 = C-1;
				rellenar(tarta, paux);
				abajo.pop_back();
				abajo.push_back(paux);
				point.x1=0;
				point.y1=point.y2+1;
			}
		}
		//ejecutar lista abajo
		while(!abajo.empty()){
			dpoint paux;
			paux = abajo.front();
			if(paux.y1==R-1) break;
			else{
				paux.y1=paux.y2+1;
				paux.y2=R-1;
				rellenar(tarta, paux);
			}
			abajo.pop_front();
		}
		print_tarta(tarta, R, C, i);
	}
}
