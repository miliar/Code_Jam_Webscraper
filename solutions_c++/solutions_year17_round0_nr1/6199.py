#include <iostream>
#include <list>
#include <fstream>
#include <string>

using namespace std;

class Case
{
public:
	string cad;
	int k;

	Case()
	{
		k = 0;
	}
};

class SolutionA
{
public:
	list<Case*> *N;

	//Constructor
	SolutionA()
	{
		string cadena;
		int casos = 0;
		char linea[1010];
		N = new list<Case*>;
		//Leer el input
		ifstream fe("input.txt");
		int index = 0;

		while (!fe.eof()) {
			if (index == 0)
			{
				fe.getline(linea, 1010);
				cadena = linea;
				casos = stoi(cadena, nullptr, 10);
			}
			else
			{
				fe.getline(linea, 1010);
				cadena = linea;
				Case *caso = new Case;
				int whiteSpace = cadena.find(' ');
				int lengthCadena = cadena.size();
				int length = lengthCadena - whiteSpace;
				string K = cadena.substr(whiteSpace, length);
				int k = stoi(K, nullptr, 10);
				string cadenaCakes = cadena.substr(0, whiteSpace);

				caso->k = k;
				caso->cad = cadenaCakes;

				//Añadimos a la  lista
				N->push_back(caso);
			}
			index++;
		}
		fe.close();
	}



	//Mostrar los datos en la consola
	void printCases()
	{
		int NumCase = 1;
		for (std::list<Case*>::iterator it = N->begin(); it != N->end(); ++it)
		{
			Case * c = *it;
			cout << "Case " << NumCase << ": cadena:" << c->cad << " k: " << c->k << endl;
			NumCase++;
		}
	}

	void Solves()
	{
		ofstream  output("output.txt");
		int NumCase = 1;
		for (std::list<Case*>::iterator it = N->begin(); it != N->end(); ++it)
		{
			Case * c = *it;
			int flips = solve(c);
			//Print 
			if (flips == -1) {
				output << "Case #" << NumCase << ": " << "IMPOSSIBLE" << endl;
			}
			else {
				output << "Case #" << NumCase << ": " << flips << endl;
			}
			NumCase++;
		}
		output.close();
	}

	int solve(Case * c)
	{
		int flips = 0;
		bool ciclo = true;
		int afterindex = -1;
		int index = 0;
		int numCliclos = 0;
		while (ciclo)
		{
			index = findFirstMinus(c->cad);
			if (afterindex < index) {
				afterindex = index;
				if (index == -1) {
					if (flips > 0) return flips;
					return 0;
				}
				else {
					if (canFlipNCakes(sizeCadena(c->cad), index, c->k))
					{
						string nuevaCadena = FlipNCakes(c->cad, index, c->k);
						c->cad = nuevaCadena;
						flips++;
					}
					else return -1;
				}
			}
			else {
				if (afterindex == index) {
					afterindex = index;
					numCliclos++;
					if (numCliclos < 4) {
						if (index == -1) {
							if (flips > 0) return flips;
							return 0;
						}
						else {
							if (canFlipNCakes(sizeCadena(c->cad), index, c->k))
							{
								string nuevaCadena = FlipNCakes(c->cad, index, c->k);
								c->cad = nuevaCadena;
								flips++;
							}
							else return -1;
						}
					}
					else { ciclo = false; }
				}
				else {
					if (flips > 0) return flips;
					return -1;
				}
			}
		}
		return -1;
	}

	string FlipNCakes(string cadena, int index, int k)
	{
		int lastIndex = index + k - 1;
		int size = sizeCadena(cadena);
		for (int i = index; i <= lastIndex; i++)
		{
			if (cadena[i] == '-') {
				cadena[i] = '+';
			}
			else {
				cadena[i] = '-';
			}
		}
		return cadena;
	}

	bool canFlipNCakes(int size, int index, int k)
	{
		int lastIndex = size - 1;
		int last = index + k - 1;
		if (last > lastIndex) return false;
		return true;
	}

	bool allPositive(string cadena)
	{
		bool resultado = false;
		//Todo
		return resultado;
	}

	int findFirstMinus(string cadena)
	{
		int index = 0;
		for (int i = 0; i <= (sizeCadena(cadena) - 1); i++)
		{
			if (cadena[i] == '-') return i;
		}
		return -1;
	}

	int sizeCadena(string cadena)
	{
		return cadena.size();
	}



};

int TestSolutionA()
{
	char key;
	SolutionA *solucion = new SolutionA;
	solucion->Solves();

	cout << "print any key to continue" << endl;
	cin >> key;

	return 0;
}



int main()
{	
	TestSolutionA();
	return 0;
}
