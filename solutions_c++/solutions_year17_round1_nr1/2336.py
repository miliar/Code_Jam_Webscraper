#include <iostream>

using namespace std ;

void fill_lines (char** tab, int hauteur, int largeur) {
	for (int i=0 ; i<hauteur ; i++) {
		for (int j=0 ; j<largeur ; j++) {
			if (tab[i][j] != '?') {
				int k, l, v ;
				v = tab[i][j] ;
				k = j+1 ;
				l = j-1 ;
				while (tab[i][k] == '?' && k < largeur) {
					tab[i][k] = v ;
					k++ ;
				}
				while (tab[i][l] == '?' && l >= 0) {
					tab[i][l] = v ;
					l-- ;
				}
			}
		}
	}
}

void fill_empty (char** tab, int hauteur, int largeur) {
	for (int i=0 ; i<hauteur ; i++) {
		if (tab[i][0] != '?') {
			int k , l ;
			k = i+1 ;
			l = i-1 ;
			if (k<hauteur) {
				while (tab[k][0] == '?' && k<hauteur) {
					for (int e=0 ; e<largeur ; e++) {
						tab[k][e] = tab[k-1][e] ;
					}
					k++ ;
					if (k>=hauteur) break ;
				}	
			}
			if (l>=0) {
				while (tab[l][0] == '?' && l>=0) {
					for (int e=0 ; e<largeur ; e++) {
						tab[l][e] = tab[l+1][e] ;
					}
					l-- ;
					if (l<0) break ;
				}	
			}
		}
	}
}

int main (void) {
	int TNB ; int h ; int l ;
	char **tab ;
	cin >> TNB ;
	for (int i=1 ; i<= TNB ; i++) {
		cin >> h >> l ;
		tab = new char* [h] ;
		for (int k=0 ; k<h ; k++) {
			tab[k] = new char[l] ;
		}
		for (int k=0 ; k<h ; k++) {
			for (int f=0 ; f<l ; f++) {
				cin >> tab[k][f] ;
			}
		}
		fill_lines (tab, h, l) ;
		fill_empty (tab, h, l) ;
		cout << "Case #" << i << ":" << endl ;
		for (int k=0 ; k<h ; k++) {
			for (int f=0 ; f<l ; f++) {
				cout << tab[k][f] ;
			}
			cout << endl ;
		}
		for (int e=0 ; e<h ; e++) {
			delete [] tab[e] ;
		}
		delete [] tab ;
	}
	return 0;
}