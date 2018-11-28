#include <iostream>
 
using namespace std;


int main(void) {
	int t;
	cin >> t;

	for (int i =0; i < t; i++){
		int r, c;
		cin >> r;
		cin >> c;
		char charmap[r][c];
		
		for (int x=0; x < r; x++){
			for (int y=0; y< c; y++){
				cin >> charmap[x][y];
			}
		}

		char fill = '?';
		for (int x=0; x < r; x++){
			for (int y=0; y< c; y++){
				//if 00 isn't ?, fill to the right until it hit something, or the end.
				char current=charmap[x][y];
				if (current=='?'){
					if (fill=='?'){
						//find what to fill
						for (int z=y; z<c; z++){
							if (charmap[x][z]!='?'){
								fill=charmap[x][z];
								break;
							}
						}
						//if nothing found... do nothing, will copy up copy down later
						if (fill=='?'){
							//empty row
							break;
						}
					}
					//fill
					charmap[x][y]=fill;

			

				} else {
					fill=current;
				}
			}
			fill='?';
		}


		//copy down, copy up.
		if (r>=1){
			for (int x=1; x < r; x++){
				if (charmap[x][0]=='?'){
					for (int y=0; y< c; y++){
						if (charmap[x-1][y]!='?')
							charmap[x][y]=charmap[x-1][y];
					}
				}
			}
			for (int x=r-2; x>=0; x--){
				if (charmap[x][0]=='?'){
					for (int y=0; y< c; y++){
						if (charmap[x+1][y]!='?')
							charmap[x][y]=charmap[x+1][y];
					}
				}
			}
		}

		cout << "Case #" <<  i+1 << ": " << endl;;

		for (int x=0; x < r; x++){
			for (int y=0; y< c; y++){
				cout <<charmap[x][y];
			}

			cout << endl;
		}


	}

	return 0;

}