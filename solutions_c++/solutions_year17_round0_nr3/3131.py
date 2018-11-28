#include <iostream>
#include <deque>

using namespace std;

int main(int argc, char const *argv[])
{
	std::deque<long long int> sets;
	std::deque<long long int> cantidad;

	long long int personas, stalls, cont, mitad;
	int casos;	cin >> casos;

	for (int i = 1; i <= casos; ++i)
	{
		sets.clear();
		cantidad.clear();

		cin >> stalls >> personas;
		sets.push_back(stalls);
		cantidad.push_back(1);
		while( personas > cantidad.front() ){

			personas -= cantidad.front();
			mitad = sets.front()/2;

			if (sets.front() == 1)	;
			else if ( sets.front()%2 == 0){

				for (cont = 0; cont < sets.size() && mitad != sets[cont]; ++cont)	;

				if (cont >= sets.size())
				{
					sets.push_back(mitad);
					cantidad.push_back(cantidad.front());
				}else{
					cantidad[cont] += cantidad.front();
				}


				for (cont = 0; cont < sets.size() && mitad-1 != sets[cont]; ++cont)	;

				if (cont >= sets.size())
				{
					sets.push_back(mitad-1);
					cantidad.push_back(cantidad.front());
				}else{
					cantidad[cont] += cantidad.front();
				}

			}else{
				
				for (cont = 0; cont < sets.size() && mitad != sets[cont]; ++cont)	;

				if (cont >= sets.size())
				{
					sets.push_back(mitad);
					cantidad.push_back(cantidad.front()*2);
				}else{
					cantidad[cont] += cantidad.front()*2;
				}
			}

			sets.pop_front();
			cantidad.pop_front();

			while( !(sets.front()) ){
				sets.pop_front();
				cantidad.pop_front();
			}
		}//Fin de while personas > cantidad.front()

		if (sets.front() == 1)
			cout << "Case #" << i << ": 0 0\n";
		else if (sets.front() % 2 == 0)
			cout << "Case #" << i << ": " << sets.front()/2 << ' ' <<  sets.front()/2-1 << '\n';
		else
			cout << "Case #" << i << ": " << sets.front()/2 << ' ' << sets.front()/2 << '\n';


	}

	return 0;
}
