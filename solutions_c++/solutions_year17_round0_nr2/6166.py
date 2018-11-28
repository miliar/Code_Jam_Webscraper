#include <iostream>
#include <list>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

class Case
{
public:
	string number;

	Case()
	{

	}
};

class SolutionB
{
public:
	list<Case*> *N;

	//Constructor
	SolutionB()
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
				caso->number = cadena;
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
			cout << "Case " << NumCase << ": number:" << c->number << endl;
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
			string tidyNumber = solve(c);
			//Print 			
			output << "Case #" << NumCase << ": " << tidyNumber << endl;
			NumCase++;
		}
		output.close();
	}

	string solve(Case * c)
	{
		string tidyNumber;

		bool estaBalanceado = false;
		//Todo
		while (estaBalanceado == false) {

			int nextIndex = 0;
			int index = 0;
			int size = getsize(c->number);
			while (getNextIndex(index, size) != -1) {

				nextIndex = getNextIndex(index, size);
				string nuevoNumber = calibrar(index, nextIndex, c->number);
				c->number = nuevoNumber;
				index++;
			}
			estaBalanceado = validar(c->number);
		}
		tidyNumber = c->number;
		tidyNumber = trim(tidyNumber);/*
									  long double tidy = stold(tidyNumber);
									  string final = std::to_string(tidy);*/

		return tidyNumber;
	}

	string trim(string number)
	{
		bool primerosCeros = true;
		string reemplazo = number;
		for (int i = 0; i <= (reemplazo.size() - 1); i++)
		{
			char caracterIndex[1] = { reemplazo[i] };
			int digitIndex = atoi(caracterIndex);
			if (digitIndex == 0)
			{
				reemplazo = string(reemplazo.erase(i, 1));
				i = 0;
			}
			else { break; }
		}
		return reemplazo;
	}

	bool validar(string number)
	{
		bool resultado = true;
		if (number.size() == 1) return true;
		else {
			for (int i = 0; i <= (number.size() - 2); i++)
			{
				char caracterIndex[1] = { number[i] };
				char caracterNext[1] = { number[i + 1] };
				int digitIndex = atoi(caracterIndex);
				int digitNext = atoi(caracterNext);
				if (digitIndex > digitNext) return false;
			}
		}
		return resultado;
	}

	string calibrar(int index, int next, string cadena)
	{
		char caracterIndex[1] = { cadena[index] };
		char caracterNext[1] = { cadena[next] };
		int digitIndex = atoi(caracterIndex);
		int digitNext = atoi(caracterNext);
		char buffer[10];

		if (digitIndex > digitNext)
		{
			digitIndex--;
			digitNext = 9;
			string a = std::to_string(digitIndex);
			string b = std::to_string(digitNext);
			cadena[index] = *a.c_str();
			for (int i = next; i <= (cadena.size() - 1); i++) {
				cadena[i] = *b.c_str();
			}
		}
		return cadena;
	}

	int getsize(string number)
	{
		return number.size();
	}

	int getNextIndex(int index, int size)
	{
		int nextIndex = index + 1;
		if (nextIndex > (size - 1)) return -1;
		else return nextIndex;
	}


};


using namespace std;

int TestSolutionB()
{
	char key;
	SolutionB *solucion = new SolutionB;
	//solucion->printCases();
	solucion->Solves();

	cout << "print any key to continue" << endl;
	cin >> key;

	return 0;
}



int main()
{
	TestSolutionB();
	return 0;
}