#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>
#include<iterator>

// None: 0
// +: 1
// x: 2
// o: 3

using namespace std;

class Cell;

// Model class
class Model{

	public:
	char type = ' ';
	Cell *cell;
	bool isNew = false;

	Model(char type_, Cell *cell_){
		type = type_;
		cell = cell_;
	}
};

// Row, Column or Diagonal
class RCD{

	public:
	bool plus = true;
	bool cross = true;
	bool circle = true;

	// Constructor
	RCD(){
		
	}
};

// A cell of the grid
class Cell{
	
	public:
	RCD *row = nullptr;
	RCD *column = nullptr;
	RCD *diagonal1 = nullptr;
	RCD *diagonal2 = nullptr;
	Model *model = nullptr;

	int R;
	int C;

	//Constructor
	Cell(int R_, int C_): R(R_), C(C_) {}

	void setModel(Model* model_){
		model = model_;
		if (model->type=='+' || model->type=='o'){
			if(diagonal1){
				diagonal1->plus=false;
				diagonal1->circle=false;
			}
			if(diagonal2){
				
				diagonal2->plus=false;
				diagonal2->circle=false;
			}
		}
		if (model->type=='x' || model->type=='o'){
			row->cross = false;
			row->circle = false;
			column->cross = false;
			column->circle = false;
		}
	}

	bool canSet(char type){
		if (type=='+'){
			if (!row->plus) return false;
			if (!column->plus) return false;
			if (diagonal1 && !diagonal1->plus) return false;
			if (diagonal2 && !diagonal2->plus) return false;
			return true;
		}
		if (type=='x'){			
			if (!row->cross) return false;
			if (!column->cross) return false;
			if (diagonal1 && !diagonal1->cross) return false;
			if (diagonal2 && !diagonal2->cross) return false;
			return true;
		}
		if (type=='o'){
			if (!row->circle) return false;
			if (!column->circle) return false;
			if (diagonal1 && !diagonal1->circle) return false;
			if (diagonal2 && !diagonal2->circle) return false;
			return true;
		}
		return false;
	}

	void display(){
		cout<<"Cell ("<<R<<", "<<C <<") o - "<<canSet('o')<<", x - "<<canSet('x')<<", + - "<<canSet('+')<<" Current Model: ";
		if (model) cout<<model->type<<endl; else cout<<"None"<<endl;

	}

};

// Grid
class Grid{

	public:
	vector<vector<Cell*>> cell;
	vector<Model*> model;
	vector<Model*> newModels;
	int value = 0;

	// Size of the grid NxN
	int N;

	// Number of preseted models
	int M;
	// Constructor
	Grid(int N_, int M_): N(N_), M(M_){
		cell = vector<vector<Cell*>>(N_);
		for (int i = 0; i<N_; i++){
			cell[i] = vector<Cell*>(N_);
			for (int j = 0; j<N_; j++){
				cell[i][j] = new Cell(i,j);
			}
		}
		init();
	}

	void init(){
		
		for (int i = 0; i<N; i++){
			RCD *row = new RCD();
			RCD *column = new RCD();
			RCD *diagonal1 = new RCD();
			RCD *diagonal1_ = new RCD();
			RCD *diagonal2 = new RCD();
			RCD *diagonal2_ = new RCD();
			
			// Setting row i
			for (int j = 0; j<N; j++) cell[i][j]->row = row;

			// Setting column i
			for (int j = 0; j<N; j++) cell[j][i]->column = column;


			// Setting diagonal 1
			for (int j = 0; j<N-i; j++){
				cell[j][j+i]->diagonal1 = diagonal1;
				cell[j+i][j]->diagonal1 = diagonal1_;
			}

			// Setting diagonal 2
			for (int j = 0; j<i+1; j++){
				cell[j][i-j]->diagonal2 = diagonal2;
				cell[N-(1+i-j)][N-(j+1)]->diagonal2 = diagonal2_;
			}
			/*
			// Setting diagonals
			if (i==0){
				for (int j = 0; j<N; j++) cell[j][j]->diagonal1 = diagonal1;
			}
			else if (i==N-1){
				for (int j = 0; j<N; j++) cell[j][N-j-1]->diagonal2 = diagonal2;
			}
			else{
				for (int j = 0; j<N-i; j++){
					cout<<j<<", "<<j+i<<endl;
					cell[j][j+i]->diagonal1 = diagonal1;
				}
				for (int j = 0; j<N-i; j++) cell[j+i][j]->diagonal2 = diagonal2;
			}
			*/

		}


	}

