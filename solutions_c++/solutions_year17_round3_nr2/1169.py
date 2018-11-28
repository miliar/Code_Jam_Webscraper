#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

#include <strstream>

using namespace std;




int _tmain( int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cout << "Case #" << NumCase << ": ";
		int Ac,Aj;

		cin >> Ac >> Aj;

		cerr << Ac << '\t' << Aj << endl;

		int Acs[200],Ace[200],Ajs[200],Aje[200];
		for(int i=0;i<Ac;i++) {
			cin >> Acs[i] >> Ace[i];
			cerr << Acs[i] << '\t' << Ace[i] << endl;
		}
		for(int i=0;i<Aj;i++) {
			cin >> Ajs[i] >> Aje[i];
			cerr << Ajs[i] << '\t' << Aje[i] << endl;
		}

		if(Ac+Aj < 2 || Ac == Aj /* i.e. 1 */) cout << 2;
		else {
			if(    (Ac==2 && max(Ace[0],Ace[1])-min(Acs[0],Acs[1]) > 720 && max(Acs[0],Acs[1])-min(Ace[0],Ace[1]) < 720   )
				|| (Aj==2 && max(Aje[0],Aje[1])-min(Ajs[0],Ajs[1]) > 720 && max(Ajs[0],Ajs[1])-min(Aje[0],Aje[1]) < 720) ) cout << 4;
			else cout << 2;
		}

		cout << endl;
	}
 	return 0;
}
