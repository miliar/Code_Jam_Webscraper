#include <bits/stdc++.h>
using namespace std;

vector <pair <int, int> > hopcroftCarp(const vector <vector <int> >& adjU, const vector <vector <int> >& adjV){
	int N = adjU.size();
	int M = adjV.size();
	vector <int> pairU(N, -1);
	vector <int> pairV(M, -1);
	while(true){
		vector <int> layerU(N, -1);
		vector <int> layerV(M, -1);
		queue <int> Q;
		queue <int> freeV;
		int maxLayer = M + N;
		for(int i = 0; i < N; i++){
			if(pairU[i] == -1){
				layerU[i] = 0;
				for(auto it = adjU[i].begin(); it != adjU[i].end(); ++it){
					if(layerV[*it] < 0){
						layerV[*it] = 1;
						if(pairV[*it] == -1){
							freeV.push(*it);
							maxLayer = 1;
						}
						else if(freeV.empty()) Q.push(*it);
					}
				}
			}
		}
		while(!Q.empty()){
			int v = Q.front();
			Q.pop();
			if(layerV[v] < maxLayer){
				int u = pairV[v];
				layerU[u] = layerV[v] + 1;
				for(auto it = adjU[u].begin(); it != adjU[u].end(); ++it) if(*it != v){
					if(layerV[*it] < 0){
						layerV[*it] = layerV[v] + 2;
						if(pairV[*it] == -1){
							freeV.push(*it);
							maxLayer = layerV[v] + 2;
						}
						else if(freeV.empty()) Q.push(*it);
					}
				}
			}
		}
		if(freeV.empty()) break;
		int np = 0;
		while(!freeV.empty()){
			int v = freeV.front();
			freeV.pop();
			stack <int> S;
			vector <int> path(maxLayer + 1, -1);
			S.push(v);
			while(!S.empty()){
				int s = S.top();
				S.pop();
				int layer = layerV[s];
				path[layer] = s;
				layerV[s] = -1;
				if(layer != maxLayer){
					path[layer + 1] = pairV[s];
					layerU[pairV[s]] = -1;
				}
				for(auto it = adjV[s].begin(); it != adjV[s].end(); ++it) if(*it != pairV[s] && layerU[*it] == layer - 1){
					if(layerU[*it] == 0){
						path[0] = *it;
						layerU[*it] = -1;
						break;
					}
					if(layerV[pairU[*it]] == layer - 2) S.push(pairU[*it]);
				}
				if(path[0] >= 0) break;
			}
			if(path[0] >= 0){
				np++;
				for(int i = 0; i < maxLayer; i += 2){
					pairU[path[i]] = path[i + 1];
					pairV[path[i + 1]] = path[i];
				}
			}
		}
	}
	vector <pair <int, int> > ret;
	for(int i = 0; i < pairU.size(); i++) if(pairU[i] >= 0) ret.push_back(make_pair(i, pairU[i]));
	return ret;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int N, M;
		cin >> N; cin >> M;
		vector <vector <int> > B(N, vector <int>(N, 0));
		set <int> missR, missC;
		for(int i = 0; i < N; i++){
			missR.insert(i);
			missC.insert(i);
		} 
		int points = 0;
		for(int i = 0; i < M; i++){
			char model;
			int R, C;
			cin >> model >> R >> C;
			R--; C--;
			switch(model){
				case 'x': B[R][C] = 1; points++; break;
				case '+': B[R][C] = 2; points++; break;
				case 'o': B[R][C] = 3; points += 2;
			}
			if(B[R][C] % 2){
				missR.erase(R);
				missC.erase(C);
			}
		}
		vector <vector <int> > Bnew = B;
		auto itR = missR.begin(); auto itC = missC.begin();
		while(itR != missR.end()){
			Bnew[*itR][*itC]++;
			points++;
			++itR; ++itC;
		}
		unordered_set <int> banUp, banDown;
		for(int r = 0; r < N; r++) for(int c = 0; c < N; c++) if(B[r][c] / 2){
			int dUp = r + c;
			int dDown = r - c + N - 1;
			banUp.insert(dUp);
			banDown.insert(dDown);
		}
		vector <vector <int> > adjU(2 * N - 1);
		vector <vector <int> > adjV(2 * N - 1);
		for(int r = 0; r < N; r++) for(int c = 0; c < N; c++) if(B[r][c] / 2 == 0){
			int dUp = r + c;
			int dDown = r - c + N - 1;
			if(banUp.count(dUp) == 0 && banDown.count(dDown) == 0){
				adjU[dUp].push_back(dDown);
				adjV[dDown].push_back(dUp);
			}
		}
		/*for(int i = 0; i < adjU.size(); i++){
			cout << i << ": ";
			for(int j = 0; j < adjU[i].size(); j++) cout << adjU[i][j];
			cout << endl;
		}
		for(int i = 0; i < adjV.size(); i++){
			cout << i << ": ";
			for(int j = 0; j < adjV[i].size(); j++) cout << adjV[i][j];
			cout << endl;
		}*/
		vector <pair <int,int> > matching = hopcroftCarp(adjU, adjV);
		for(int i = 0; i < matching.size(); i++){
			int dUp = matching[i].first;
			int dDown = matching[i].second;
			int r = (dUp + dDown - N + 1) / 2;
			int c = (dUp - dDown + N - 1) / 2;
			Bnew[r][c] += 2;
			points++;
		}

		int changes = 0;
		for(int i = 0; i < N; i++) for(int j = 0; j < N; j++) if(B[i][j] != Bnew[i][j]) changes++;
		cout << "Case #" << t << ": " << points << " " << changes << endl;
		for(int i = 0; i < N; i++) for(int j = 0; j < N; j++) if(B[i][j] != Bnew[i][j]){
			switch(Bnew[i][j]){
				case 1: cout << 'x'; break;
				case 2: cout << '+'; break;
				case 3: cout << 'o'; break;
			}
			cout << " " << i + 1 << " " << j + 1 << endl;
		}
		
		/*cout << endl;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				cout << B[i][j];
			}
			cout << endl;
		}
		cout << endl;
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				cout << Bnew[i][j];
			}
			cout << endl;
		}*/
	}
  return 0;
}