	void addModel(char type, int R, int C){
		Model *model_ = new Model(type, cell[R][C]) ;
		model.push_back( model_ );
		if (model.size() > M) model_->isNew = true;
		cell[R][C]->setModel(model_);

		if (type=='x' || type=='+') value+=1;
		if (type=='o') value+=2;
	}



	void updateModel(Cell *cell){
		cell->model->type = 'o';
		cell->model->isNew = true;
		cell->setModel(cell->model);
		value++;
	}

	void displayModels(){
		//for (auto m: model) cout<<"Model "<<m->type<<" in: "<<m->cell->R<<", "<<m->cell->C<<endl;

		/*for (int i = 0; i<N; i++) for (int j = 0; j<N; j++){
			if (cell[i][j]->model) cout<<"Model "<<cell[i][j]->model->type<<" in: "<<cell[i][j]->R<<", "<<cell[i][j]->C<<endl;
		}*/

		for (int i = 0; i<N; i++){
			for (int j = 0; j<N; j++) cell[i][j]->display();
				
			cout<<endl;
		}
	}


	// Updating/Adding
	void updateModels(){
		for (int i = 0; i<N; i++) for (int j = 0; j<N; j++){
			if (cell[i][j]->model) if (cell[i][j]->model->type != 'o') if (cell[i][j]->canSet('x') || cell[i][j]->canSet('+')) updateModel(cell[i][j]);

		}
	}

	void addPlusses(){
		for (int i = 0; i<N; i++) for (int j = 0; j<N; j++) if (cell[i][j]->canSet('+') && !(cell[i][j]->model) ) addModel('+',i,j);
	}

	void addCrosses(){
		for (int i = 0; i<N; i++) for (int j = 0; j<N; j++) if (cell[i][j]->canSet('x') && !(cell[i][j]->model)) addModel('x',i,j);
	}

	void addCircles(){
		for (int i = 0; i<N; i++) for (int j = 0; j<N; j++) if (cell[i][j]->canSet('o') && !(cell[i][j]->model)) addModel('o',i,j);
	}

	void solve(){
		for (int i = 0; i<N; i++) if (cell[0][i]->canSet('+') && !(cell[0][i]->model) ) addModel('+',0,i);
		for (int i = 0; i<N; i++) if (cell[N-1][i]->canSet('+') && !(cell[N-1][i]->model) ) addModel('+',N-1,i);
		addCrosses();
		addPlusses();	
		addCircles();	
		updateModels();

		for (auto m: model) if(m->isNew) newModels.push_back(m);
	}
	void solve1(){	
		addCrosses();
		for (int i = 0; i<N; i++) if (cell[0][i]->canSet('+') && !(cell[0][i]->model) ) addModel('+',0,i);
		for (int i = 0; i<N; i++) if (cell[N-1][i]->canSet('+') && !(cell[N-1][i]->model) ) addModel('+',N-1,i);
		updateModels();
		addCircles();	
		addPlusses();	
		addCrosses();
		addCircles();	
		updateModels();

	}
	void solve2(){
		updateModels();
		addCircles();	
		addCrosses();
		addPlusses();	
	}
	void solve3(){
		updateModels();
		addCrosses();	
		addCircles();
		addPlusses();	
		updateModels();
	}

};


int main(int argc, char **argv){

	ifstream input(argv[1], ios::in);
	ofstream output;
	output.open("output", ios::out);	
	
	int T; input >> T;
	for (int i = 0; i<T; i++){
		cout<<"Teste case: "<<i<<" - ";
		int N;
		int M;
		input >> N >> M;
		Grid grid(N,M);
		Grid grid1(N,M);

		for (int j = 0; j<M; j++){
			char type; int R, C;
			input >> type >> R >> C;
			grid.addModel(type,R-1,C-1);
			grid1.addModel(type,R-1,C-1);
		}
		grid.solve();
		
		output <<"Case #"<<i+1<<": "<<grid.value<<" "<<grid.newModels.size()<<endl;
		for (auto m: grid.newModels) output<<m->type<<" "<<m->cell->R+1<<" "<<m->cell->C+1<<endl;
		cout<<grid.value<<" max "<<grid.newModels.size()<<" "<<M<<endl;
	}
	
	input.close();
	output.close();
}



