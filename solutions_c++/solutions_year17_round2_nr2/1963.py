#include <iostream>

using namespace std;

int main() {
	int TC; cin >> TC;
	int cont = 0;
	int colors[6];
	int N;
	string res;
	while (TC --) {
		int redBlocks = 0; int blueBLocks = 0; int yellowBlocks = 0;
		res.clear();
		bool impossible = false;
		cont++;
		cin >> N;
		for (int i = 0; i < 6; i++) {
			cin >> colors[i];
		}
		//RED BLOCKS
		if (colors[3] <= 2*colors[0]) {
			redBlocks = colors[3];
			colors[0] -= 2*redBlocks;
			colors[0] += redBlocks;
			colors [3] = 0;
		} else impossible = true;
		if (colors[5] <= 2*colors[2]) {
			yellowBlocks = colors[5];
			colors[2] -= 2*colors[5];
			colors[2] += yellowBlocks;
			colors[5] = 0;
		} else impossible = true;
		if (colors[1] <= 2*colors[4]) {
			blueBLocks = colors[1];
			colors[4] -= 2*colors[1];
			colors[4] += blueBLocks;;
			colors[1] = 0;
		}
		bool pick = true;
		int last = -1;
		while (pick && !impossible) {
			pick = false;
			int idxMaxColor = 0;
			int maxColor = 0;
			for (int i = 0; i < 6; i++) {
				if (colors[i] > maxColor && last != i) {
					maxColor = colors[i];
					idxMaxColor = i;
				}
			}
			//cout << idxMaxColor << "~";
			if (maxColor != 0) {
				int k = idxMaxColor;
				colors[k]--;
				pick = true;
				last = k;
				if (k == 0) {
					if (redBlocks > 0) {
						res += "RGR"; redBlocks --;
					} else res += "R";
				}
				else if (k == 2) {
					if (yellowBlocks > 0) {
						res += "YVY"; yellowBlocks --;
					} else res += "Y";
				}
				else if (k == 4) {
					if (blueBLocks > 0) {
						res += "BOB"; blueBLocks--;
					} else res +="B";
				}

			}


			

		}

		for (int i = 0; i < 6 && !impossible; i++) {
			if (colors[i] > 0) impossible = true;
		}
		if (res[0] == res[res.size() - 1]) {
			char aux = res[res.size() - 1];
			res[res.size() - 1] = res[res.size() - 2];
			res[res.size() - 2] = aux;
			if (res[res.size() - 1] == res[0] || res[res.size() - 2]  == res[res.size() - 1] || res[res.size() - 2]  == res[res.size() - 3]) 
				impossible = true;
		}
		

		cout << "Case #" << cont << ": ";
		if (impossible) cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;


	}




}