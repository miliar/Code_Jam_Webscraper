#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int testCase = 1; testCase <= T; testCase++){
		cout << "Case #" << testCase << ": ";
		int Ac, Aj;
		cin >> Ac; cin >> Aj;
		vector <int> S(24 * 60, 0);
		int Afree = 720;
		int Bfree = 720;
		for(int i = 0; i < Ac; i++){
			int C, D;
			cin >> C; cin >> D;
			for(int j = C; j < D; j++) S[j] = 1;
			Afree -= D - C;
		}
		for(int i = 0; i < Aj; i++){
			int C, D;
			cin >> C; cin >> D;
			for(int j = C; j < D; j++) S[j] = -1;
			Bfree -= D - C;
		}
		int i = 0;
		while(S[i] == 0) i++;
		vector <int> Aholes; 
		vector <int> Bholes; 
		vector <int> ABholes;
		int length = 1;
		int prev = S[(i + 1439) % 1440];
		for(int j = i; j < i + 24 * 60; j++){
			if(S[j % 1440] != S[(j + 1) % 1440]){
				if(S[j % 1440] == 0){
					if(prev == 1 && S[(j + 1) % 1440] == 1) Aholes.push_back(length);
					else if(prev == -1 && S[(j + 1) % 1440] == -1) Bholes.push_back(length);
					else ABholes.push_back(length);
				}
				else if(S[(j + 1) % 1440] != 0) ABholes.push_back(0);
				prev = S[j % 1440];
				length = 0;
			}
			length++;
		}
		sort(Aholes.begin(), Aholes.end(), [&](int aa, int bb){return aa >  bb;});
		sort(Bholes.begin(), Bholes.end(), [&](int aa, int bb){return aa >  bb;});
		//cout << Afree << " " << Bfree << " free\n";
		while(!Aholes.empty() && Afree >= Aholes.back()){
			Afree -= Aholes.back();
			Aholes.pop_back();
		}
		while(!Bholes.empty() && Bfree >= Bholes.back()){
			Bfree -= Bholes.back();
			Bholes.pop_back();
		}
		/*if(Afree > 0 && !Aholes.empty()){
			Aholes.back() -= Afree;
			Afree = 0;
		}
		if(Bfree > 0 && !Bholes.empty()){
			Bholes.back() -= Bfree;
			Bfree = 0;
		}
		if(Afree > 0 && Bfree > 0) cout << Aholes.size() + Bholes.size() + ABholes.size();
		else if(Afree == 0){
			while(!Aholes.empty() && Bfree > 0)
		}*/
		cout << 2 * Aholes.size() + 2* Bholes.size() + ABholes.size();
		
		/*for(int j = 0; j < Aholes.size(); j++) cout << Aholes[j] << " ";
		cout << endl;
		for(int j = 0; j < Bholes.size(); j++) cout << Bholes[j] << " ";
		cout << endl;
		for(int j = 0; j < ABholes.size(); j++) cout << ABholes[j] << " ";
		cout << endl;*/
		cout << endl;
	}
  return 0;
}
