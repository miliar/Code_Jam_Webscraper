#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=1;i<=t;i++) {
		int N, R, O, Y, G, B, V;
		in >> N >> R >> O >> Y >> G >> B >> V;
		string s(N, ' ');
		int it(0);
		
		if (R == G && R+G == N) {
			for (int j=0;j<N;j+=2) {
				s[j] = 'R';
				s[j+1] = 'G';
			}
		} else if (Y == V && Y+V == N) {
			for (int j=0;j<N;j+=2) {
				s[j] = 'Y';
				s[j+1] = 'V';
			}
		} else if (B == O && B+O == N) {
			for (int j=0;j<N;j+=2) {
				s[j] = 'B';
				s[j+1] = 'O';
			}
		} else {
			bool GF(false),VF(false),OF(false);
			int RG = R-G;
			int YV = Y-V;
			int BO = B-O;
			if (G > 0) GF = true;
			if (V > 0) VF = true;
			if (O > 0) OF = true;
			if ((RG <= 0 && GF) || (YV <= 0 && VF) || (BO <= 0 && OF)) {
				s = "IMPOSSIBLE";
			} else if (RG > YV + BO || YV > BO + RG || BO > RG + YV) {
				s = "IMPOSSIBLE";
			} else {
				int prev = 0;
				int first = 0;
				while (RG > 0 || YV > 0 || BO > 0) {
					//cout << s << "|\t" << RG << "\t" << YV << "\t" << BO << "\t" << prev << "\t" << first << "\n";
					if ((RG > 0) && (first == 1 && YV <= BO + RG && BO <= RG + YV) && (prev != 1)) {
						if (GF) {
							GF = false;
							for (int j=0;j<G;j++) {
								s[it] ='R';
								s[it+1] ='G';
								it += 2;
							}
						}
						s[it] = 'R';
						it++;
						RG--;
						if (prev == 0) first = 1;
						prev = 1;
					} else if ((YV > 0) && (first == 2 && RG <= YV + BO && BO <= RG + YV) && (prev != 2)) {
						if (VF) {
							VF = false;
							for (int j=0;j<V;j++) {
								s[it] ='Y';
								s[it+1] ='V';
								it += 2;
							}
						}
						s[it] = 'Y';
						it++;
						YV--;
						if (prev == 0) first = 2;
						prev = 2;
					} else if ((BO > 0) && (first == 3 && YV <= BO + RG && RG <= YV + BO) && (prev != 3)) {
						if (OF) {
							OF = false;
							for (int j=0;j<O;j++) {
								s[it] ='B';
								s[it+1] ='O';
								it += 2;
							}
						}
						s[it] = 'B';
						it++;
						BO--;
						if (prev == 0) first = 3;
						prev = 3;
					} else if ((RG > 0) && ((RG >= YV || prev == 2) && (RG >= BO || prev == 3)) && (prev != 1)) {
						if (GF) {
							GF = false;
							for (int j=0;j<G;j++) {
								s[it] ='R';
								s[it+1] ='G';
								it += 2;
							}
						}
						s[it] = 'R';
						it++;
						RG--;
						if (prev == 0) first = 1;
						prev = 1;
					} else if ((YV > 0) && ((YV >= RG || prev == 1) && (YV >= BO || prev == 3)) && (prev != 2)) {
						if (VF) {
							VF = false;
							for (int j=0;j<V;j++) {
								s[it] ='Y';
								s[it+1] ='V';
								it += 2;
							}
						}
						s[it] = 'Y';
						it++;
						YV--;
						if (prev == 0) first = 2;
						prev = 2;
					} else if ((BO > 0) && ((BO >= RG || prev == 1) && (BO >= YV || prev == 2)) && (prev != 3)) {
						if (OF) {
							OF = false;
							for (int j=0;j<O;j++) {
								s[it] ='B';
								s[it+1] ='O';
								it += 2;
							}
						}
						s[it] = 'B';
						it++;
						BO--;
						if (prev == 0) first = 3;
						prev = 3;
					}
				}
			}
		}
		
		out << "Case #" << i << ": " << s << "\n";
		//cout << "Case #" << i << ": " << s << "\n";
	}
	return 0;
}

