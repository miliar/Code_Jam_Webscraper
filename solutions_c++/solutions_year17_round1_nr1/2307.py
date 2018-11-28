#include <iostream>
#include <fstream>
using namespace std;


int t;

int rows, columns;

char grid[30][30];

void replace(char which, char with) {
	for(int i = 0; i < rows; i ++) {
		for (int j = 0; j < columns; j++){
			if(grid[i][j] == which) {
				grid[i][j] = with;
			}
		}
	}
}

void show(){
	for(int i = 0;i<rows;i++){
	for(int j=0;j<columns;j++)
	{
		cout<<grid[i][j];
	}
	cout<<endl;
	}
}

void fshow(ofstream& out){
	for(int i = 0;i<rows;i++){
	for(int j=0;j<columns;j++)
	{
		out<<grid[i][j];
	}
	out<<endl;
	}
}



void expand() {
	// Try to expand horizontally
		for(int i = 0; i < rows; i++) {
			char firstChar = ' ';
			for (int j = 0; j < columns; j++){
				if (grid[i][j] != ' ') {
					firstChar = grid[i][j];
					break;
				}
			}
			
			if(firstChar == ' ')
				continue;
			
			//Left to right completing cells until firstChar is seen
			int j;
			for(j = 0;grid[i][j] != firstChar;j++) {
				grid[i][j] = firstChar;
			}
			
			for(;j + 1 < columns;j++) {
				char currentChar = grid[i][j];
				if( grid[i][j+1] == ' '  )
					grid[i][j+1] = currentChar;
				else
					currentChar = grid[i][j+1];
			}		
		}
}

void flip() {
	char newGrid[30][30];
	for(int i = 0; i < rows; i++)
	for(int j = 0;j<columns;j++){
		newGrid[j][i] = grid[i][j];
	}
	int t = rows;
	rows = columns;
	columns = t;
	
	// copy new grid
	for(int i = 0; i < rows; i++)
	for(int j = 0;j<columns;j++){
		grid[i][j] = newGrid[i][j];
	}
}

int main() {
	ifstream in ("a.in");
	ofstream out ("a.out");
	
	in>>t;
	int problemNumber = 0;
	while(problemNumber++<t) {
		in>>rows>>columns;
		for(int i = 0; i < rows; i ++) {
			string row;
			in>>row;
			for (int j = 0; j < columns; j++){
				char cell = row[j];
				if (cell == '?')
					cell = ' ';
				grid[i][j] = cell;
					
			}
		}
		
		/*cout<<grid[0][0]<<endl;
	
		replace('a', 'b');
		
		cout<<grid[2][2];*/
		
		expand();
		
		//show();
		
		flip();
		
		//show();
		
		expand();
		
		flip();
		
		out<<"Case #"<<problemNumber<<":"<<endl;
		
		fshow(out);
		
		// Seems to be working fine
		//*/
		
		// Try to expand vertically
		
		
	}	
}
