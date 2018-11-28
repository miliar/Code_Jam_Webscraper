#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <list>
#include <sys/time.h>
#include <ilcp/cp.h>
#include <ilcplex/cplex.h>

Federico Javier Pousa




//Problema Data pointer
struct Problema{
	int N;
	int M;
	vector<vector<char> > gridOri;
	vector<vector<char> > grid;
	int best;
	Problema(){}
};
Problema * prob;


void solveMIP(){
	CPXENVptr env = NULL;
	CPXLPptr lp = NULL;
	int status;
	
	int cantvar = prob->N*prob->N*3;
	double *obj=(double*)malloc(sizeof(double)*cantvar);
	double *lb=(double*)malloc(sizeof(double)*cantvar);
	double *ub=(double*)malloc(sizeof(double)*cantvar);
	char *coltype=(char*)malloc(sizeof(char)*cantvar);
	int *rmatbeg=(int*)malloc(sizeof(int));
	int *rmatind=(int*)malloc(sizeof(int)*cantvar);
	double *rmatval=(double*)malloc(sizeof(double)*cantvar);
	double *rhs=(double*)malloc(sizeof(double)*1);
	char *sense=(char*)malloc(sizeof(char)*1);
	double objval;
	double *x = NULL;
	double *y = NULL;
	double *pi = NULL;
	double *slack = NULL;
	double *dj = NULL;
		
	
	env = CPXopenCPLEX(&status);
	if(env==NULL)exit(-1);
	
	status = CPXsetintparam(env, CPX_PARAM_SCRIND, CPX_ON);
	if(status)exit(-1);
	
	status = CPXsetintparam(env, CPX_PARAM_DATACHECK, CPX_ON);
	if(status)exit(-1);
	
	
	lp = CPXcreateprob(env, &status, "bppc");
	if(lp==NULL)exit(-1);
	
	status = CPXsetintparam(env, CPX_PARAM_MIPSEARCH, CPX_MIPSEARCH_TRADITIONAL);
	if(status)exit(-1);
	
	status = CPXsetintparam (env, CPX_PARAM_MIPCBREDLP, CPX_OFF);
	if(status)exit(-1);
	
	
	
		

	
	status=0;
	CPXchgobjsen(env, lp, CPX_MAX);
	
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			obj[i*prob->N+j] = 1.;
			lb[i*prob->N+j] = 0.;
			ub[i*prob->N+j] = 1.;
			coltype[i*prob->N+j] = 'B';
		}
	}
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			obj[(prob->N*prob->N)+i*prob->N+j] = 1.;
			lb[(prob->N*prob->N)+i*prob->N+j] = 0.;
			ub[(prob->N*prob->N)+i*prob->N+j] = 1.;
			coltype[(prob->N*prob->N)+i*prob->N+j] = 'B';
		}
	}
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			obj[2*(prob->N*prob->N)+i*prob->N+j] = 2.;
			lb[2*(prob->N*prob->N)+i*prob->N+j] = 0.;
			ub[2*(prob->N*prob->N)+i*prob->N+j] = 1.;
			coltype[2*(prob->N*prob->N)+i*prob->N+j] = 'B';
		}
	}

		
	status = CPXnewcols(env, lp, cantvar, obj, lb, ub, coltype, NULL);
	if(status)exit(-1);
	
	//Filas tienen como maximo una "no +"
	for(int i=0; i<prob->N; i++){
		rmatbeg[0] = 0;
		rhs[0] = 1.0;
		sense[0] = 'L';
		int count = 0;
		for(int j=0; j<prob->N; j++){
			rmatval[count] = 1.0;
			rmatind[count++] = (prob->N*prob->N)+i*prob->N+j;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+i*prob->N+j;
		}
		status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
		if(status)exit(-1);
	}
	
	//Columnas tienen como maximo una "no +"
	for(int j=0; j<prob->N; j++){
		rmatbeg[0] = 0;
		rhs[0] = 1.0;
		sense[0] = 'L';
		int count = 0;
		for(int i=0; i<prob->N; i++){
			rmatval[count] = 1.0;
			rmatind[count++] = (prob->N*prob->N)+i*prob->N+j;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+i*prob->N+j;
		}
		status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
		if(status)exit(-1);
	}
	
	//Diagonales para la derecha que empiezan en la primera fila
	for(int j=0; j<prob->N; j++){
		int a = 0;
		int b = j;
		rmatbeg[0] = 0;
		rhs[0] = 1.0;
		sense[0] = 'L';
		int count = 0;
		while(a<prob->N&&b<prob->N){
			rmatval[count] = 1.0;
			rmatind[count++] = a*prob->N+b;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+a*prob->N+b;
			a++;
			b++;
		}
		status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
		if(status)exit(-1);
	}
	
	//Diagonales para la derecha que empiezan en la primera columna
	for(int i=1; i<prob->N; i++){
		int a = i;
		int b = 0;
		rmatbeg[0] = 0;
		rhs[0] = 1.0;
		sense[0] = 'L';
		int count = 0;
		while(a<prob->N&&b<prob->N){
			rmatval[count] = 1.0;
			rmatind[count++] = a*prob->N+b;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+a*prob->N+b;
			a++;
			b++;
		}
		status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
		if(status)exit(-1);
	}
	
	//Diagonales para la izquierda que empiezan en la primera fila
	for(int j=0; j<prob->N; j++){
		int a = 0;
		int b = j;
		rmatbeg[0] = 0;
		rhs[0] = 1.0;
		sense[0] = 'L';
		int count = 0;
		while(a<prob->N&&b>=0){
			rmatval[count] = 1.0;
			rmatind[count++] = a*prob->N+b;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+a*prob->N+b;
			a++;
			b--;
		}
		status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
		if(status)exit(-1);
	}
	
	//Diagonales para la izquierda que empiezan en la ultima columna
	for(int i=1; i<prob->N; i++){
		int a = i;
		int b = prob->N-1;
		rmatbeg[0] = 0;
		rhs[0] = 1.0;
		sense[0] = 'L';
		int count = 0;
		while(a<prob->N&&b>=0){
			rmatval[count] = 1.0;
			rmatind[count++] = a*prob->N+b;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+a*prob->N+b;
			a++;
			b--;
		}
		status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
		if(status)exit(-1);
	}
	
	
	
	//Cumplir con lo que ya esta en la grilla
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			if(prob->grid[i][j]=='.')continue;
			if(prob->grid[i][j]=='+'){
				rmatbeg[0] = 0;
				rhs[0] = 1.0;
				sense[0] = 'G';
				int count = 0;
				rmatval[count] = 1.0;
				rmatind[count++] = i*prob->N+j;
				rmatval[count] = 1.0;
				rmatind[count++] = 2*(prob->N*prob->N)+i*prob->N+j;
				status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
				if(status)exit(-1);
			}
			if(prob->grid[i][j]=='x'){
				rmatbeg[0] = 0;
				rhs[0] = 1.0;
				sense[0] = 'G';
				int count = 0;
				rmatval[count] = 1.0;
				rmatind[count++] = (prob->N*prob->N)+i*prob->N+j;
				rmatval[count] = 1.0;
				rmatind[count++] = 2*(prob->N*prob->N)+i*prob->N+j;
				status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
				if(status)exit(-1);
			}
			if(prob->grid[i][j]=='o'){
				rmatbeg[0] = 0;
				rhs[0] = 1.0;
				sense[0] = 'G';
				int count = 0;
				rmatval[count] = 1.0;
				rmatind[count++] = 2*(prob->N*prob->N)+i*prob->N+j;
				status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
				if(status)exit(-1);
			}
		}
	}
	
	//Cada posicion en la grilla tiene como maximo una modelo
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			rmatbeg[0] = 0;
			rhs[0] = 1.0;
			sense[0] = 'L';
			int count = 0;
			rmatval[count] = 1.0;
			rmatind[count++] = i*prob->N+j;
			rmatval[count] = 1.0;
			rmatind[count++] = (prob->N*prob->N)+i*prob->N+j;
			rmatval[count] = 1.0;
			rmatind[count++] = 2*(prob->N*prob->N)+i*prob->N+j;
			status = CPXaddrows(env, lp, 0, 1, count, rhs, sense, rmatbeg, rmatind, rmatval, NULL, NULL);
			if(status)exit(-1);
		}
	}
	////////////////////////////////////////////////////
	
	
	

	
	/////////////////////////////
	status = CPXmipopt(env,lp);
	if(status)exit(-1);
	/////////////////////////////
	
	
	status = CPXgetobjval (env, lp, &objval);
	if ( status ) {
		fprintf (stderr,"No MIP objective value available.  Exiting...\n");
		exit(-1);
	}
	printf ("Valor de la solucion  = %f\n\n", objval);
	
	status = CPXgetbestobjval (env, lp, &objval);
	if ( status ) {
		fprintf (stderr,"No MIP objective value available.  Exiting...\n");
		exit(-1);
	}
	printf ("Valor de la relajacion  = %f\n\n", objval);
	
	
	int cur_numrows=CPXgetnumrows(env,lp);
	int cur_numcols=CPXgetnumcols(env,lp);
	
	x = (double *) malloc(cur_numcols * sizeof(double));
	slack = (double *) malloc(cur_numrows * sizeof(double));
	dj = (double *) malloc(cur_numcols * sizeof(double));
	pi = (double *) malloc(cur_numrows * sizeof(double));
	
	if(x==NULL||slack==NULL||dj==NULL||pi==NULL){
		status = CPXERR_NO_MEMORY;
		fprintf(stderr, "No se pudieron alocar las variables\n");
		exit(-1);
	}
	
	
	status = CPXgetx(env, lp, x, 0, cur_numcols-1);
	if ( status ) {
		fprintf (stderr, "Failed to get optimal integer x.\n");
		exit(-1);
	}
	int var = 0;
	
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			if(x[var]>0.95){
				prob->grid[i][j] = '+';
			}
			var++;
		}
	}
	
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			if(x[var]>0.95){
				prob->grid[i][j] = 'x';
			}
			var++;
		}
	}
	
	for(int i=0; i<prob->N; i++){
		for(int j=0; j<prob->N; j++){
			if(x[var]>0.95){
				prob->grid[i][j] = 'o';
			}
			var++;
		}
	}
	
	prob->best = objval;
	
	return;
}




int main(int argc, char** argv){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		prob = new Problema();
		cin >> prob->N >> prob->M;
		prob->gridOri = vector<vector<char> >(prob->N, vector<char>(prob->N,'.'));
		char c;
		int x,y;
		for(int i=0; i<prob->M; i++){
			cin >> c >> x >> y;
			prob->gridOri[x-1][y-1] = c;
		}
		prob->best = 0;
		prob->grid = prob->gridOri;
		solveMIP();
		
		int diff = 0;
		for(int i=0; i<prob->N; i++){
			for(int j=0; j<prob->N; j++){
				if(prob->grid[i][j]!=prob->gridOri[i][j])diff++;
			}
		}
		cerr << "Case #" << caso << ": " << prob->best << " " << diff << endl;
		for(int i=0; i<prob->N; i++){
			for(int j=0; j<prob->N; j++){
				if(prob->grid[i][j]!=prob->gridOri[i][j]){
					cerr << prob->grid[i][j] << " " << i+1 << " " << j+1 << endl;
				}
			}
		}
		delete prob;
	}
	return 0;
}

