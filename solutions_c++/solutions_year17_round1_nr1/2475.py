#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n, r, c;
	cin >> n;
	for (int l = 1; l <= n; l++) {
	    cin >> r >> c;
	    char cake[r][c];
	    for (int x = 0; x < r; x++) {
	        for (int i = 0; i < c; i++) {
	            cin >> cake[x][i];
	        }
	    }
	    cout << "Case #" << l << ":" << endl;
	    int w[300] = {0};
	    bool calc1[301] = {0};
	    for (int x = 0; x < r; x++) {
	        for (int i = 0; i < c; i++) {
	            if (cake[x][i] != '?' && !calc1[(int)cake[x][i]]) {
	                calc1[(int)cake[x][i]] = true;
	                int temp = i - 1;
	                while (temp >= 0) {
	                    if (cake[x][temp] == '?' || cake[x][temp] == cake[x][temp + 1]) {
	                        w[(int)cake[x][i]]++;
	                        cake[x][temp] = cake[x][i];
	                    } else {
	                        break;
	                    }
	                    temp--;
	                }
	                temp = i + 1;
	                while (temp < c) {
	                    if (cake[x][temp] == '?' || cake[x][temp] == cake[x][temp + 1]) {
	                        w[(int)cake[x][i]]++;
	                        cake[x][temp] = cake[x][i];
	                    } else {
	                        break;
	                    }
	                    temp++;
	                }
	                w[(int)cake[x][i]]++; //include itself
	            }
	        }
	    }
	    bool calc[301] = {0};
	    for (int x = 0; x < r; x++) {
	        for (int i = 0; i < c; i++) {
	            if (cake[x][i] != '?' && !calc[(int)cake[x][i]]) {
	                calc[(int)cake[x][i]] = true;
	                //cout << w[(int)cake[x][i]] << "!" << endl;
	                int temp = x - 1;
	                while (temp >= 0) {
	                    for (int a = i; a <= i + w[(int)cake[x][i]] - 1; a++) {
	                        if (cake[temp][a] != cake[x][i] && cake[temp][a] != '?') {
	                            temp = -1;
	                            break;
	                        } else if (a == i + w[(int)cake[x][i]] - 1) {
	                            for (int z = i; z <= a; z++) {
	                                cake[temp][z] = cake[x][i];
	                            }
	                        }
	                    }
	                    temp--;
	                }
	                temp = x + 1;
	                while (temp < r) {
	                    for (int a = i; a <= i + w[(int)cake[x][i]] - 1; a++) {
	                        if (cake[temp][a] != cake[x][i] && cake[temp][a] != '?') {
	                            temp = r;
	                            break;
	                        } else if (a == i + w[(int)cake[x][i]] - 1) {
	                            for (int z = i; z <= a; z++) {
	                                cake[temp][z] = cake[x][i];
	                            }
	                        }
	                    }
	                    temp++;
	                }
	            }
	        }
	    }
	    for (int x = 0; x < r; x++) {
	        for (int i = 0; i < c; i++) {
	            cout << cake[x][i];
	        } cout << endl;
	    }
	}
	return 0;
}