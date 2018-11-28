#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<set>
using namespace std;

struct elemento {
	long long int cardinalidad;
	long long int longitud;
	elemento(long long int c, long long int l) {
		cardinalidad = c;
		longitud = l;
	}
	elemento(const elemento&otro) {
		cardinalidad = otro.cardinalidad;
		longitud = otro.longitud;
	}
	bool operator<(const elemento&otro) const {
		return longitud > otro.longitud;
	}
	bool operator==(const elemento&otro) const {
		return longitud == otro.longitud;
	}
};

struct intervalo {
	int longitud;
	int posenlaqueempieza;
	int posenlaqqueacaba;
	intervalo(int pos, int lon) {
		longitud = lon;
		posenlaqueempieza = pos;
		posenlaqqueacaba = pos + lon - 1;
	}
	bool operator<(const intervalo&otro) const {
		if (longitud > otro.longitud)return true;
		else if (longitud == otro.longitud) {
			return posenlaqueempieza < otro.posenlaqueempieza;
		}
		else return false;
	}
};

const int VACIO = 0;
const int OCUPADO = 1;

int min(int a, int b) {
	if (a < b)return a;
	else return b;
}

int max(int a, int b) {
	if (a > b)return a;
	else return b;
}

int hallarposenlaquedivido(int lon) {
	return (lon - 1) / 2;
}


void resolver2(long long int n, long long int k, ofstream&salida) {
	set<elemento>lista;
	set<elemento>::iterator a;
	lista.insert({1,n});
	while (k > 0) {
		elemento caso = *lista.begin();
		lista.erase(lista.begin());
		switch (caso.longitud % 2) {
		case 0: {
			if (lista.count({ 0,caso.longitud / 2 }) != 0) {
				elemento elem =  *(lista.find({ 0,caso.longitud / 2 }));
				elem.cardinalidad += caso.cardinalidad;
				lista.erase(lista.find({ 0,caso.longitud / 2 }));
				lista.insert(elem);
			}
			else lista.insert({ caso.cardinalidad ,caso.longitud / 2 });
			if (lista.count({ 0,caso.longitud / 2 - 1 }) != 0) {
				elemento elem = *(lista.find({ 0,caso.longitud / 2 - 1 }));
				elem.cardinalidad += caso.cardinalidad;
				lista.erase(lista.find({ 0,caso.longitud / 2 - 1}));
				lista.insert(elem);
			}
			else lista.insert({ caso.cardinalidad, caso.longitud / 2 - 1 });
			if (k - caso.cardinalidad <= 0) {
				salida << caso.longitud / 2 << ' ' << caso.longitud / 2 - 1 << '\n';
			}
			k -= caso.cardinalidad;
		}break;
		case 1: {
			if (lista.count({ 0,caso.longitud / 2 }) != 0) {
				elemento elem = *(lista.find({ 0,caso.longitud / 2 }));
				elem.cardinalidad += 2*caso.cardinalidad;
				lista.erase(lista.find({ 0,caso.longitud / 2 }));
				lista.insert(elem);
			}
			else lista.insert({ 2*caso.cardinalidad, caso.longitud / 2 });
			if (k - caso.cardinalidad <= 0) {
				salida << caso.longitud / 2 << ' ' << caso.longitud / 2 << '\n';
			}
			k -= caso.cardinalidad;
		}break;
		}
	}
}

void resolver(int n, int k, ofstream&salida) {
	set<intervalo>lista;
	int pos;
	lista.insert({ 1, n});//empieza en el 1(incluido) y tiene longitud n, es decir acaba en 0+n+1
	for (int ctrl = 0; ctrl < k-1; ctrl++) {
		intervalo i = *lista.begin();
		lista.erase(i);
		pos = i.posenlaqueempieza + hallarposenlaquedivido(i.longitud);//posicion en la que inserto
		/*if (pos - i.posenlaqueempieza > 0) {
			lista.insert({i.posenlaqueempieza+1,-i.posenlaqueempieza+1+pos});//insertamos intervalo izquierdo
		}
		if (i.posenlaqueempieza + i.longitud - 1 - pos > 0) {
			lista.insert({pos+1,i.posenlaqueempieza+i.longitud-1-pos});
		}*/
		switch (i.longitud % 2) {
		case 1: {
			if (pos - i.posenlaqueempieza > 0)lista.insert({i.posenlaqueempieza,i.longitud/2});
			if (i.posenlaqqueacaba - pos > 0)lista.insert({ pos + 1,i.longitud / 2 });
		}break;
		case 0: {
			if (pos - i.posenlaqueempieza > 0)lista.insert({ i.posenlaqueempieza,	(i.longitud / 2) -1 });
			if (i.posenlaqqueacaba - pos > 0)lista.insert({ pos + 1,i.longitud / 2 });
		}break;
		}
	}
	intervalo i = *lista.begin();
	switch (i.longitud % 2) {
	case 0: salida << i.longitud / 2 << ' ' << i.longitud / 2 - 1 << '\n'; break;
	case 1: salida << i.longitud / 2 << ' ' << i.longitud / 2 << '\n'; break;
	}
}

int main() {
	int casos;
	ofstream salida;
	ifstream entrada;
	entrada.open("C-large.in");
	salida.open("output.txt");
	long long int n, k;
	entrada >> casos;
	for (int ctrl = 0; ctrl < casos; ctrl++) {
		entrada >> n >> k;
		salida << "Case #" << ctrl + 1 << ": ";
		resolver2(n, k, salida);
	}
}