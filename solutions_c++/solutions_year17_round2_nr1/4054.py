#include <bits/stdc++.h>

using namespace std;
int caso=1;

void doit(){

int D,N;
cin >> D;
cin >> N;
long double K[N];
long double S[N];
long double t_total;

for(int i=0; i<N; i++){
	cin >> K[i];
	cin >> S[i];
}

long double aux;

//ordenar
for(int i=0; i<N-1; i++){
	for(int j=i+1; j<N; j++){
		if(K[i]>K[j]){
			aux=K[i];
			K[i]=K[j];
			K[j]=aux;
			aux=S[i];
			S[i]=S[j];
			S[j]=aux;
		}
	}
}

long double t_aux,t_alcance,d_restante;


if(N==1){
	t_total=  (D-K[0])/S[0];
}
else {
	if(S[0]<S[1]){
		t_total= (D-K[0])/S[0];
	}
	else{
		t_aux=  (D-K[0])/S[0];
		t_alcance= (K[1]-K[0])/(S[0]-S[1]);
		if(t_aux<t_alcance){
			t_total=t_aux;
		} else
		{
			d_restante= D- (t_alcance*S[1]+K[1]);
			t_total=t_alcance +  (d_restante)/S[1];
		}
	} 
}

long double vmax;
	cout << "Case #" << caso << ": ";
vmax= D/ t_total;
 printf("%Lf", vmax);
cout << endl;
caso++;

}

int main(){
	freopen("A-small-attempt0 (1).in" , "r" , stdin);
	freopen ("cruise_control.out","w",stdout);
	
int T;
cin >> T;

while(T--) doit();

return 0;
}

